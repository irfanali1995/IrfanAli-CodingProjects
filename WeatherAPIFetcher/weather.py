import requests 

API_KEY = "b652a6be0b0cd5688bfe210361a8b522"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

lat = input("Enter a latitude of city: ")
lon = input("Enter a longitude of city: ")
request_url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
    
else:
    print("Error Occured")
 

# 40.7128, 74.0060 
