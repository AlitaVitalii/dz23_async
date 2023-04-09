import asyncio
import aiohttp
import time
from datetime import datetime


api_urls = [
    'https://api.open-meteo.com/v1/forecast?latitude=50.4333&longitude=30.5167&current_weather=true',
    'https://goweather.herokuapp.com/weather/Kiev',
    "https://wttr.in/kyiv?format=j1"
]


async def weather_data(url: str, session: aiohttp.ClientSession):
    async with session.get(url) as response:
        data = await response.json()
        return data


async def main():
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*(weather_data(url, session) for url in api_urls))
        temperatures = [
            responses[0]['current_weather']['temperature'],
            float(responses[1]['temperature'][1:3]),
            float(responses[2]["current_condition"][0]['temp_C'])
        ]

        print(f"Температура в Киеве ({datetime.now().strftime('%Y-%m-%d %H:%M')}): {round(sum(temperatures)/3, 1)}°C")


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")
