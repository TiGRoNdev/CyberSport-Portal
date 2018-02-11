from fillDB import fill
from models import *


def datetime_from_tnt(obj):
    return datetime(obj[2], obj[1], obj[0], hour=obj[3], minute=obj[4])


async def filltnt():
    await fill()
    text = 'Successfully filled DB'
    return text


async def home():
    text = 'Hello! to filling DB open /filldb'
    return text


async def teams_in_game(id_game, limit=100000, sort_by='nosort', reverse=False):
    game = Game()
    gameobject = await game.get_by_id(id_game)
    team = Team()
    teams = await team.search('id_game', 'EQ', id_game, limit)
    if sort_by == 'rating':
        teams.sort(key=lambda x: x[4], reverse=reverse)
    elif sort_by == 'name':
        teams.sort(key=lambda x: x[1], reverse=reverse)
    teams_json = [{'id': t[0],
                   'name': t[1],
                   'description': t[2],
                   'logo': t[3],
                   'rating': t[4],
                   'id_game': t[5]} for t in teams]
    return {'game': gameobject, 'teams': teams_json}


async def players_in_game(id_game, limit=100000, sort_by='nosort', reverse=False):
    game = Game()
    gameobject = await game.get_by_id(id_game)
    player = Player()
    players = await player.search('id_game', 'EQ', id_game, limit)
    if sort_by == 'rating':
        players.sort(key=lambda x: x[4], reverse=reverse)
    elif sort_by == 'name':
        players.sort(key=lambda x: x[1], reverse=reverse)
    players_json = [{'id': t[0],
                     'name': t[1],
                     'description': t[2],
                     'logo': t[3],
                     'rating': t[4],
                     'id_game': t[5],
                     'id_team': t[6]} for t in players]
    return {'game': gameobject, 'players': players_json}


async def cups_in_game(id_game, limit=100000, sort_by='nosort', reverse=False):
    game = Game()
    gameobject = await game.get_by_id(id_game)
    cup = Cup()
    cups = await cup.search('id_game', 'EQ', id_game, limit)
    if sort_by == 'rating':
        cups.sort(key=lambda x: x[4], reverse=reverse)
    elif sort_by == 'name':
        cups.sort(key=lambda x: x[1], reverse=reverse)
    cups_json = [{'id': t[0],
                  'name': t[1],
                  'description': t[3],
                  'logo': t[2],
                  'rating': t[4],
                  'id_game': t[5]} for t in cups]
    return {'game': gameobject, 'cups': cups_json}


async def teams_in_cup(id_cup, limit=100000, sort_by='nosort', reverse=False):
    cup = Cup()
    cupobject = await cup.get_by_id(id_cup)
    stage = Stage()
    stages = await stage.search('id_cup', 'EQ', id_cup, 15)
    id_stages = [t[0] for t in stages]
    match = Match()
    matches = []
    for id_stage in id_stages:
        matches.extend(await match.search('id_stage', 'EQ', id_stage, int(limit/len(id_stages))))
    id_matches = [t[0] for t in matches]
    teammatch = TeamMatch()
    teammatches = []
    for id_match in id_matches:
        teammatches = await teammatch.search('id_match', 'EQ', id_match, 3)
    id_teams = [t[1] for t in teammatches]
    team = Team()
    teams = []
    for id_1 in id_teams:
        teams.append(await team.get_by_id(id_1))
    if sort_by == 'rating':
        teams.sort(key=lambda x: x[4], reverse=reverse)
    elif sort_by == 'name':
        teams.sort(key=lambda x: x[1], reverse=reverse)
    teams_json = [{'id': t[0],
                   'name': t[1],
                   'description': t[2],
                   'logo': t[3],
                   'rating': t[4],
                   'id_game': t[5]} for t in teams]
    return {'cup': cupobject, 'teams': teams_json}


async def players_in_cup(id_cup, limit=100000, sort_by='nosort', reverse=False):
    cup = Cup()
    cupobject = await cup.get_by_id(id_cup)
    stage = Stage()
    stages = await stage.search('id_cup', 'EQ', id_cup, 15)
    id_stages = [t[0] for t in stages]
    match = Match()
    matches = []
    for id_stage in id_stages:
        matches.extend(await match.search('id_stage', 'EQ', id_stage, int(limit / len(id_stages))))
    id_matches = [t[0] for t in matches]
    teammatch = TeamMatch()
    teammatches = []
    added_players = []
    all_players = []
    deleted_players = []
    for id_match in id_matches:
        teammatches = await teammatch.search('id_match', 'EQ', id_match, 3)
    for onematch in teammatches:
        added_players.extend(onematch[2])
        deleted_players.extend(onematch[3])
    id_teams = [t[1] for t in teammatches]
    player = Player()
    for id_team in id_teams:
        all_players.extend(await player.search('id_team', 'EQ', id_team, 100))
    for oneplayer in all_players:
        if oneplayer[0] in deleted_players:
            all_players.remove(oneplayer)
    for oneplayer_id in added_players:
        all_players.append(await player.get_by_id(oneplayer_id))
    # Дальше сортировка и возврат all_players
    if sort_by == 'rating':
        all_players.sort(key=lambda x: x[4], reverse=reverse)
    elif sort_by == 'name':
        all_players.sort(key=lambda x: x[1], reverse=reverse)
    players_json = [{'id': t[0],
                     'name': t[1],
                     'description': t[2],
                     'logo': t[3],
                     'rating': t[4],
                     'id_game': t[5],
                     'id_team': t[6]} for t in all_players]
    return {'cup': cupobject, 'players': players_json}


async def cup_and_stages(id_cup):
    cup = Cup()
    cupobject = await cup.get_by_id(id_cup)
    stage = Stage()
    stages = await stage.search('id_cup', 'EQ', id_cup, 15)
    stages_json = [{'type': t[1],
                    'body': {'id': t[0],
                             'start': t[2],
                             'end': t[3],
                             'description': t[4],
                             'id_cup': t[5]}} for t in stages]
    return {'cup': cupobject, 'stages': stages_json}


async def matches_in_cup(id_cup):
    cup = Cup()
    cupobject = await cup.get_by_id(id_cup)
    stage = Stage()
    stages = await stage.search('id_cup', 'EQ', id_cup, 15)
    id_stages = [t[0] for t in stages]
    match = Match()
    matches = []
    for id_stage in id_stages:
        matches.extend(await match.search('id_stage', 'EQ', id_stage, 100))
    matches.sort(key=lambda x: len(x[2]))
    matches_json = [{'id': t[0],
                     'start': t[1],
                     'status': t[2],
                     'name': t[3],
                     'description': t[4],
                     'logo': t[5],
                     'uri_video': t[6],
                     'id_winner': t[7],
                     'id_stage': t[8]} for t in matches]
    return {'cup': cupobject, 'matches': matches_json}


async def cups_in_team(id_team, limit=100000):
    team = Team()
    teamobject = await team.get_by_id(id_team)
    teammatch = TeamMatch()
    teammatches = await teammatch.search('id_team', 'EQ', id_team, limit)
    id_matches = [t[4] for t in teammatches]
    cups = []
    match = Match()
    stage = Stage()
    cup = Cup()
    for id_match in id_matches:
        match1 = await match.get_by_id(id_match)
        stage1 = await stage.get_by_id(match1['id_stage'])
        cups.append(await cup.get_by_id(stage1['id_cup']))
    return {'team': teamobject, 'cups': cups}


async def matches_in_team(id_team, limit=100000):
    team = Team()
    teamobject = await team.get_by_id(id_team)
    teammatch = TeamMatch()
    teammatches = await teammatch.search('id_team', 'EQ', id_team, limit)
    id_matches = [t[4] for t in teammatches]
    matches = []
    match = Match()
    for id_match in id_matches:
        matches.append(await match.get_by_id(id_match))
    return {'team': teamobject, 'matches': matches}


async def team_and_players(id_team, sort_by='nosort', reverse=False):
    team = Team()
    teamobject = await team.get_by_id(id_team)
    player = Player()
    players = await player.search('id_team', 'EQ', id_team, 100)
    if sort_by == 'rating':
        players.sort(key=lambda x: x[4], reverse=reverse)
    elif sort_by == 'name':
        players.sort(key=lambda x: x[1], reverse=reverse)
    players_json = [{'id': t[0],
                     'name': t[1],
                     'description': t[2],
                     'logo': t[3],
                     'rating': t[4],
                     'id_game': t[5],
                     'id_team': t[6]} for t in players]
    return {'team': teamobject, 'players': players_json}


async def live_matches(limit=1000):
    match = Match()
    matches = await match.search('status', 'EQ', 'LIVE', limit)
    matches_json = [{'id': t[0],
                     'start': t[1],
                     'status': t[2],
                     'name': t[3],
                     'description': t[4],
                     'logo': t[5],
                     'uri_video': t[6],
                     'id_winner': t[7],
                     'id_stage': t[8]} for t in matches]
    return {'matches': matches_json}


async def top_players(limit=100):
    player = Player()
    players = await player.get_all()
    players.sort(key=lambda x: x['rating'], reverse=True)
    players = players[:limit]
    return {'players': players}


async def my_teams(user_id):
    team = Team()
    teams = await team.search('owner', 'EQ', user_id, 100)
    myteams = [{
        'id': k[0],
        'name': k[1],
        'description': k[2],
        'logo': k[3],
        'rating': k[4],
        'id_game': k[5],
        'owner': k[6]
    } for k in teams]
    return {'message': "All your teams", 'teams': myteams}


async def my_cups(user_id):
    cup = Cup()
    cups = await cup.search('owner', 'EQ', user_id, 100)
    mycups = [{
        'id': k[0],
        'name': k[1],
        'logo': k[2],
        'description': k[3],
        'rating': k[4],
        'id_game': k[5],
        'owner': k[6]
    } for k in cups]
    return {'message': "All your cups", 'cups': mycups}
