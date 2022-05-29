import itertools
from statistics import mean

import requests as requests

from config import Config as config


class AirPollutionRequester:
    def __init__(self):
        self.find_all_url = config.AIR_POLLUTION_FIND_ALL
        self.find_sensors_url = config.AIR_POLLUTION_SENSORS
        self.find_measurement_url = config.AIR_POLLUTION_MEASUREMENT

    def get_all_stations(self):
        return requests.get(url=self.find_all_url).json()

    def get_all_sensors(self, stations):
        sensors = []
        for id in stations:
            sensors.append(requests.get(url=self.find_sensors_url.__add__(str(id))).json())
        return sensors

    def get_measurements(self, sensors):
        measurements = []
        for id in sensors:
            measurements.append(requests.get(url=self.find_measurement_url.__add__(str(id))).json())
        return measurements

