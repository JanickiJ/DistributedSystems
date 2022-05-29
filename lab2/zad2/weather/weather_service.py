from weather.weather_requester import WeatherRequester


class WeatherService:
    def __init__(self):
        self.weather_requester = WeatherRequester()

    def get_weather_from_town(self, town_name):
        return self.weather_requester.request_with_town_name(town_name)
