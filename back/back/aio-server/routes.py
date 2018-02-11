from controllers import *
from auth.controllers import register, login


routes = [
    ('POST', '/api/register', register, 'register'),
    ('POST', '/api/login', login, 'login'),

    ('*', '/filldb', filldb, 'filldb'),  #для DEBUG

    ('GET', r'/api/games{id:/?\d*}{join_space:/?\w*}', games_GET, 'games_GET'),

    ('GET', r'/api/teams{id:/?\d*}{join_space:/?\w*}', teams_GET, 'teams_GET'),
    ('GET', '/api/my/teams', my_teams_GET, 'my_teams_GET'),
    ('POST', '/api/my/teams', teams_POST, 'teams_POST'),

    ('GET', r'/api/players{id:/?\d*}', players_GET, 'players_GET'),
    ('POST', '/api/my/players', players_POST, 'players_POST'),

    ('GET', r'/api/cups{id:/?\d*}{join_space:/?\w*}', cups_GET, 'cups_GET'),
    ('GET', r'/api/my/cups', my_cups_GET, 'my_cups_GET'),
    ('POST', r'/api/my/cups', cups_POST, 'cups_POST'),

    ('GET', r'/api/matches{id:/?\d*}', matches_GET, 'matches_GET'),
    #('POST', r'/api/my/matches', matches_POST, 'matches_POST'),
]