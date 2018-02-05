import asyncio
from aiotnt.operations import *


async def home():
    value = await get_games()
    return value
