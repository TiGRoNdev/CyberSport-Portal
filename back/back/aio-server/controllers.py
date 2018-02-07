import json
from aiohttp import web
from logic import *
from models import *


async def index(request):
    text = await home()
    response = json.dumps({'title': 'aio-server', 'text': str(text)})
    return web.Response(body=response, status=200, content_type='application/json')


async def filldb(request):
    text = await filltnt()
    response = json.dumps({'title': 'Tarantool-DB', 'text': str(text)})
    return web.Response(body=response, status=200, content_type='application/json')


async def game(request):
    games = Game()
    json_possible = await games.get_all()
    response = json.dumps({'title': 'All games from Tarantool-DB', 'text': json_possible})
    return web.Response(body=response, status=200, content_type='application/json')


async def team(request):
    teams = Team()
    json_possible = await teams.get_all()
    response = json.dumps({'title': 'All teams from Tarantool-DB', 'text': json_possible})
    return web.Response(body=response, status=200, content_type='application/json')


async def match(request):
    matches = Match()
    json_possible = await matches.get_all()
    response = json.dumps({'title': 'All matches from Tarantool-DB', 'text': json_possible})
    return web.Response(body=response, status=200, content_type='application/json')
    pass


async def player(request):
    players = Player()
    json_possible = await players.get_all()
    response = json.dumps({'title': 'All players from Tarantool-DB', 'text': json_possible})
    return web.Response(body=response, status=200, content_type='application/json')


async def cup(request):
    cups = Cup()
    json_possible = await cups.get_all()
    response = json.dumps({'title': 'All cups from Tarantool-DB', 'text': json_possible})
    return web.Response(body=response, status=200, content_type='application/json')


async def top_cup(request):
    pass


async def top_player(request):
    pass
