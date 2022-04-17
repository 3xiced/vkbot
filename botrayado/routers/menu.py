import botrayado.keyboards.menu_kb as menu_kb
import botrayado.utils.constants as constants

from botrayado.database.db import database_handler
from botrayado.utils.constants import headmans_ids

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, TextFilter, PayloadFilter


menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router, TextFilter(["старт", "начать"], PayloadFilter({"button": "menu"})))
@database_handler(is_menu=True)
async def menu(event: SimpleBotEvent) -> str:
    if event.from_id in list(headmans_ids.keys()):
        constants.headman_requests[event.from_id] = constants.HeadmanRequest()
    await event.answer(message='Добро пожаловать в Bot Rayado\n\nЕсли у вас не отобразилась клавиатура, нажмите на кнопку' +
                       'слева от кнопки выбора эмодзи\n\n Наши преимущества:\n\n - Есть шаблоны для быстрого получения расписания\n' +
                       ' - Всегда новое расписание, полученное с сайта\n - Все потоки 1 курса\n - Быстрая работа бота\n - Регулярные обновления', keyboard=menu_kb.START_KB.get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(["меню", "расписание", ], PayloadFilter({"button": "menu"})))
@database_handler(is_menu=True)
async def menu(event: SimpleBotEvent) -> str:
    if event.from_id in list(headmans_ids.keys()):
        constants.headman_requests[event.from_id] = constants.HeadmanRequest()
    await event.answer(message='Выберите команду из списка.', keyboard=menu_kb.START_KB.get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(["привет", "добрый день", "здравствуй", "здравствуйте", "ку", "прив", "приффки", "дратути"]))
@database_handler()
async def hello(event: SimpleBotEvent) -> None:
    if event.from_id in list(headmans_ids.keys()):
        constants.headman_requests[event.from_id] = constants.HeadmanRequest()
    await event.answer(message='Здравствуйте', keyboard=menu_kb.START_KB.get_keyboard())


@simple_bot_message_handler(menu_router, TextFilter(["пока", "до свидания", "бб", "прощай", "до связи"]))
@database_handler()
async def goodbye(event: SimpleBotEvent) -> None:
    if event.from_id in list(headmans_ids.keys()):
        constants.headman_requests[event.from_id] = constants.HeadmanRequest()
    await event.answer(message='До свидания', keyboard=menu_kb.START_KB.get_keyboard())
