import asyncio
import websockets
import time
import json


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        # time.sleep(3)
        # pong = await websocket.ping('ping')
        # await pong
        await websocket.send('b')
        await websocket.send(json.dumps((1, 'hello')))
        while True:
            print(await websocket.recv())

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))