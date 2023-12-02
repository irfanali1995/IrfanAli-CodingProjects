import requests



API_KEY = 'b652a6be0b0cd5688bfe210361a8b522'
api_key = API_KEY 

def get_lat_long(city_name, state_code, country_code, API_KEY):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}').json()
    lat, lon = response[0].get('lat'), response[0].get('lon')
    return lat, lon

def current_weather(lat, lon, API_KEY):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric')
    data = response.json()
    print(data)

    if 'weather' in data and len(data['weather']) > 0:
        weather_info = data['weather'][0]
        temperature = round(data["main"]["temp"])
        name = data["name"]
        print(name)
        return weather_info['description'], temperature,name
        '''return {
             'weather':weather_info['description'],
             'temperature': temperature
        }'''
    else:
        return {'weather': 'N/A', 'temperature': 'N/A'}

def main(city_name, state_name, country_name, api_key):
    lat, lon = get_lat_long(city_name, state_name, country_name, api_key)
    weather_data = current_weather(lat, lon, api_key)
    return weather_data

'''
description, temperature = current_weather(51.5073219, -0.1276474, api_key)
#51.5073219 -0.1276474
print("Description:", description)
print("Temperature:", temperature)
'''

'''#Example usage:
city_name = "London"
state_name = ""  # Leave it empty for London
country_name = "GB"
main(city_name, state_name, country_name, api_key)'''