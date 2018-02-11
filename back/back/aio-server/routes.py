from controllers import *
from auth.controllers import register, login


routes = [
    ('POST', '/api/register', register, 'register'),
    ('POST', '/api/login', login, 'login'),

    ('*', '/filldb', filldb, 'filldb'),  #для DEBUG

    ('GET', r'/api/games{id:/?\d*}{join_space:/?\w*}', games_GET, 'games_GET'),

    ('GET', r'/api/teams{id:/?\d*}{join_space:/?\w*}', teams_GET, 'teams_GET'),

    ('GET', r'/api/cups{id:/?\d*}{join_space:/?\w*}', cups_GET, 'cups_GET'),

    ('GET', r'/api/matches{id:/?\d*}', matches_GET, 'matches_GET'),

    ('GET', r'/api/players{id:/?\d*}', players_GET, 'players_GET'),
    ('POST', '/api/players', players_POST, 'players_POST'),
]