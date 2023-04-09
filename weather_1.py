import aiohttp
import asyncio
import time
from datetime import datetime


api_url1 = 'https://api.open-meteo.com/v1/forecast?latitude=50.4333&longitude=30.5167&current_weather=true'
api_url2 = 'https://goweather.herokuapp.com/weather/Kiev'
api_url3 = "https://wttr.in/kyiv?format=j1"


async def weather_data1():
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url1) as response:
            data = await response.json()
            temperature = data['current_weather']['temperature']
            return temperature


async def weather_data2():
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url2) as response:
            data = await response.json()
            temperature = data['temperature'][1:3]
            return float(temperature)


async def weather_data3():
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url3) as response:
            data = await response.json()
            temperature = data["current_condition"][0]['temp_C']
            return float(temperature)


async def main():
    temperatures = await asyncio.gather(weather_data1(), weather_data2(), weather_data3())
    print(f"Температура в Киеве ({datetime.now().strftime('%Y-%m-%d %H:%M')}): {round(sum(temperatures)/3, 1)}°C")


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")