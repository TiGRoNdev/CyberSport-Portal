from os.path import isfile
from envparse import env
import logging


log = logging.getLogger('app')
log.setLevel(logging.DEBUG)

f = logging.Formatter('[L:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', datefmt = '%d-%m-%Y %H:%M:%S')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(f)
log.addHandler(ch)

if isfile('.env'):
    env.read_envfile('.env')

DEBUG = env.bool('DEBUG', default=False)
HOST = env.str('HOST')
PORT = env.int('PORT')

DB_USER = env.str('DB_USER')
DB_PASS = env.str('DB_PASS')

SHARDING = env.bool('SHARDING')

SHARDS = {}
'''
    Структура словаря SHARDS выглядит таким образом:
        {
            'count': количество шардов(мастеров),
            'count_replics': количество реплик одного шарда(мастера),
            'SHARD<номер шарда мастера>': [ip адрес, порт],
            'SHARD<номер шарда мастера>_SPACES': [список пространств(таблиц) в определенном шарде],
            'SHARD<номер шарда мастера>_REPLICA<номер реплики>': [ip реплики, порт реплики],
            ... и т.д.
        }
'''

if SHARDING:
    SHARDS['count'] = env.int('SHARDS_COUNT')
    SHARDS['count_replics'] = env.int('REPLICS_OF_SHARD')
    for i in range(SHARDS['count']):
        name = 'SHARD{}'.format(i+1)
        SHARDS[name] = [env.str('{}_HOST'.format(name)),
                        env.int('{}_PORT'.format(name))]
        SHARDS[name + '_SPACES'] = env.list(name + '_SPACES')
        for k in range(SHARDS['count_replics']):
            name_rep = (name + '_REPLICA' + str(k+1))
            SHARDS[name_rep] = [env.str(name_rep + '_HOST'),
                                env.int(name_rep + '_PORT')]
else:
    DB_HOST = env.str('DB_HOST')
    DB_PORT = env.int('DB_PORT')
