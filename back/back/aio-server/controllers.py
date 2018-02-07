import aiohttp_jinja2
from logic import home, filltnt


@aiohttp_jinja2.template('index.html')
async def index(request):
    text = await home()
    return {'title': 'aio-server',
            'text': str(text),
            'app': request.app}


@aiohttp_jinja2.template('index.html')
async def filldb(request):
    text = await filltnt()
    return {'title': 'Tarantool-DB',
            'text': str(text),
            'app': request.app}


async def game(request):
    pass


async def team(request):
    pass


async def match(request):
    pass


async def player(request):
    pass


async def cup(request):
    pass


async def top_cup(request):
    pass


async def top_player(request):
    pass
