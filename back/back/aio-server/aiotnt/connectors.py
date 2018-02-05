import asynctnt
import asynctnt.exceptions
from settings import SHARDS, DB_USER, DB_PASS


async def get_db_connector(space):
    num = 0  # здесь вычисляем номер нужного шарда, в котором находится пространство
    for i in range(SHARDS['count']):
        name = 'SHARD' + str(i + 1) + '_SPACES'
        if space in SHARDS[name]:
            num = i + 1
            break
    connector = asynctnt.Connection(host=SHARDS['SHARD' + str(num)][0],
                                    port=SHARDS['SHARD' + str(num)][1],
                                    username=DB_USER,
                                    password=DB_PASS)
    try:
        await connector.connect()
    except asynctnt.exceptions.TarantoolError:
        for i in range(SHARDS['count_replics']):
            connector = asynctnt.Connection(host=SHARDS['SHARD' + str(num) + '_REPLICA' + str(i + 1)][0],
                                            port=SHARDS['SHARD' + str(num) + '_REPLICA' + str(i + 1)][1],
                                            username=DB_USER,
                                            password=DB_PASS)
            try:
                await connector.connect()
            except asynctnt.exceptions.TarantoolError:
                continue
            else:
                break
            finally:
                raise asynctnt.exceptions.TarantoolError
    return connector



