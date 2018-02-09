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
                                    reconnect_timeout=0,
                                    initial_read_buffer_size=600,
                                    username=DB_USER,
                                    password=DB_PASS)
    try:
        await connector.connect()
    except ConnectionRefusedError:
        for i in range(SHARDS['count_replics']):
            connector = asynctnt.Connection(host=SHARDS['SHARD' + str(num) + '_REPLICA' + str(i + 1)][0],
                                            port=SHARDS['SHARD' + str(num) + '_REPLICA' + str(i + 1)][1],
                                            reconnect_timeout=0,
                                            initial_read_buffer_size=600,
                                            username=DB_USER,
                                            password=DB_PASS)
            try:
                await connector.connect()
            except ConnectionRefusedError:
                continue
            else:
                return connector
        raise asynctnt.exceptions.TarantoolError("I can't connect"
                                                 " to my DB host={}, port={}".format(
            SHARDS['SHARD' + str(num) + '_REPLICA' + str(1)][0], SHARDS['SHARD' + str(num) + '_REPLICA' + str(1)][1]))
    return connector



