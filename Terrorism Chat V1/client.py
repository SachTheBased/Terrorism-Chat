import websockets
import asyncio
import json
from colorama import Fore as C

with open('user.json', 'r') as f:
    info = json.load(f)

async def listen():
    url = "wss://Websocket.sachsthebased.repl.co"
    while True:
        message = input(f"{C.LIGHTBLUE_EX}Message: {C.RESET}")
        async with websockets.connect(url) as ws:
            await ws.send('{"Content": ' + '"' + message + '"' + ',"Token": ' + '"' + info['TOKEN'] + '"' + '}')

asyncio.get_event_loop().run_until_complete(listen())
