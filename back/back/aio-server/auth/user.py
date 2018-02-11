from aiotnt.basemodel import Model
from aiotnt.operations import *
import bcrypt


class User(Model):
    def __init__(self):
        self.space = 'user'

    async def match_password(self, id, password):
        user = await get_obj_by_id(self.space, id)
        if user == '404':
            raise User.DoesNotExist
        if bcrypt.checkpw(password.encode("utf-8"), user['hash'].encode("utf-8")):
            return True
        raise User.PasswordDoesNotMatch

    async def add(self, email, password, is_admin=False, is_organizer=False, is_team=True):
        user = await search_by_index(self.space, 'email', 'EQ', email, 1)
        if len(user) != 0:
            raise User.EmailDoesExist
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), salt)
        return await add_obj(self.space, email, hashed_pw, salt, is_admin, is_organizer, is_team)

    class DoesNotExist(BaseException):
        pass

    class PasswordDoesNotMatch(BaseException):
        pass

    class EmailDoesExist(BaseException):
        pass