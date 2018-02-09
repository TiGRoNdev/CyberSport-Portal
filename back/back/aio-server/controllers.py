import json
from aiohttp import web
from logic import *
from models import *


async def auth(request):
    pass


async def filldb(request):
    text = await filltnt()
    response = json.dumps({'title': 'Tarantool-DB', 'text': str(text)})
    return web.Response(body=response, status=200, content_type='application/json')


async def games_GET(request):
    game = Game()
    id_1 = request.match_info.get('id')
    join_space = request.match_info.get('join_space')
    try:
        limit = request.query['lim']
        limit = int(limit)
    except (KeyError, ValueError):
        limit = 100000
    try:
        sort = request.query['sort']
        sort = str(sort)
    except (KeyError, ValueError):
        sort = 'nosort'
    try:
        reverse = request.query['reverse']
        reverse = bool(reverse)
    except (KeyError, ValueError):
        reverse = False
    if id_1 != '':
        id_1 = id_1[1:]
        if join_space != '':
            if join_space == '/teams':
                return web.Response(body=json.dumps(await teams_in_game(int(id_1), limit=int(limit),
                                                                        sort_by=sort, reverse=bool(reverse))),
                                    status=200,
                                    content_type='application/json')
            if join_space == '/players':
                return web.Response(body=json.dumps(await players_in_game(int(id_1), limit=int(limit),
                                                                          sort_by=sort, reverse=bool(reverse))),
                                    status=200,
                                    content_type='application/json')
            if join_space == '/cups':
                return web.Response(body=json.dumps(await cups_in_game(int(id_1), limit=int(limit),
                                                                       sort_by=sort, reverse=bool(reverse))),
                                    status=200,
                                    content_type='application/json')
        return web.Response(body=json.dumps(await game.get_by_id(int(id_1))),
                            status=200,
                            content_type='application/json')
    return web.Response(body=json.dumps(await game.get_all()),
                        status=200,
                        content_type='application/json')


async def cups_GET(request):
    cup = Cup()
    id_1 = request.match_info.get('id')
    join_space = request.match_info.get('join_space')
    try:
        limit = request.query['lim']
        limit = int(limit)
    except (KeyError, ValueError):
        limit = 100000
    try:
        sort = request.query['sort']
        sort = str(sort)
    except (KeyError, ValueError):
        sort = 'nosort'
    try:
        reverse = request.query['reverse']
        reverse = bool(reverse)
    except (KeyError, ValueError):
        reverse = False
    if id_1 != '':
        id_1 = id_1[1:]
        if join_space != '':
            if join_space == '/teams':
                return web.Response(body=json.dumps(await teams_in_cup(int(id_1), limit=int(limit),
                                                                       sort_by=sort, reverse=bool(reverse))),
                                    status=200,
                                    content_type='application/json')
            if join_space == '/players':
                return web.Response(body=json.dumps(await players_in_cup(int(id_1), limit=int(limit),
                                                                         sort_by=sort, reverse=bool(reverse))),
                                    status=200,
                                    content_type='application/json')
            if join_space == '/matches':
                return web.Response(body=json.dumps(await matches_in_cup(int(id_1))),
                                    status=200,
                                    content_type='application/json')
        return web.Response(body=json.dumps(await cup_and_stages(int(id_1))),
                            status=200,
                            content_type='application/json')
    return web.Response(body=json.dumps(await cup.get_all()),
                        status=200,
                        content_type='application/json')


async def teams_GET(request):
    team = Team()
    id_1 = request.match_info.get('id')
    join_space = request.match_info.get('join_space')
    try:
        limit = request.query['lim']
        limit = int(limit)
    except (KeyError, ValueError):
        limit = 100000
    try:
        sort = request.query['sort']
        sort = str(sort)
    except (KeyError, ValueError):
        sort = 'nosort'
    try:
        reverse = request.query['reverse']
        reverse = bool(reverse)
    except (KeyError, ValueError):
        reverse = False
    if id_1 != '':
        id_1 = id_1[1:]
        if join_space != '':
            if join_space == '/cups':
                return web.Response(body=json.dumps(await cups_in_team(int(id_1), limit=int(limit))),
                                    status=200,
                                    content_type='application/json')
            if join_space == '/matches':
                return web.Response(body=json.dumps(await matches_in_team(int(id_1), limit=int(limit))),
                                    status=200,
                                    content_type='application/json')
        return web.Response(body=json.dumps(await team_and_players(int(id_1), sort_by=sort, reverse=reverse)),
                            status=200,
                            content_type='application/json')
    return web.Response(body=json.dumps(await team.get_all()),
                        status=200,
                        content_type='application/json')


async def matches(request):
    match = Match()
    json_possible = await match.get_all()
    response = json.dumps({'title': 'All matches from Tarantool-DB', 'text': json_possible})
    return web.Response(body=response, status=200, content_type='application/json')
    pass


async def players(request):
    player = Player()
    json_possible = await player.get_all()
    response = json.dumps({'title': 'All players from Tarantool-DB', 'text': json_possible})
    return web.Response(body=response, status=200, content_type='application/json')
