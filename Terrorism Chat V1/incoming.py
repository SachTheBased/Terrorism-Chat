import websockets
import asyncio
from colorama import Fore as C

async def listen():
    url = "wss://Websocket.sachsthebased.repl.co"
    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            print(C.LIGHTGREEN_EX + msg + C.RESET)
asyncio.get_event_loop().run_until_complete(listen())
