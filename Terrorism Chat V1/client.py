#Only edit if you know what you're doing
import websockets
import asyncio
import json
from colorama import Fore as C

with open('user.json', 'r') as f:
    info = json.load(f)

async def listen(room: int):
    with open('user.json', 'r') as f:
        info = json.load(f)

    with open('user.json', 'w') as f:
        info['ROOM'] = room
        json.dump(info, f)

    url = "wss://Websocket.sachsthebased.repl.co"

    async with websockets.connect(url) as ws:
        pass

    while True:
        message = input(f"{C.LIGHTGREEN_EX}Message: {C.RESET}")
        async with websockets.connect(url) as ws:
            await ws.send('{"Content": ' + '"' + message + '"' + ',"Token": ' + '"' + info['TOKEN'] + '"' + ',"Location": ' + str(room) + '}')

while True:
    print(f"""{C.LIGHTGREEN_EX}Options:
[1] Connect to Room
[2] View TOS{C.RESET}\n""")
    option = int(input(f"{C.LIGHTGREEN_EX}Option: {C.RESET}"))

    if option == 1:
        room = int(input(f"{C.LIGHTGREEN_EX}Room ID: {C.RESET}"))
        try: asyncio.get_event_loop().run_until_complete(listen(room))
        except: print("Could not connect... Retrying")
