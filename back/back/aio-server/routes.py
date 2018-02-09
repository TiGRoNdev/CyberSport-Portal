from controllers import *


routes = [
    ('*', '/api/auth', auth, 'auth'),
    ('*', '/filldb', filldb, 'filldb'),  #для DEBUG

    ('GET', r'/api/games{id:/?\d*}{join_space:/?\w*}', games_GET, 'games'),

    ('*', r'/api/teams{id:\d*}{join_space:/\w*}', teams, 'teams'),

    ('GET', r'/api/cups{id:/?\d*}{join_space:/?\w*}', cups_GET, 'cups'),

    ('*', r'/api/matches{id:/?\d*}{join_space:/?\w*}', matches, 'matches'),
    ('*', r'/api/players{id:/?\d*}{join_space:/?\w*}', players, 'players'),
]