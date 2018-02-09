from fillDB import fill
from models import *


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
