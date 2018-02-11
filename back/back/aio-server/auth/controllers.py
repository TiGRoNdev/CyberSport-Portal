import jwt
import json
from datetime import datetime, timedelta
from aiohttp import web
from auth.user import User
from settings import JWT_SECRET, JWT_EXP_DELTA_MINUTES, JWT_ALGORITHM


async def register(request):
    post_data = await request.json()
    try:
        email = post_data['email']
        pw = post_data['password']
        is_organizer = post_data['is_organizer']
        is_team = post_data['is_team']
    except KeyError:
        return web.Response(body=json.dumps({'message': 'Missing one of the required fields'}),
                            status=400,
                            content_type='application/json')
    user = User()
    try:
        await user.add(email, pw, is_organizer=is_organizer, is_team=is_team)
    except User.EmailDoesExist:
        return web.Response(body=json.dumps({'message': 'User with this e-mail does exist'}),
                            status=400,
                            content_type='application/json')
    return web.Response(body=json.dumps({'message': 'Registration successfully completed.'
                                                    ' To login open: /api/login with POST'}),
                        status=200,
                        content_type='application/json')


async def login(request):
    post_data = await request.json()
    try:
        email = post_data['email']
        pw = post_data['password']
    except KeyError:
        return web.Response(body=json.dumps({'message': 'Missing one of the required fields'}),
                            status=400,
                            content_type='application/json')
    user = User()
    try:
        found_users = await user.search('email', 'EQ', email, 1)
        user_id = found_users[0][0]
        await user.match_password(user_id, pw)
    except (User.DoesNotExist, User.PasswordDoesNotMatch, IndexError):
        return web.Response(body=json.dumps({'message': 'Wrong credentials'}),
                            status=400,
                            content_type='application/json')
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(minutes=JWT_EXP_DELTA_MINUTES)
    }
    jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return web.Response(body=json.dumps({'message': 'Your JWT will expire in {} minutes'.format(JWT_EXP_DELTA_MINUTES),
                                         'token': jwt_token.decode('utf-8')}),
                        status=200,
                        content_type='application/json')
