from models import Game, Player, Team, Match, Stage, Cup
from datetime import datetime, timedelta


async def fill():
    text = ''
    cup = Cup()
    stage = Stage()
    match = Match()
    game = Game()
    player = Player()
    team = Team()

    idgame = []
    idcup = []
    idgame.append(await game.add('Dota2', "Dota 2 — компьютерная многопользовательская командная игра"
                                          " в жанре multiplayer online battle arena, разработанная Valve Corporation."
                                          " Является независимым продолжением карты-модификации DotA"
                                          " для игры Warcraft III."))
    idgame.append(await game.add('CS:GO', "Counter-Strike: Global Offensive — многопользовательская компьютерная игра,"
                                          " разработанная компаниями Valve и Hidden Path Entertainment."
                                          " Последняя основная игра в серии игр Counter-Strike; как и все игры серии"
                                          ", она посвящена противостоянию террористов и подразделений"
                                          " специального назначения."))
    idgame.append(await game.add('PUBG', 'PlayerUnknown’s Battlegrounds (сокр. PUBG) — '
                                         'многопользовательская онлайн-игра'
                                         ' в жанре королевской битвы, разрабатываемая и издаваемая студией'
                                         ' PUBG Corporation, дочерней компанией корейского издателя Bluehole. '
                                         'Официально дистрибьюцией игры на территории России занимается Mail.Ru Group.'
                                         ' Игра основана на предыдущих модификациях для других игр, созданных Бренданом'
                                         ' Грином (англ. Brendan Greene) под псевдонимом «PlayerUnknown», концепция'
                                         ' которых была вдохновлена японским фильмом «Королевская битва» 2000 года.'
                                         ' В итоге это привело к созданию самостоятельной игры, где Грин'
                                         ' выступил в качестве ведущего геймдизайнера. В игре до 100 игроков, которые'
                                         ' парашютируются на остров, после чего ищут снаряжение и оружие, чтобы убить'
                                         ' других участников и при этом самим остаться в живых. Доступная безопасная'
                                         ' зона на внутриигровой карте со временем начинает уменьшаться, '
                                         'делая доступное пространство более тесным, чтобы сталкивать их между'
                                         ' собой. Последний выживший игрок или команда побеждает в раунде.'))
    idcup.append(await cup.add('The International 2012', 'The International 2012 — второй турнир по игре Dota 2,'
                                                         ' проведённый компанией Valve, который был проведён в Сиэтле'
                                                         ' с 26 августа по 2 сентября 2012 года. Начальный призовой'
                                                         ' фонд составил 1 600 000 долларов США, дополнительных'
                                                         ' сборов в фонд не поступало. Для освещения турнира'
                                                         ' были приглашены известные комментаторы, которые в том'
                                                         ' числе проводили прямые видео трансляции '
                                                         '(через сервис Twitch.tv).', idgame[0]))
    idcup.append(await cup.add('The International 2013', 'The International 2013 — третий турнир The International'
                                                         ' по игре Dota 2, проведённый компанией Valve, который прошёл'
                                                         ' в Сиэтле с 3 по 12 августа 2013 года. Начальный призовой'
                                                         ' фонд составил 1 600 000 долларов США, а дополнительный сбор'
                                                         ' с билетов составил ещё 1 274 407 долларов США. Призовой фонд'
                                                         ', на момент 2013 года, оказался самым большим за всю историю'
                                                         ' киберспорта. Для освещения турнира были приглашены известные'
                                                         ' комментаторы, которые в том числе проводили прямые'
                                                         ' видеотрансляции (через сервис Twitch.tv).', idgame[0]))
    idcup.append(await cup.add('The International 2014', 'The International 2014 — четвёртый турнир The International'
                                                         ' по игре Dota 2, проведённый компанией Valve, который прошёл'
                                                         ' в Сиэтле с 18 по 21 июля 2014 года. Начальный призовой фонд'
                                                         ' составил 1 600 000 долларов США, а дополнительный сбор с '
                                                         'билетов составил ещё 9 324 024 долларов США. В отличие от '
                                                         'турниров прошлых лет International 2014 прошёл в середине'
                                                         ' июля, а не в августе, как раньше. Всего турнир посмотрели'
                                                         ' более 20 миллионов человек. Для освещения турнира были '
                                                         'приглашены известные комментаторы, которые в том числе '
                                                         'проводили прямые видео трансляции '
                                                         '(через сервис Twitch.tv).', idgame[0]))
    idcup.append(await cup.add('The International 2015', 'The International 2015 — пятый турнир The International'
                                                         ' по игре Dota 2, проводимый компанией Valve, который проходил'
                                                         ' в Сиэтле с 3 по 8 августа 2015 года. Начальный призовой фонд'
                                                         ' составил 1 600 000 долларов США, а дополнительный сбор с'
                                                         ' билетов составил ещё 16 816 970 долларов США. Для освещения'
                                                         ' турнира были приглашены известные комментаторы, которые в '
                                                         'том числе проводили прямые видео трансляции '
                                                         '(через сервис Twitch.tv).', idgame[0]))
    idcup.append(await cup.add('The International 2016', 'The International 2016 (англ. international — международный)'
                                                         ' — турнир по игре Dota 2, организованный компанией Valve,'
                                                         ' который прошёл в Сиэтле в августе 2016 года. Начальный '
                                                         'призовой фонд составил 1 600 000 долларов США, а '
                                                         'дополнительный сбор с билетов составил более 20 '
                                                         'миллионов долларов США. Ежегодный турнир проходил в шестой'
                                                         ' раз подряд, ввиду чего его название часто сокращалось до '
                                                         'аббревиатуры TI-6, и традиционно стал крупнейшим в '
                                                         'году соревнованием по Dota 2.', idgame[0]))
    idcup.append(await cup.add('The International 2017', 'The International 2017 (англ. international — международный)'
                                                         ' — турнир по игре Dota 2, организованный компанией Valve,'
                                                         ' который проходил в Сиэтле в августе 2017 года. Ежегодный '
                                                         'турнир состоялся в седьмой раз подряд и традиционно стал '
                                                         'крупнейшим в году соревнованием по Dota 2.'
                                                         'Участие в турнире приняли несколько приглашённых команд, а '
                                                         'также коллективы, победившие в международных квалификациях. '
                                                         'Отборочные турниры начались после окончания The Kiev Major: '
                                                         'открытые квалификации были назначены на 22—25 июня, а '
                                                         'региональные квалификации прошли 26—29 июня и определили '
                                                         'команды, которые поехали в Сиэтл для участия в финальной '
                                                         'части соревнования.'
                                                         'Призовой фонд турнира напрямую зависит от количества '
                                                         'проданных внутриигровых предметов. Четверть суммы, вырученной'
                                                         ' Valve от продажи так называемых «боевых пропусков», н'
                                                         'апрямую входит в призовой фонд. Сумма призовых превышает '
                                                         '$24 млн; так, годом ранее призовой фонд также '
                                                         'превышал $20 млн.'
                                                         'The International 2017 побил рекорд прошлого года и '
                                                         'официально стал крупнейшим киберспортивным турниром по '
                                                         'размеру призового фонда.', idgame[0]))
    idcup.append(await cup.add('joinDOTA season 2', 'Второй сезон турнира, который проводится по тому же принципу что и'
                                                    ' первый. Команды поделены на регионы: Америка, Европа, Азия, а '
                                                    'так же на несколько десятков дивизионов, от профессионалов до л'
                                                    'юбителей. Чемпионат продлится около 4 месяцев.', idgame[0]))
    idcup.append(await cup.add('joinDOTA season 5', 'Пятый сезон турнира, который проводится по тому же принципу что и'
                                                    ' первый. Команды поделены на регионы: Америка, Европа, Азия, а '
                                                    'так же на несколько десятков дивизионов, от профессионалов до л'
                                                    'юбителей. Чемпионат продлится около 4 месяцев.', idgame[0]))
    idcup.append(await cup.add('PREDATOR LEAGUE 2017', 'Get ready for all the thrills and chills from the biggest DOTA2'
                                                       ' tournament in Asia Pacific! At Asia Pacific Predator '
                                                       'League 2017, the best teams of each country will fight to '
                                                       'be the greatest e-sport team in Asia Pacific. The finals will '
                                                       'be held in Indonesia with a total prize pool of '
                                                       'USD 150,000.', idgame[0]))
    idcup.append(await cup.add('ESL PRO LEAGUE SEASON 6', '', idgame[1]))
    idcup.append(await cup.add('Legends Cup', '', idgame[1]))
    idcup.append(await cup.add('QIWI Team Play', '', idgame[1]))
    idcup.append(await cup.add('ELEAGUE Major 2017', '', idgame[1]))
    idcup.append(await cup.add('CIS XPUBG MASTER SERIES', '', idgame[2]))
    idcup.append(await cup.add('StarLadder 2017', '', idgame[2]))
    idcup.append(await cup.add('PUBG Resf Cup', '', idgame[2]))
    idcup.append(await cup.add('ROG City Battles', '', idgame[2]))
    for i in range(100):
        idcup.append(await cup.add('WESG 201{} CS:GO'.format(i), 'Один из крупнейших международных турниров по '
                                                           'CS:GO', idgame[1]))
        idcup.append(await cup.add('WESG 201{} DOTA 2'.format(i), 'Один из крупнейших международных турниров по '
                                                           'DOTA 2', idgame[0]))
        idcup.append(await cup.add('StarLadder 201{} DOTA 2'.format(i), 'Один из крупнейших международных турниров по '
                                                                 'DOTA 2', idgame[0]))
        idcup.append(await cup.add('StarLadder 201{} PUBG'.format(i), 'Один из крупнейших международных турниров по '
                                                                 'PUBG', idgame[2]))
        idcup.append(await cup.add('SurvivalRussian League 201{} PUBG'.format(i), 'Один из крупнейших российских'
                                                                             ' турниров по PUBG', idgame[2]))
        idcup.append(await cup.add('SurvivalRussian League 201{} DOTA 2'.format(i), 'Один из крупнейших российских'
                                                                             ' турниров по DOTA 2', idgame[0]))
        idcup.append(await cup.add('SurvivalRussian League 201{} CS:GO'.format(i), 'Один из крупнейших российских'
                                                                             ' турниров по CS:GO', idgame[1]))
    idteam = []
    for i in range(500):
        idteam.append(await team.add('Team{}_DOTA2'.format(i), 'We are playing Dota!', idgame[0]))
        idteam.append(await team.add('Team{}_CS:GO'.format(i), 'We are playing CS:GO!', idgame[1]))
        idteam.append(await team.add('Team{}_PUBG'.format(i), 'We are playing PUBG!', idgame[2]))

    for id in idteam:
        team1 = await team.get_by_id(id)
        for k in range(10):
            await player.add('Player_{}:{}_GAME-ID:{}'.format(id, k, team1['id_game']),
                             'The best player who id is {}'.format(id), team1['id_game'], id)

    for id in idcup:
        cup1 = await cup.get_by_id(id)
        game1 = await game.get_by_id(cup1['id_game'])
        start = datetime(2011, 2, 7, 12, 0)
        end = datetime(2011, 2, 17, 23, 0)
        typeS = [0, 1/8,  1/4, 1/2, 1]
        for tp in typeS:
            id_stage = await stage.add(tp, start, end, 'This is a {} stage of {}'.format(tp, cup1['name']), id)
            if tp == 0:
                for i in range(16):
                    delta = timedelta(hours=i*2)
                    await match.add(start + delta, 'SOON', 'MatchTEST_{}'.format(i), 'Match on {} stage of {} cup on {}'.format(
                        tp, cup1['name'], game1['name']
                    ), id_stage)
            else:
                for i in range(int(1/tp)):
                    await match.add(start, 'SOON', 'MatchTEST_{}'.format(i), 'Match on {} stage of {} cup on {}'.format(
                        tp, cup1['name'], game1['name']
                    ), id_stage)
            start += timedelta(days=12)
            end += timedelta(days=12)
        start += timedelta(days=200)
        end += timedelta(days=200)

    return text


# def rand_teamMatch_add():
    # while True:
        # team_id = randint(0, 99)
        # try:
            # players_ids = [i[0] for i in await player.search('id_team', 'EQ', idteam[team_id], lim=40)]
            # rand_deleted = [players_ids[randint(0, len(players_ids) - 1)] for i in range(2)]
            # rand_added = [randint(10, 450) for i in range(2)]
            # await teamMatch.add(idteam[team_id], idmatch, deleted=rand_deleted, added=rand_added)
        # except ValueError:
            # continue
        # else:
            # break
