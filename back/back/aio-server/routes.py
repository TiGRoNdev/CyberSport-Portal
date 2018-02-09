from controllers import *


routes = [
    ('*', '/api/auth', auth, 'auth'),
    ('*', '/filldb', filldb, 'filldb'),  #для DEBUG

    ('GET', r'/api/games{id:/?\d*}{join_space:/?\w*}', games_GET, 'games_GET'),

    ('GET', r'/api/teams{id:/?\d*}{join_space:/?\w*}', teams_GET, 'teams_GET'),

    ('GET', r'/api/cups{id:/?\d*}{join_space:/?\w*}', cups_GET, 'cups_GET'),

    ('GET', r'/api/matches{id:/?\d*}{join_space:/?\w*}', matches_GET, 'matches_GET'),

    ('GET', r'/api/players{id:/?\d*}{join_space:/?\w*}', players_GET, 'players_GET'),
]