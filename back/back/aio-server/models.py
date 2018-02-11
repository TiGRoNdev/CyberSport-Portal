from datetime import datetime
from aiotnt.operations import *
from aiotnt.basemodel import Model


class Game(Model):
    def __init__(self):
        self.space = 'game'

    async def add(self, name, description, logo='/static/img/logo/game/default.png'):
        if len(await search_by_index(self.space, 'name', 'EQ', name, 1)) != 0:
            raise ValueError("This game is only added")
        return await add_obj(self.space, name, logo, description)


class Player(Model):
    def __init__(self):
        self.space = 'player'

    async def add(self, name, description, id_game, id_team, logo='/static/img/logo/player/default.png'):
        if len(await search_by_index(self.space, 'name', 'EQ', name, 1)) != 0:
            raise ValueError("This player is only added")
        if await get_obj_by_id('game', id_game) == '404':
            raise ValueError('The game with this id_game does not exist')
        return await add_obj(self.space, name, description, logo, 0, id_game, id_team)


class Team(Model):
    def __init__(self):
        self.space = 'team'

    async def add(self, name, description, id_game, id_owner, logo='/static/img/logo/team/default.png'):
        if len(await search_by_index(self.space, 'name', 'EQ', name, 1)) != 0:
            raise ValueError("This team is only added")
        if await get_obj_by_id('game', id_game) == '404':
            raise ValueError('The game with this id_game does not exist')
        return await add_obj(self.space, name, description, logo, 0, id_game, id_owner)


class TeamMatch(Model):
    def __init__(self):
        self.space = 'team_match'

    async def add(self, id_team, id_match, added=[], deleted=[]):
        teams = await search_by_index(self.space, 'id_team', 'EQ', id_team, 10000)
        matches = [i[4] for i in await search_by_index(self.space, 'id_match', 'EQ', id_match, 2)]
        for team in teams:
            if team[4] in matches:
                raise ValueError("This match for this team is only added")
        return await add_obj(self.space, id_team, added, deleted, id_match)


class Cup(Model):
    def __init__(self):
        self.space = 'cup'

    async def add(self, name, description, id_game, id_owner, logo='/static/img/logo/cup/default.png'):
        if len(await search_by_index(self.space, 'name', 'EQ', name, 1)) != 0:
            raise ValueError("This cup is only added")
        if await get_obj_by_id('game', id_game) == '404':
            raise ValueError('The game with this id_game does not exist')
        return await add_obj(self.space, name, logo, description, 0, id_game, id_owner)


class Stage(Model):
    def __init__(self):
        self.space = 'stage'

    async def add(self, type_of_stage, start, end, description, id_cup):
        """
        :param type_of_stage: variants: [0 ... 1] 0- отбор, 1-финал; Минимальное значение 1/16
        :param start: datetime объект
        :param end: datetime
        :return: id этапа
        """
        if type_of_stage not in [0, 1/16, 1/8, 1/4, 1/2, 1]:
            raise ValueError('type_of_stage must be in range [0, 1/16, 1/8, 1/4, 1/2, 1]')
        if start >= end:
            raise ValueError('Start time >= End time')
        stages = await search_by_index(self.space, 'id_cup', 'EQ', id_cup, 6)
        res = [float(i[1]) for i in stages]
        if len(res) == 0:
            curr = -1
        else:
            curr = max(res)
        if type_of_stage <= curr:
            raise ValueError("This stage is low of added stages or it's stage is only added")
        for i in stages:
            ended = i[3]
            if start < datetime(ended[2], ended[1], ended[0], hour=ended[3], minute=ended[4]):
                raise ValueError("Start time must be highly then End time of previous Stage")
        starts = [start.day, start.month, start.year, start.hour, start.minute]
        ends = [end.day, end.month, end.year, end.hour, end.minute]
        return await add_obj(self.space, str(type_of_stage), starts, ends, description, id_cup)


class Match(Model):
    def __init__(self):
        self.space = 'match'

    async def add(self, start, status, name, description, id_stage, logo='/static/img/logo/cup/default.png', uri_video=''):
        """
        :param start: DATETIME object
        :param status: Must be LIVE or SOON or ENDED
        :param uri_video: URI of videofile or stream socket
        :return: id матча
        """
        stage = await get_obj_by_id('stage', id_stage)
        if stage == '404':
            raise ValueError("Stage with this id_stage does not exist")
        start_stage = datetime(stage['start'][2], stage['start'][1], stage['start'][0], hour=stage['start'][3], minute=stage['start'][4])
        end_stage = datetime(stage['end'][2], stage['end'][1], stage['end'][0], hour=stage['end'][3], minute=stage['end'][4])
        if start < start_stage or start > end_stage:
            raise ValueError("Start time of this match isn't in Stage time range")
        if stage['type'] != 0:
            count_of_exist_matches = len(await search_by_index(self.space, 'id_stage', 'EQ', id_stage, 20))
            if stage['type'] == 1 / 16:
                if count_of_exist_matches >= 16:
                    raise ValueError("Max count of matches on one stage")
            elif stage['type'] == 1 / 8:
                if count_of_exist_matches >= 8:
                    raise ValueError("Max count of matches on one stage")
            elif stage['type'] == 1 / 4:
                if count_of_exist_matches >= 4:
                    raise ValueError("Max count of matches on one stage")
            elif stage['type'] == 1 / 2:
                if count_of_exist_matches >= 2:
                    raise ValueError("Max count of matches on one stage")
            elif stage['type'] == 1:
                if count_of_exist_matches >= 1:
                    raise ValueError("Max count of matches on one stage")
        starts = [start.day, start.month, start.year, start.hour, start.minute]
        return await add_obj(self.space, starts, status, name, description, logo, uri_video, 0, id_stage)
