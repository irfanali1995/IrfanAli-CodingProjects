import json

def get_activities(temperature, description,num_activities=4):
    with open('activities.json') as file:
        activity_data = json.load(file)
    if description == "clear sky" and temperature < 10:
        clear_sky_activities = activity_data.get("clear sky", [])
        print(clear_sky_activities)
result = get_activities(4,'clears sky', num_activities=4)
print(result)