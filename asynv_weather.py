import asyncio
import aiohttp

async def fetch_weather(api_key, city, session):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    async with session.get(url) as response:
        data = await response.json()
        return data

async def get_weather_data():
    api_keys = ['0132c883f67b09bd955b2a063dd6f985']  # Replace with your actual API keys
    city = 'Kyiv'
    weather_data = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for api_key in api_keys:
            task = fetch_weather(api_key, city, session)
            tasks.append(task)

        # Use gather to make all requests concurrently
        responses = await asyncio.gather(*tasks)

        # Extract relevant data from each response
        for response in responses:
            temperature = response['main']['temp']
            weather_data.append(temperature)

    return weather_data


async def calculate_average_temperature():
    weather_data = await get_weather_data()
    average_temperature = sum(weather_data) / len(weather_data)
    return average_temperature

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    average_temperature = loop.run_until_complete(calculate_average_temperature())
    print(f'Average temperature: {average_temperature}°C')
