from vkwave.bots import Keyboard, ButtonColor
from bot.db import db_get_priority_button
from bot.utils import schedule_request as sr
from bot.utils import ScheduleRequest


async def create_menu_kb(user_id: int) -> Keyboard:
    '''Генерирует стартовую клавиатуру и устанавливает реквесты пользователя на стандарт'''
    sr.user_schedule_requests[user_id] = ScheduleRequest()

    button = await db_get_priority_button(user_id)

    MENU_BUTTONS: list = ['Расписание', 'Шаблоны расписания', 'Анекдот',
                          'Поддержать', 'Помощь', f'Приоритет расписания: {button}']
    MENU_BUTTONS_PAYLOAD: list = [{"menu_button": "schedule"}, {"menu_button": "config"}, {"menu_button": "joke"},
                                  {"menu_button": "donate"}, {"menu_button": "help"}, {"menu_button": "priority"}]
    MENU_KB: Keyboard = Keyboard(one_time=False)

    MENU_KB.add_text_button(text=MENU_BUTTONS[0],
                            color=ButtonColor.SECONDARY,
                            payload=MENU_BUTTONS_PAYLOAD[0])
    MENU_KB.add_text_button(text=MENU_BUTTONS[1],
                            color=ButtonColor.SECONDARY,
                            payload=MENU_BUTTONS_PAYLOAD[1])
    MENU_KB.add_row()
    MENU_KB.add_text_button(text=MENU_BUTTONS[2],
                            color=ButtonColor.SECONDARY,
                            payload=MENU_BUTTONS_PAYLOAD[2])
    MENU_KB.add_text_button(text=MENU_BUTTONS[3],
                            color=ButtonColor.SECONDARY,
                            payload=MENU_BUTTONS_PAYLOAD[3])
    MENU_KB.add_text_button(text=MENU_BUTTONS[4],
                            color=ButtonColor.SECONDARY,
                            payload=MENU_BUTTONS_PAYLOAD[4])
    MENU_KB.add_row()
    MENU_KB.add_text_button(text=MENU_BUTTONS[5],
                            color=ButtonColor.PRIMARY,
                            payload=MENU_BUTTONS_PAYLOAD[5])

    return MENU_KB
