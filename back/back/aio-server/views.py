import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'title': 'aio-server',
            'text': 'Hello from Aiohttp! I am working!',
            'app': request.app}

