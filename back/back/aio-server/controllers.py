import aiohttp_jinja2
from models import *


@aiohttp_jinja2.template('index.html')
async def index(request):
    text = await home()
    return {'title': 'aio-server',
            'text': str(text),
            'app': request.app}
