from aiotnt.operations import get_obj_by_id, count, get_all, search_by_index


class Model:
    def __init__(self):
        self.space = ''

    async def get_by_id(self, id):
        return await get_obj_by_id(self.space, id)

    async def count(self):
        return await count(self.space)

    async def get_all(self):
        return await get_all(self.space)

    async def search(self, index, iter, value, lim):
        return await search_by_index(self.space, index, iter, value, lim)

