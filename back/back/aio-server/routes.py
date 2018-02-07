from controllers import *
from apicontrollers import *


routes = [
    ('GET', '/', index, 'index'),
    ('GET', '/filldb', filldb, 'filldb'),  #для DEBUG
    ('GET', '/game', game, 'game'),
    ('GET', '/team', team, 'team'),
    ('GET', '/cup', cup, 'cup'),
    ('GET', '/match', match, 'match'),
    ('GET', '/player', player, 'player'),
    ('GET', '/top/cup', top_cup, 'top_cup'),
    ('GET', '/top/player', top_player, 'top_player'),

    ('*', r'/api/game/{name:\d*}', apiGame, 'api_game'),
    ('*', r'/api/team/{name:\d*}', apiTeam, 'api_team'),
    ('*', r'/api/cup/{name:\d*}', apiCup, 'api_cup'),
    ('*', r'/api/match/{name:\d*}', apiMatch, 'api_match'),
    ('*', r'/api/player/{name:\d*}', apiPlayer, 'api_player')
]