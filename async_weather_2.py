import asyncio
import aiohttp

async def fetch_weather_data(api_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            data = await response.json()
            return data

async def get_temperature(api_url):
    try:
        data = await fetch_weather_data(api_url)
        temperature = data['current']['temperature']
        return temperature
    except Exception as e:
        print(f'Error getting temperature from {api_url}: {e}')
        return None

async def get_average_temperature(city, date):
    # List of weather API URLs
    api_urls = [
        f'http://api.weatherapi.com/v1/forecast.json?key=YOUR_API_KEY1&q={city}&date={date}',
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=0132c883f67b09bd955b2a063dd6f985&units=metric',
        f'http://api.weatherstack.com/current?access_key=4670cd98cb8ece0c2af1cd5f988db249f&query={city}'
    ]

    tasks = [get_temperature(api_url) for api_url in api_urls]
    temperatures = await asyncio.gather(*tasks)

    # Remove None values from temperatures list
    temperatures = [temp for temp in temperatures if temp is not None]

    if len(temperatures) > 0:
        average_temperature = sum(temperatures) / len(temperatures)
        print(f'Average temperature in {city} for {date}: {average_temperature}°C')
    else:
        print('Failed to get temperature from any API.')

async def main():
    city = 'Kiev'
    date = '2023-04-10'
    await get_average_temperature(city, date)

asyncio.run(main())
