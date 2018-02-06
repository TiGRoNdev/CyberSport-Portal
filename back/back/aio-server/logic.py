from fillDB import fill


async def home():
    await fill()
    text = 'Successfully filled DB'
    return text




