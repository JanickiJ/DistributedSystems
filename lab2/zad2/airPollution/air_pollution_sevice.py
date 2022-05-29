import itertools
from statistics import mean

from airPollution.air_pollution_requester import AirPollutionRequester


class AirPollutionService:
    def __init__(self):
        self.air_pollution_requester = AirPollutionRequester()

    def get_air_pollution_from_town(self, town_name):
        all_stations = self.air_pollution_requester.get_all_stations()
        all_stations_in_town = [a for a in all_stations if str(a['stationName']).startswith(str(town_name))]
        all_stations_in_town = list(map(lambda x: x['id'], all_stations_in_town))
        sensors = self.air_pollution_requester.get_all_sensors(all_stations_in_town)
        sensors_id = []
        for sensor in list(itertools.chain(*sensors)):
            sensors_id.append(sensor['id'])

        measurements = self.air_pollution_requester.get_measurements(sensors_id)
        measurements_values = dict()
        for measure in measurements:
            measurement_value = measure['values'][0]['value'] if measure['values'][0]['value'] else \
                measure['values'][1]['value']
            if not measure['key'] in measurements_values:
                measurements_values[measure['key']] = [measurement_value]
            else:
                measurements_values[measure['key']].append(measurement_value)
        measurements_mean = dict()
        for k, v in measurements_values.items():
            v = [x for x in v if x]
            if v:
                measurements_mean[k] = round(mean(v), 2)
        return measurements_mean
