import inspect
from typing import Iterable


class WeatherDto:
    def __init__(self, data):
        self.station_id = data['id_stacji']
        self.station = data['stacja']
        self.measurement_date = data['data_pomiaru']
        self.measurement_time = data['godzina_pomiaru']
        self.temperature = data['temperatura']
        self.wind_speed = data['predkosc_wiatru']
        self.wind_direction = data['kierunek_wiatru']
        self.humidity = data['wilgotnosc_wzgledna']
        self.rainfall = data['suma_opadu']
        self.pressure = data['cisnienie']

    def parameters_dict(self):
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        parameters_list = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
        return dict(parameters_list)
