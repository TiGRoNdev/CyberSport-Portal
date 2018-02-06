from models import Game


async def home():
    game = Game()
    text = ''
    text += str(await game.add_object('Dota2', '/static/img/logo/game/default.png', 'The best Online game ever')) + '\n'
    text += str(await game.add_object('CS:GO', '/static/img/logo/game/default.png', 'Online shooter')) + '\n'
    text += str(await game.add_object('PUBG', '/static/img/logo/game/default.png', 'Online new survival shooter')) + '\n'
    text += str(await game.get_object_by_id(7))
    return text




