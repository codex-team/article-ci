from flask import Flask
import requests
from flask import request

from config import APP_ID

app = Flask(__name__)


def parse_weather(data):
    try:
        temp = data['main']['temp']
        return f'The temperature is: {float(temp)-273.15:.1f}°'

    except Exception as e:
        return f'Data error: {e}'


def get_weather(city):
    try:
        r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APP_ID}')
        if r.status_code != 200:
            return f'Invalid response code: {r.status_code}'
        else:
            return parse_weather(r.json())

    except Exception as e:
        return f'API error: {e}'


@app.route("/")
def weather():
    city = request.args.get('city', 'Sankt-Peterburg')
    return get_weather(city)


@app.route("/")
def index():
    return "Welcome! The service takes a date and gives corresponding day of the week"

if __name__ == "__main__":
    app.run()
