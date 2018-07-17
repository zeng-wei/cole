import asyncio
import websockets
import json
from websockets.exceptions import ConnectionClosed
from asyncio.futures import TimeoutError
from websockets import WebSocketServerProtocol

# WebSocketServerProtocol()


class DataCarryServer:
    """
    功能：客户端分两组，A客户端组每一个成员发的消息要发给B客户端组全部成员
    """

    def __init__(self):
        self.websockets_a = []  # a组是发消息的
        self.websockets_b = []  # b组是收消息的

    def run(self):
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(
            websockets.serve(self.echo, '0.0.0.0', 5555))
        self.loop.run_forever()

    async def add_client(self, websocket):
        if websocket not in self.websockets_a and websocket not in self.websockets_b:
            try:
                msg = await asyncio.wait_for(websocket.recv(), timeout=0.1)
            except TimeoutError:
                pass
            else:
                print(msg)
                if msg == 'producer':
                    self.websockets_a.append(websocket)
                elif msg == 'consumer':
                    self.websockets_b.append(websocket)

    async def trans_data(self):
        for ws in self.websockets_a[:]:
            # print(await z.ensure_open())
            # try:
            #     await z.ensure_open()
            # except ConnectionClosed:
            #     print('ConnectionClosed')
            #     w.remove(z)
            #     continue
            # print(await ws.pong('pong'))

            try:
                try:
                    message = await asyncio.wait_for(ws.recv(), timeout=0.01)
                except TimeoutError:
                    continue
                print(message)
                for i in self.websockets_b[:]:
                    try:
                        await i.send(message)
                    except ConnectionClosed:
                        print('B ConnectionClosed')
                        self.websockets_b.remove(i)
                        continue
            except ConnectionClosed:
                print('A ConnectionClosed')
                self.websockets_a.remove(ws)
                continue

    async def echo(self, websocket, path):
        # help(websocket)
        # print(type(path))
        print(id(websocket))
        await self.add_client(websocket)

        print(self.websockets_a, self.websockets_b)
        while True:
            await self.trans_data()

        # for i in range(10000):
        #     await asyncio.sleep(10)


if __name__ == '__main__':
    DataCarryServer().run()