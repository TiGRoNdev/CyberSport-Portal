from aiotnt.operations import *
from aiotnt.basemodel import Model


class Game(Model):
    def __init__(self):
        self.space = 'game'

    async def add_object(self, name, logo, description):
        return await add_obj(self.space, name, logo, description)