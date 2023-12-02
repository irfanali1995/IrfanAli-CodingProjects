from flask import Flask, render_template, request
from weather import * 
from activities import *
from dotenv import load_dotenv
from synonyms import synonyms
import os

app = Flask(__name__)

API_KEY = 'b652a6be0b0cd5688bfe210361a8b522'
api_key = API_KEY 



@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city_name = request.form['cityName']
        country_name = request.form['countryName']
        state_name = request.form['stateName']
        try:
            lat, lon = get_lat_long(city_name, state_name, country_name, api_key)
            description, temperature, name= current_weather(lat, lon, api_key)
            lookup_description = synonyms.get(description, description)
            recommended_activities = get_activities(temperature, lookup_description)
            return render_template('index.html', city=city_name, state=state_name, country=country_name, lat=lat, lon=lon, description=description, temperature=temperature, name=name, recommended_activities=recommended_activities)
        except Exception as e:
             error_message = "An error occurred. Please check the city name and try again."
             return render_template('index.html', error=error_message)
        
    return render_template('index.html', city=None, state=None, country=None, lat=None, lon=None, description=None, temperature=None)

if __name__ == '__main__':
    app.run(debug=True)
