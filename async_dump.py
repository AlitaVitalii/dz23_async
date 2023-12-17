import os
import re
import time

import aiohttp
import asyncio

import requests
import json
# import datetime
# from aiofile import async_open
# from urllib.parse import urljoin
# from bs4 import BeautifulSoup
# from itertools import chain

import environ


env = environ.Env

api_key = env('S_KEY')
city = 'Kyiv'
url_owt = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'




async def openweathermap(session):
    async with session.get(url_owt) as response:
        assert response.status == 200
        weather_data = json.loads(response.text)
        # Extract weather data
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        # Print weather data
        print(f'Temperature in Kyiv: {temperature}°C')
        print(f'Weather description: {description}')


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(openweathermap(session))




if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")
