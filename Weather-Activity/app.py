from flask import Flask, render_template, request
from weather import *
from activities import *
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
api_key = os.getenv('API_KEY')

def extract_city_name(weather_data):
    if 'name' in weather_data:
        return weather_data['name']
    else:
        return None

@app.route('/', methods=['GET','POST'])
def index():
    data = None
    if request.method == 'POST':
        city_name = request.form['cityName']
        state_name = request.form['stateName']
        country_name = request.form['countryName']
        lat,lon = get_lat_long(city_name,state_name,country_name,api_key)
        description, temperature, Name = current_weather(lat, lon, api_key)
        activities = get_activities(temperature, description,num_activities=4)
        return render_template('index.html', city=city_name, state=state_name, country=country_name, lat=lat, lon=lon, description=description, temperature=temperature, city_name=city_name, activities=activities)
    # return render_template('index.html', city=None, state=None, country=None, lat=None, lon=None, description=None, temperature=None)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
