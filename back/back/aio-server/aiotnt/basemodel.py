from aiotnt.operations import *


class Model:
    def __init__(self):
        self.space = ''

    async def get_object_by_id(self, id):
        response = await get_obj_by_id(self.space, id)
        return response

    async def add_object(self, *args):
        return await add_obj(self.space, args)



