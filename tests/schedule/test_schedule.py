import asyncio
import pytest


from schedule import sheethandler


@pytest.mark.asyncio  # Общий тест для всех групп на сегодня или завтра, на просто вывод
@pytest.mark.parametrize('day, group, week_type, excepted',
                         [('завтра', 'бвт2101', 'текущая неделя', 'None'),
                          ('завтра', 'бвт2102', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2103', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2104', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2105', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2106', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2107', 'текущая неделя', 'None'),
                             ('завтра', 'бвт2108', 'текущая неделя', 'None'),
                             ('завтра', 'бфи2101', 'текущая неделя', 'None'),
                             ('завтра', 'бфи2102', 'текущая неделя', 'None'),
                             ('завтра', 'бст2101', 'текущая неделя', 'None'),
                             ('завтра', 'бст2102', 'текущая неделя', 'None'),
                             ('завтра', 'бст2103', 'текущая неделя', 'None'),
                             ('завтра', 'бст2104', 'текущая неделя', 'None'),
                             ('завтра', 'бст2105', 'текущая неделя', 'None'),
                             ('завтра', 'бст2106', 'текущая неделя', 'None'),
                             ('завтра', 'бэи2101', 'текущая неделя', 'None'),
                             ('завтра', 'бэи2102', 'текущая неделя', 'None'),
                             ('завтра', 'бэи2103', 'текущая неделя', 'None'),#
                             ('завтра', 'биб2101', 'текущая неделя', 'None'),
                             ('завтра', 'биб2102', 'текущая неделя', 'None'),
                             ('завтра', 'биб2103', 'текущая неделя', 'None'),
                             ('завтра', 'биб2104', 'текущая неделя', 'None'),
                             ('завтра', 'бин2101', 'текущая неделя', 'None'),
                             ('завтра', 'бин2102', 'текущая неделя', 'None'),
                             ('завтра', 'бин2103', 'текущая неделя', 'None'),
                             ('завтра', 'бин2104', 'текущая неделя', 'None'),
                             ('завтра', 'бин2105', 'текущая неделя', 'None'),
                             ('завтра', 'бин2106', 'текущая неделя', 'None'),
                             ('завтра', 'бин2107', 'текущая неделя', 'None'),
                             ('завтра', 'бин2108', 'текущая неделя', 'None'),
                             ('завтра', 'бин2109', 'текущая неделя', 'None'),
                             ('завтра', 'бин2110', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2101', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2102', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2103', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2104', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2105', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2106', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2107', 'текущая неделя', 'None'),
                             ('сегодня', 'бвт2108', 'текущая неделя', 'None'),
                             ('сегодня', 'бфи2101', 'текущая неделя', 'None'),
                             ('сегодня', 'бфи2102', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2101', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2102', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2103', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2104', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2105', 'текущая неделя', 'None'),
                             ('сегодня', 'бст2106', 'текущая неделя', 'None'),
                             ('сегодня', 'бэи2101', 'текущая неделя', 'None'),
                             ('сегодня', 'бэи2102', 'текущая неделя', 'None'),
                             ('сегодня', 'бэи2103', 'текущая неделя', 'None'),
                             ('сегодня', 'биб2101', 'текущая неделя', 'None'),
                             ('сегодня', 'биб2102', 'текущая неделя', 'None'),
                             ('сегодня', 'биб2103', 'текущая неделя', 'None'),
                             ('сегодня', 'биб2104', 'текущая неделя', 'None'),
                             ('сегодня', 'бин2101', 'текущая неделя', 'None'),
                             ('сегодня', 'бин2102', 'текущая неделя', 'None'),
                             ('сегодня', 'бин2103', 'текущая неделя', 'None'),
                             ('сегодня', 'бин2104', 'текущая неделя', 'None'),
                             ('сегодня', 'бин2105', 'текущая неделя', 'None'),
                             ('сегодня', 'бин2106', 'текущая неделя', 'None'),
                             ('сегодня', 'бин2107', 'текущая неделя', 'None'),
                             ('сегодня', 'бин2108', 'текущая неделя', 'None'),
                             ('сегодня', 'бин2109', 'текущая неделя', 'None'),
                             ('сегодня', 'бин2110', 'текущая неделя', 'None')])
async def test_schedule(day, group, week_type, excepted):
    assert excepted not in await sheethandler.print_schedule(day, group, '123', week_type)


@pytest.mark.asyncio  # Тест на количество пар, проверяю через количество разделений пар,
# так как их энивей больше 7 быть не может(не должно)
@pytest.mark.parametrize('day, group, week_type, excepted',
                         [('завтра', 'бвт2101', 'текущая неделя', '7'),
                          ('завтра', 'бвт2102', 'текущая неделя', '7'),
                             ('завтра', 'бвт2103', 'текущая неделя', '7'),
                             ('завтра', 'бвт2104', 'текущая неделя', '7'),
                             ('завтра', 'бвт2105', 'текущая неделя', '7'),
                             ('завтра', 'бвт2106', 'текущая неделя', '7'),
                             ('завтра', 'бвт2107', 'текущая неделя', '7'),
                             ('завтра', 'бвт2108', 'текущая неделя', '7'),
                             ('завтра', 'бфи2101', 'текущая неделя', '7'),
                             ('завтра', 'бфи2102', 'текущая неделя', '7'),
                             ('завтра', 'бст2101', 'текущая неделя', '7'),
                             ('завтра', 'бст2102', 'текущая неделя', '7'),
                             ('завтра', 'бст2103', 'текущая неделя', '7'),
                             ('завтра', 'бст2104', 'текущая неделя', '7'),
                             ('завтра', 'бст2105', 'текущая неделя', '7'),
                             ('завтра', 'бст2106', 'текущая неделя', '7'),
                             ('завтра', 'бэи2101', 'текущая неделя', '7'),
                             ('завтра', 'бэи2102', 'текущая неделя', '7'),
                             ('завтра', 'бэи2103', 'текущая неделя', '7'),
                             ('завтра', 'биб2101', 'текущая неделя', '7'),
                             ('завтра', 'биб2102', 'текущая неделя', '7'),
                             ('завтра', 'биб2103', 'текущая неделя', '7'),
                             ('завтра', 'биб2104', 'текущая неделя', '7'),
                             ('завтра', 'бин2101', 'текущая неделя', '7'),
                             ('завтра', 'бин2102', 'текущая неделя', '7'),
                             ('завтра', 'бин2103', 'текущая неделя', '7'),
                             ('завтра', 'бин2104', 'текущая неделя', '7'),
                             ('завтра', 'бин2105', 'текущая неделя', '7'),
                             ('завтра', 'бин2106', 'текущая неделя', '7'),
                             ('завтра', 'бин2107', 'текущая неделя', '7'),
                             ('завтра', 'бин2108', 'текущая неделя', '7'),
                             ('завтра', 'бин2109', 'текущая неделя', '7'),
                             ('завтра', 'бин2110', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2101', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2102', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2103', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2104', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2105', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2106', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2107', 'текущая неделя', '7'),
                             ('сегодня', 'бвт2108', 'текущая неделя', '7'),
                             ('сегодня', 'бфи2101', 'текущая неделя', '7'),
                             ('сегодня', 'бфи2102', 'текущая неделя', '7'),
                             ('сегодня', 'бст2101', 'текущая неделя', '7'),
                             ('сегодня', 'бст2102', 'текущая неделя', '7'),
                             ('сегодня', 'бст2103', 'текущая неделя', '7'),
                             ('сегодня', 'бст2104', 'текущая неделя', '7'),
                             ('сегодня', 'бст2105', 'текущая неделя', '7'),
                             ('сегодня', 'бст2106', 'текущая неделя', '7'),
                             ('сегодня', 'бэи2101', 'текущая неделя', '7'),
                             ('сегодня', 'бэи2102', 'текущая неделя', '7'),
                             ('сегодня', 'бэи2103', 'текущая неделя', '7'),
                             ('сегодня', 'биб2101', 'текущая неделя', '7'),
                             ('сегодня', 'биб2102', 'текущая неделя', '7'),
                             ('сегодня', 'биб2103', 'текущая неделя', '7'),
                             ('сегодня', 'биб2104', 'текущая неделя', '7'),
                             ('сегодня', 'бин2101', 'текущая неделя', '7'),
                             ('сегодня', 'бин2102', 'текущая неделя', '7'),
                             ('сегодня', 'бин2103', 'текущая неделя', '7'),
                             ('сегодня', 'бин2104', 'текущая неделя', '7'),
                             ('сегодня', 'бин2105', 'текущая неделя', '7'),
                             ('сегодня', 'бин2106', 'текущая неделя', '7'),
                             ('сегодня', 'бин2107', 'текущая неделя', '7'),
                             ('сегодня', 'бин2108', 'текущая неделя', '7'),
                             ('сегодня', 'бин2109', 'текущая неделя', '7'),
                             ('сегодня', 'бин2110', 'текущая неделя', '7'),])
async def test_count_pars_schedule(day, group, week_type, excepted):
    response = await sheethandler.print_schedule(day, group, '123', week_type)
    count_pars = response.count('⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻\n')
    assert count_pars <= int(excepted)


@pytest.mark.asyncio  # Тест, что выводит все дни недели и не выводит лишних, а также правильно дни недели выводит и не выводит пустых ячеек
@pytest.mark.parametrize('day, group, week_type, excepted',
                         [('вся неделя', 'бвт2101', 'текущая неделя', ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                          ('вся неделя', 'бвт2102', 'текущая неделя',
                           ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2103', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2104', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2105', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2106', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2107', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2108', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бфи2101', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бфи2102', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2101', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2102', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2103', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2104', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2105', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2106', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                          ('вся неделя', 'бэи2101', 'текущая неделя',
                           ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бэи2102', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бэи2103', 'текущая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2101', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2102', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2103', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2104', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2105', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2106', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2107', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бвт2108', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бфи2101', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бфи2102', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2101', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2102', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2103', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2104', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2105', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бст2106', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бэи2101', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бэи2102', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бэи2103', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                              ('вся неделя', 'биб2101', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'биб2102', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'биб2103', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'биб2104', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                              ('вся неделя', 'бин2101', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бин2102', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бин2103', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бин2104', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бин2105', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бин2106', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                              ('вся неделя', 'бин2107', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бин2108', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бин2109', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None']),
                             ('вся неделя', 'бин2110', 'следующая неделя',
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'None'])])
async def test_full_schedule(day, group, week_type, excepted):
    response = await sheethandler.print_schedule(day, group, '123', week_type)
    assert (excepted[0] in response[1]
            and excepted[1] in response[2]
            and excepted[2] in response[3]
            and excepted[3] in response[4]
            and excepted[4] in response[5]
            and excepted[5] in response[6]
            and excepted[6] not in response[1]
            and excepted[6] not in response[2]
            and excepted[6] not in response[3]
            and excepted[6] not in response[4]
            and excepted[6] not in response[5]
            and excepted[6] not in response[6])
