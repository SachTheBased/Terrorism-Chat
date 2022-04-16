import websockets
import asyncio
import socket
import json

PORT = 1000
print("Server listening on Port " + str(PORT))

connected = set()

async def history(websocket):
    with open('messages.json', 'r') as f:
        messages = json.load(f)
    for message in messages["Messages"]:
        await websocket.send(f"{message['Author']}: {message['Content']}")

async def echo(websocket, path):
    connected.add(websocket)
    await history(websocket)
    try:
        async for message in websocket:
            message = json.loads(message)
            for conn in connected:
                if conn != websocket:
                  with open('users.json', 'r') as f:
                    tokens = json.load(f)
                  await conn.send(f"{tokens[message['Token']]['Username']}: {message['Content']}")
                  with open('messages.json', 'r') as f:
                    contents = json.load(f)
                  with open('messages.json', 'w') as f:
                    contents["Messages"].append({"Author": tokens[message['Token']]['Username'], "Content": message['Content']})
                    json.dump(contents, f)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
    finally:
        connected.remove(websocket)

start_server = websockets.serve(echo, "0.0.0.0", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
