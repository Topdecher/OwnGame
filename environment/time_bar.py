import asyncio


class TimeBar:
    def __init__(self, time: int):
        self.time = time

    async def process(self):
        while self.time > 0:
            await asyncio.sleep(1)
            self.time -= 1
