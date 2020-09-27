import asyncio
class RabbitMQApi:
    def __init__(self, url, auth):
        self.url = url
        self.auth = auth
    
    async def get_definitions(self):
        print("get_definitions begin")
        await asyncio.sleep(2)
        print("get_definitions end")
        return "get_definitions"

    async def get_consumers(self):
        print("get_consumers begin")
        await asyncio.sleep(1)
        print("get_consumers end")
        return "get_consumers"