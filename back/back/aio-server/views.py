from aiohttp import web


async def index(request):
	return web.Response(text='Hello from Aiohttp! I am working on BACK_1 server')
