from aiotnt.connectors import get_db_connector


async def count(space):
    connector = await get_db_connector(space)
    values = await connector.select(space, [1], index='primary')
    await connector.disconnect()
    return len(values.body)


async def get_all(space):
    connector = await get_db_connector(space)
    values = await connector.select(space, index='primary')
    await connector.disconnect()
    return values.body


async def add_game(name, description, logo='/static/img/logo/game/default.png'):
    connector = await get_db_connector('game')
    await connector.call('mod_insert', ['game', [
        name,
        logo,
        description
    ]])
    await connector.disconnect()


