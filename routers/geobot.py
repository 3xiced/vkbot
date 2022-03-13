from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, PayloadFilter, DocUploader
from utils.sqlite_requests import sqlite_fetch
from keyboards.menu_kb import START_KB
from entry import settings
from datetime import datetime
import geobot


geobot_router = DefaultRouter()


@simple_bot_message_handler(geobot_router, PayloadFilter({"button": "miamor"}))
async def miamor(event: SimpleBotEvent) -> str:
    user = await event.get_user()
    sqlite_fetch(event, user)
    if str(event.from_id) in settings.GET_ALLOWED_USER_IDS():
        await event.answer(message='ACCESS GRANTED.', keyboard=START_KB.get_keyboard())
        await geobot.write_gpx(0, 5)
        gpx = await DocUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path="geobot/test.gpx", title=f"Route {datetime.now()}")
        await event.answer(message='Карта:', keyboard=START_KB.get_keyboard(), attachment=gpx)
    else:
        await event.answer(message='MI AMOR LA VINO!!! CASILLERO DEL DIABLO!!!!', keyboard=START_KB.get_keyboard())
