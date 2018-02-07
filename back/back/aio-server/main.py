import argparse
import asyncio
import aiohttp_debugtoolbar
from aiohttp import web
from routes import routes
from settings import DEBUG, HOST, PORT

parser = argparse.ArgumentParser(description="aiohttp server example")
parser.add_argument('--path')
parser.add_argument('--port')


async def init(loop):
    middle = []

    app = web.Application(loop=loop, middlewares=middle)

    if DEBUG:
        aiohttp_debugtoolbar.setup(app)

    # route part
    for route in routes:
        res = app.router.add_resource(route[1])
        res.add_route(route[0], route[2])

    return app

loop = asyncio.get_event_loop()
app = loop.run_until_complete(init(loop))

args = parser.parse_args()
# web.run_app(app, path=args.path, port=args.port)
web.run_app(app, host=HOST, port=PORT)
