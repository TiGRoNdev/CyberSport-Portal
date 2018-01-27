from aiohttp import web


async def index(request):
    return web.Response(text='Hello from Aiohttp! I am started on 127.0.1.0:8081')
