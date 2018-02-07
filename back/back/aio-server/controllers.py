import json
from aiohttp import web
from logic import home, filltnt


async def index(request):
    text = await home()
    response = json.dumps({'title': 'aio-server', 'text': str(text)})
    return web.Response(body=response, status=200, content_type='application/json')


async def filldb(request):
    text = await filltnt()
    response = json.dumps({'title': 'Tarantool-DB', 'text': str(text)})
    return web.Response(body=response, status=200, content_type='application/json')


async def game(request):
    pass


async def team(request):
    pass


async def match(request):
    pass


async def player(request):
    pass


async def cup(request):
    pass


async def top_cup(request):
    pass


async def top_player(request):
    pass
