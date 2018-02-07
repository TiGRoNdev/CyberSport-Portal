from fillDB import fill


async def filltnt():
    await fill()
    text = 'Successfully filled DB'
    return text


async def home():
    text = 'Hello! to filling DB open /filldb'
    return text

