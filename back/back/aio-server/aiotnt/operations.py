from aiotnt.connectors import get_db_connector


async def count(space):
    connector = await get_db_connector(space)
    val = await connector.call('mod_len', [space])
    await connector.disconnect()
    return val.body[0]


async def get_all(space):
    connector = await get_db_connector(space)
    values = await connector.select(space, index='primary')
    await connector.disconnect()
    return values.body


async def add_game(name, description, logo='/static/img/logo/game/default.png'):
    connector = await get_db_connector('game')
    await connector.call('mod_insert', ['game', [
        name,
        logo,
        description
    ]])
    await connector.disconnect()


async def add_player(name, description, id_game, id_team=[], logo='/static/img/logo/player/default.png'):
    connector = await get_db_connector('player')
    await connector.call('mod_insert', ['player', [
        name,
        description,
        logo,
        0,
        id_game,
        id_team
    ]])
    await connector.disconnect()


async def add_team(name, description, id_game, logo='/static/img/logo/team/default.png'):
    connector = await get_db_connector('team')
    await connector.call('mod_insert', ['team', [
        name,
        description,
        logo,
        0,
        id_game
    ]])
    await connector.disconnect()


async def add_team_match(id_team, id_match, added=[], deleted=[]):
    connector = await get_db_connector('team_match')
    await connector.call('mod_insert', ['team_match', [
        id_team,
        added,
        deleted,
        id_match
    ]])
    await connector.disconnect()


async def add_cup(name, description, id_game, logo='/static/img/logo/cup/default.png'):
    connector = await get_db_connector('cup')
    await connector.call('mod_insert', ['cup', [
        name,
        logo,
        description,
        0,
        id_game,
    ]])
    await connector.disconnect()


async def add_stage(type, start, end, description, id_cup):  # Start & end are
                                                             # DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
    connector = await get_db_connector('stage')
    await connector.call('mod_insert', ['stage', [
        type,
        start,
        end,
        description,
        id_cup,
    ]])
    await connector.disconnect()


async def add_match(start, status, name, description, id_stage, logo='/static/img/logo/cup/default.png', uri_video=''):
    # Start & end are
    # DATETIME array [DAY, MONTH, YEAR, HOUR, MINUTE]
    connector = await get_db_connector('match')
    await connector.call('mod_insert', ['match', [
        start,
        status,
        name,
        description,
        logo,
        uri_video,
        id_stage
    ]])
    await connector.disconnect()
