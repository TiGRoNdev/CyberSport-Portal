from aiotnt.operations import *


async def home():
    await add_game('Dota2', 'The best Online game ever')
    await add_game('CS:GO', 'Online shooter')
    await add_game('PUBG', 'Online new survival shooter')
    value = await count('game')
    return value
