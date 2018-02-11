from aiotnt.connectors import get_db_connector


async def count(space):
    connector = await get_db_connector(space)
    val = await connector.call('mod_len', [space])
    await connector.disconnect()
    return val.body[0]


async def get_all(space):
    connector = await get_db_connector(space)
    values = await connector.select(space, index='primary', limit=100000, tuple_as_dict=True)
    await connector.disconnect()
    return values.body


async def get_obj_by_id(space, id):
    connector = await get_db_connector(space)
    value = await connector.select(space, [id], tuple_as_dict=True)
    await connector.disconnect()
    try:
        response = value.body[0]
    except IndexError:
        return '404'
    return response


async def search_by_index(space, index, iter, value, lim):
    connector = await get_db_connector(space)
    val = await connector.call('mod_search', [space, index, value, iter, lim])
    await connector.disconnect()
    return val.body[0]


async def add_obj(space, *args):
    connector = await get_db_connector(space)
    response = await connector.call('mod_insert', [space, args])
    await connector.disconnect()
    try:
        response = response.body[0]
    except IndexError:
        return '500'
    return response


async def delete_obj(space, id):
    connector = await get_db_connector(space)
    response = await connector.delete(space, id)
    await connector.disconnect()
    try:
        response = response.body[0]
    except IndexError:
        return '500'
    return response


async def update_obj(space, id, operations):
    connector = await get_db_connector(space)
    response = await connector.update(space, [id], operations, tuple_as_dict=True)
    await connector.disconnect()
    try:
        response = response.body[0]
    except IndexError:
        return '500'
    return response
