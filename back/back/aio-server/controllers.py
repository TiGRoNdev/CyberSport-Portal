import json
from aiohttp import web
from logic import *
from models import *
from auth.tools import login_required


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


async def matches_GET(request):
    match = Match()
    id_1 = request.match_info.get('id')
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
    if id_1 != '':
        id_1 = id_1[1:]
        if sort == 'live':
            return web.Response(body=json.dumps(await live_matches(limit=int(limit))),
                                status=200,
                                content_type='application/json')
        return web.Response(body=json.dumps(await match.get_by_id(int(id_1))),
                            status=200,
                            content_type='application/json')
    return web.Response(body=json.dumps(await match.get_all()),
                        status=200,
                        content_type='application/json')


async def players_GET(request):
    player = Player()
    id_1 = request.match_info.get('id')
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
    if id_1 != '':
        id_1 = id_1[1:]
        if sort == 'top':
            return web.Response(body=json.dumps(await top_players(limit=int(limit))),
                                status=200,
                                content_type='application/json')
        return web.Response(body=json.dumps(await player.get_by_id(int(id_1))),
                            status=200,
                            content_type='application/json')
    return web.Response(body=json.dumps(await player.get_all()),
                        status=200,
                        content_type='application/json')


# ---------------->
#
#       NEXT CONTROLLERS LOGIN REQUIRED
#
# ---------------->


@login_required
async def my_teams_GET(request):
    if not request.user['is_team']:
        return web.Response(body=json.dumps({'message': "Not Found. Only teams-users have teams"}),
                            status=404,
                            content_type='application/json')
    return web.Response(body=json.dumps(await my_teams(request.user['id'])),
                        status=200,
                        content_type='application/json')


@login_required
async def teams_POST(request):
    if not request.user['is_team']:
        return web.Response(body=json.dumps({'message': "Permission denied. Only teams-users can create teams"}),
                            status=403,
                            content_type='application/json')
    post_data = await request.json()
    try:
        new_teams = post_data['new_teams']
        tmp = new_teams[0]['name']
        tmp = new_teams[0]['description']
        tmp = new_teams[0]['id_game']
    except (KeyError, IndexError):
        return web.Response(body=json.dumps({'message': 'Missing one of the required fields'}),
                            status=400,
                            content_type='application/json')
    game = Game()
    the_games = []
    for k in new_teams:
        the_game = await game.get_by_id(k['id_game'])
        if the_game == '404':
            return web.Response(body=json.dumps({'message': "Game with that id not found"}),
                                status=404,
                                content_type='application/json')
        the_games.append(the_game)
    team = Team()
    new_teams_ids = []
    i = 0
    try:
        for new_team in new_teams:
            new_teams_ids.append(await team.add(new_team['name'],
                                                new_team['description'],
                                                the_games[i]['id'],
                                                request.user['id']))
            i += 1
    except ValueError:
        return web.Response(body=json.dumps({'message': "Teams exist"}),
                            status=400,
                            content_type='application/json')
    return web.Response(body=json.dumps({'message': "Teams added", 'id_teams': new_teams_ids}),
                        status=200,
                        content_type='application/json')


@login_required
async def players_POST(request):
    if not request.user['is_team']:
        return web.Response(body=json.dumps({'message': "Permission denied. Only teams-users can create players"}),
                            status=403,
                            content_type='application/json')
    post_data = await request.json()
    try:
        team_id = post_data['team_id']
        new_players = post_data['new_players']
        tmp = new_players[0]['name']
        tmp = new_players[0]['description']
    except (KeyError, IndexError):
        return web.Response(body=json.dumps({'message': 'Missing one of the required fields'}),
                            status=400,
                            content_type='application/json')
    team = Team()
    the_team = await team.get_by_id(team_id)
    if the_team == '404':
        return web.Response(body=json.dumps({'message': "Team not found"}),
                            status=404,
                            content_type='application/json')
    if the_team['owner'] != request.user['id'] and not request.user['is_admin']:
        return web.Response(body=json.dumps({'message': "Permission denied. You can add players only for your team"}),
                            status=403,
                            content_type='application/json')
    player = Player()
    new_players_ids = []
    try:
        for new_player in new_players:
            new_players_ids.append(await player.add(new_player['name'],
                                                    new_player['description'],
                                                    the_team['id_game'],
                                                    the_team['id']))
    except ValueError:
        return web.Response(body=json.dumps({'message': "Players exist"}),
                            status=400,
                            content_type='application/json')
    return web.Response(body=json.dumps({'message': "Players added", 'id_players': new_players_ids}),
                        status=200,
                        content_type='application/json')
