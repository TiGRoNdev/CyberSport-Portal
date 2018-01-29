#! /usr/bin/python3.6

import argparse
from aiohttp import web
from views import *

parser = argparse.ArgumentParser(description="aiohttp server example")
parser.add_argument('--path')
parser.add_argument('--port')


if __name__ == '__main__':
    app = web.Application()
    # configure app
    app.router.add_get('/', index)

    args = parser.parse_args()
    web.run_app(app, path=args.path, port=args.port)
