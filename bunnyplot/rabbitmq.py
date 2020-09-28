import asyncio
import aiohttp
import async_timeout
import logging
from base64 import b64encode

TIMEOUT = 10
logger = logging.Logger(__name__)


class RabbitMQApi:
    def __init__(self, url, username, password):
        self.__url = url
        basic_credentials = b64encode(f"{username}:{password}".encode()).decode()
        self.__auth = f"Basic {basic_credentials}"

    def __get_url(self, endpoint):
        return self.__url + endpoint

    async def get_definitions(self):
        async with aiohttp.ClientSession() as session:
            async with async_timeout.timeout(TIMEOUT):
                async with session.get(
                    self.__get_url("/api/definitions"),
                    headers={"Authorization": self.__auth},
                ) as response:
                    return await response.json()

    async def get_consumers(self):
        async with aiohttp.ClientSession() as session:
            async with async_timeout.timeout(TIMEOUT):
                async with session.get(
                    self.__get_url("/api/consumers"),
                    headers={"Authorization": self.__auth},
                ) as response:
                    return await response.json()
