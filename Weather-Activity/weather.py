import requests
from dotenv import load_dotenv
import os 
from activities import get_activities

load_dotenv()
api_key = os.getenv('API_KEY')


def get_lat_long(city_name, state_code, country_code, API_KEY):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}').json()
    if response:  # Check if the response is not empty
        location = response[0]  # Take the first location object
        lat, lon = location.get('lat'), location.get('lon')
        return lat, lon


def current_weather(lat, lon, API_KEY):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric')
    data = response.json()
    print(data)
    if 'weather' in data and len(data['weather']) > 0:
        weather_info = data['weather'][0]
        description = weather_info['description']
        temperature = round(data["main"]["temp"])
        Name = data['name']
        return [description,temperature,Name]
    


def main(city_name,state_name,country_name,api_key):
    lat,lon = get_lat_long(city_name,state_name,country_name,api_key)
    weather_data = current_weather(lat,lon,api_key)
    return weather_data


def activity(temperature,description, num_activities=4):
    return get_activities(temperature,description,num_activities=4)
    
#current_weather(52.2297,21.0122,api_key)