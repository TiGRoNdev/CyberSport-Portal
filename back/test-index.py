#путь к библиотеке
sys.path.append( settings.root )
#путь к проекту
sys.path.append( os.path.dirname( __file__ ) )

import asyncio
from aiohttp import web

def test(request):
    return {'title': 'Hello' }

async def init(loop):
    app = web.Application( loop = loop )
    app.router.add_route('GET', '/', basic_handler, name='index')
    handler = app.make_handler()
    srv = await loop.create_server(handler, '127.0.0.1', 8080)
    return srv, handler

loop = asyncio.get_event_loop()
srv, handler = loop.run_until_complete(  init( loop )  )
try:  loop.run_forever()
except KeyboardInterrupt:  
          loop.run_until_complete(handler.finish_connections())
