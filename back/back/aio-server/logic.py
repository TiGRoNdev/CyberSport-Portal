from fillDB import fill
from models import *


async def filltnt():
    await fill()
    text = 'Successfully filled DB'
    return text


async def home():
    text = 'Hello! to filling DB open /filldb'
    return text


