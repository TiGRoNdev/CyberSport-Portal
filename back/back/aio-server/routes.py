from controllers import *


routes = [
    ('*', '/', index, 'index'),
    ('*', '/filldb', filldb, 'filldb'),  #для DEBUG
    ('*', '/game', game, 'game'),
    ('*', '/team', team, 'team'),
    ('*', '/cup', cup, 'cup'),
    ('*', '/match', match, 'match'),
    ('*', '/player', player, 'player'),
    ('*', '/top/cup', top_cup, 'top_cup'),
    ('*', '/top/player', top_player, 'top_player')
]