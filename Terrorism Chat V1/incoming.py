import websockets
import asyncio
import json
from colorama import Fore as C

async def listen():
    url = "wss://Websocket.sachsthebased.repl.co"
    async with websockets.connect(url) as ws:
        while True:
            with open('user.json', 'r') as f:
                info = json.load(f)
            msg = await ws.recv()
            msg = json.loads(msg)
            if msg['Location'] == int(info['ROOM']):
                print(f"{C.LIGHTGREEN_EX}{msg['Author']}: {msg['Content']}{C.RESET}")

while True:
    try: asyncio.get_event_loop().run_until_complete(listen())
    except: print("Could not connect... Retrying")
