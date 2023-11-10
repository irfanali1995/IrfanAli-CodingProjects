import json 
import random

def get_activities(temperature, description,num_activities=4):
    with open('activities.json') as file:
        activity_data = json.load(file)
    if temperature >= 10:
        available_descriptions = activity_data['cloudy']
    else:
        return []  # If no descriptions are available for the temperature condition, return an empty list

    activity_list = available_descriptions

    if activity_list:
        random.shuffle(activity_list)
    return activity_list[:num_activities]
