# importing required modules
import requests, json

# enter your API key from openweathermap.org here
api_key = 'Your API key goes here'

# base url to store url from api
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# input city name here
city_name = input('Enter city name: ')

# create complete url to be used for get request
complete_url = base_url + 'appid=' + api_key + '&q=' + city_name
response = requests.get(complete_url)
x = response.json()

# checking validity of city name
if x['cod'] != '404':
    # uses main object
    y = x['main']
    current_temperature = y['temp']
    current_pressure = y['pressure']
    current_humidity = y['humidity']

    # uses weather object
    z = x['weather']
    weather_description = z[0]['description']
    q = x['wind']
    wind_speed = q['speed']
    wind_direction = q['deg']
    k = x['clouds']
    cloudliness = k['all']

    # uses sys object to get sunrise/sunset data
    # uses main object to get sea and ground level data
    m = x['sys']
    sunrise = m['sunrise']
    sunset = m['sunset']
    sea_level = y['sea_level']
    ground_level = y['grnd_level']

    print(f'Temperature (in Kelvin) = {current_temperature}.'
          f'\nAtmospheric Pressure (in hPa) = {current_pressure}.'
          f'\nHumidity (in percentage) = {current_humidity}.'
          f'\nWind Speed (in m/s) = {wind_speed}.'
          f'\nWind Direction (in degrees) = {wind_direction}.'
          f'\nCloudliness (in percentage) = {cloudliness}.'
          f'\nWeather Description = {weather_description}.')

    # ask if they want to see sunrise and sunset times
    firstResponse = int(input('Would you like to know the sunrise and sunset times, ground level, and/or sea level? '
                              'Type 1 for sunrise/sunset, 2 for ground level, 3 for sea level, or 4 for all.'))

    if firstResponse == 1:
        print(f'Sunrise time is {sunrise}. Sunset time is {sunset}.')

    elif firstResponse == 2:
        print(f'Ground level is: {ground_level}.')

    elif firstResponse == 3:
        print(f'Sea level is: {sea_level}.')

    elif firstResponse == 4:
        print(f'Sunrise time is: {sunrise}.'
              f'\nSunset time is {sunset}.'
              f'\nGround level is: {ground_level}.'
              f'\nSea level is {sea_level}.')

    else:
        print('Input option not found!')

else:
    print('City Not Found')
