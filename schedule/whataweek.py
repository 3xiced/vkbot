import re

from bs4 import BeautifulSoup

from utils.aiohttp_requests import aiohttp_fetch
# Закомментировать для локального тестирования

""" import os
import sys
sys.path.append(os.path.abspath('../utils'))
from aiohttp_requests import aiohttp_fetch """
# Раскоментить для локального тестирования


async def get_week() -> str:
    try:
        response = await aiohttp_fetch("http://week.kodan.ru/")
        soup = BeautifulSoup(response, 'lxml')
        return (((re.sub("^\s+|\n|\r|\s+$", '', str(soup.find_all("span", {"class": "week-type"}))).replace('[<span class="week-type">', '')).replace("</span>]", "")).replace('	', '')).lower()
    except:
        return 'Ошибка в чётности недели #1'