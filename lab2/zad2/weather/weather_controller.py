from flask import Blueprint, render_template

from weather.weather_service import WeatherService

weather_controller = Blueprint('weather_controller', __name__, template_folder='templates')
weather_service = WeatherService()


@weather_controller.route('/api/v1/town_info/weather/<town_name>')
def get_weather_for_specified_town(town_name):
    data = weather_service.get_weather_from_town(town_name)
    if not data:
        return f"There is no weather station in {town_name}", 400
    else:
        result = render_template('weather.html', townName=town_name, **data.parameters_dict(),
                                 result="There is weather station")
        return result, 200, {'Content-Type': 'text/html'}
