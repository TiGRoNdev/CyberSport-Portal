from aiotnt.connectors import get_db_connector


async def get_games():
    space = 'game'
    connector = await get_db_connector(space)
    values = await connector.select(space, key=[0])
    await connector.disconnect()
    return values.body

#async def add_game()
