import json
import random
import os


script_dir = os.path.dirname(__file__)

# Construct the full path to test.json
json_file_path = os.path.join(script_dir, 'test.json')


def get_activities(temperature, description, num_activities=4):
    
    with open(json_file_path) as file:
        activity_data = json.load(file)

# making conditions 
    conditions = [
            (3, 40, 'clear sky'),  
            (-10, 30, 'few clouds'),  
            (-4, 20, 'scattered clouds'),  
            (-5, 25, 'cloudy'),  
            (-5, 30, 'overcast clouds'),  
            (-5, 30, 'broken clouds'),
            (2, 30, 'light rain'),  
            (2, 30, 'moderate rain'),  
            (2, 30, 'heavy rain'),  
            (2, 25, 'showers'),  
            (1, 24, 'thunderstorm'), 
            (-10, 10, 'snow'), 
            (0, 25, 'fog'),  
            (0, 30, 'mist'),  
            (0, 42, 'haze'), 
        ]

    # checking if condition is available 
    available_descriptions = [] 
    for min_temp,max_temp,desc in conditions:
        if desc == description and min_temp <= temperature <= max_temp :
            available_descriptions = activity_data.get(f"{desc}", [])
            break


    if available_descriptions:
        random.shuffle(available_descriptions)
        return available_descriptions[:num_activities]

    return available_descriptions
