import os

from flask import Flask

from config import Config as config
from dialog.dialog_controller import dialog_controller
from weather.weather_controller import weather_controller
from youtube.youtube_controller import youtube_controller
from airPollution.air_pollution_controller import air_pollution_controller
from autoFill.auto_fill_controller import auto_fill_controller

app = Flask(__name__)
app.register_blueprint(weather_controller)
app.register_blueprint(youtube_controller)
app.register_blueprint(air_pollution_controller)
app.register_blueprint(dialog_controller)
app.register_blueprint(auto_fill_controller)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SERVER_NAME'] = config.SERVER_URL

if __name__ == '__main__':
    app.run(debug=True)
