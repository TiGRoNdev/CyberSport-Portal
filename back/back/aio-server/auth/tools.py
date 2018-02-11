import jwt
import json
from aiohttp import web
from auth.user import User
from settings import JWT_ALGORITHM, JWT_SECRET


async def auth_middleware(app, handler):
    async def middleware(request):

        user = User()
        request.user = None
        jwt_token = request.headers.get('authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, JWT_SECRET,
                                     algorithms=[JWT_ALGORITHM])
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return web.Response(body=json.dumps({'message': 'Token is invalid, please Log In'}),
                                    status=400,
                                    content_type='application/json')

            tmp = await user.get_by_id(payload['user_id'])
            if tmp == '404':
                return web.Response(body=json.dumps({'message': 'User not found, please check Token'}),
                                    status=404,
                                    content_type='application/json')
            request.user = {'id': tmp['id'],
                            'is_admin': tmp['is_admin'],
                            'is_organizer': tmp['is_organizer'],
                            'is_team': tmp['is_team']}
        return await handler(request)
    return middleware


def login_required(func):
    async def wrapper(request):
        if not request.user:
            return web.Response(body=json.dumps({'message': 'Auth required, please Log In or Register'}),
                                status=403,
                                content_type='application/json')
        return await func(request)
    return wrapper
