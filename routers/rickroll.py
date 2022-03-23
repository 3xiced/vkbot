import keyboards.menu_kb as menu_kb

from utils.sqlite_requests import database_handler

from vkwave.bots import simple_bot_message_handler, DefaultRouter, SimpleBotEvent, PayloadFilter


geobot_router = DefaultRouter()


@simple_bot_message_handler(geobot_router, PayloadFilter({"button": "donate"}))
@database_handler()
async def miamor(event: SimpleBotEvent) -> str:
    await event.answer(message='Сколько не жалко <3\nhttps://www.tinkoff.ru/cf/67hbUB2jUpf', keyboard=menu_kb.START_KB.get_keyboard())