import argparse
import asyncio
import aiohttp_debugtoolbar
import aiohttp_jinja2
import jinja2
from aiohttp import web
from routes import routes
from settings import *

parser = argparse.ArgumentParser(description="aiohttp server example")
parser.add_argument('--path')
parser.add_argument('--port')


async def init(loop):
    middle = []

    app = web.Application(loop=loop, middlewares=middle)

    if DEBUG:
        aiohttp_debugtoolbar.setup(app)

    # install jinja2 templates
    loader = jinja2.FileSystemLoader('templates')
    aiohttp_jinja2.setup(app, loader=loader)

    # route part
    for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])

    # db connect
    # app.client = ma.AsyncIOMotorClient(MONGO_HOST)
    # app.db = app.client[MONGO_DB_NAME]
    # end db connect

    return app

loop = asyncio.get_event_loop()
app = loop.run_until_complete(init(loop))

args = parser.parse_args()
# web.run_app(app, path=args.path, port=args.port)
web.run_app(app, host=HOST, port=PORT)
