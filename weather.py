import asyncio
import time

import aiohttp

api_key = '0132c883f67b09bd955b2a063dd6f985'
city = 'Kiev'
api_url1 = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
api_url2 = 'http://api.weatherstack.com/current?access_key=4670cd98cb8ece0c2af1cd5f988db249&query=Kiev'
api_url3 = "https://api.oceandrivers.com:443/v1.0/getWeatherDisplay/kiev/?period=latestdata"


async def weather_data_owt():
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url1) as response:
            data = await response.json()
            temperature = data['main']['temp']
            return temperature


async def weather_data_ws():
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url2) as response:
            data = await response.json()
            temperature = data['current']['temperature']
            return temperature


async def weather_data_7t():
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url3) as response:
            data = await response.json()
            temperature = data["TEMPERATURE"]
            return temperature


async def main():
    temperatures = await asyncio.gather(weather_data_owt(), weather_data_7t(), weather_data_ws())
    print(f"Температура в Киеве: {sum(temperatures)/3}")
    print(temperatures)




if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")