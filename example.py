import requests
import json

#
# # Replace YOUR_API_KEY with your actual API key from OpenWeatherMap
# # api_key = 'YOUR_API_KEY'
# # city = 'Kyiv'
# # url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
#
# api_key = '0132c883f67b09bd955b2a063dd6f985'
# city = 'Kyiv'
# url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
#
#
# response = requests.get(url)
# weather_data = json.loads(response.text)
# # Extract weather data
# temperature = weather_data['main']['temp']
# description = weather_data['weather'][0]['description']
#
# # Print weather data
# print(f'Temperature in Kyiv: {temperature}°C')
# print(f'Weather description: {description}')
#
#
# # api_key_2 = '4670cd98cb8ece0c2af1cd5f988db249'
# url = f'http://api.weatherstack.com/current?access_key=4670cd98cb8ece0c2af1cd5f988db249&query=Kiev'
#
# response2 = requests.get(url)
# weather_data2 = json.loads(response2.text)
# temperature2 = weather_data2['current']['temperature']
# print(f'Temperature in Kyiv: {temperature2}°C')
#
#
# url3 = "http://www.7timer.info/bin/api.pl?lon=30.5167&lat=50.4333&product=astro&output=json"
#
#
# response3 = requests.get(url3)
# weather_data3 = json.loads(response3.text)
# temperature3 = weather_data3["dataseries"][0]['temp2m']
# print(f'Temperature in Kyiv: {temperature3}°C')


url3 = "https://api.oceandrivers.com:443/v1.0/getWeatherDisplay/kiev/?period=latestdata"


response3 = requests.get(url3)
weather_data3 = json.loads(response3.text)
temperature3 = weather_data3["TEMPERATURE"]
print(f'Temperature in Kyiv: {temperature3}°C')
