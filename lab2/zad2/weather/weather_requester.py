import unicodedata

import requests as requests
from unidecode import unidecode

from config import Config as config
from weather.weather_dto import WeatherDto


class WeatherRequester:
    def __init__(self):
        self.base = config.WEATHER_REQUESTER_BASE

    def request_with_town_name(self, town_name):
        request = requests.get(url=self.base.__add__(unidecode(str.lower(town_name))))
        if request.status_code != 200:
            measurement = None
        else:
            measurement = WeatherDto(request.json())
        return measurement
