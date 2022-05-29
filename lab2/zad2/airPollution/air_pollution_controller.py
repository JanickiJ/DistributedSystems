from flask import Blueprint, render_template

from airPollution.air_pollution_sevice import AirPollutionService

air_pollution_controller = Blueprint('air_pollution_controller', __name__, template_folder='templates')
air_pollution_server = AirPollutionService()


@air_pollution_controller.route('/api/v1/town_info/air_pollution/<town_name>')
def get_air_pollution_for_specified_town(town_name):
    measurements = air_pollution_server.get_air_pollution_from_town(town_name).items()
    if not measurements:
        return f"Couldn't find measurements for: {town_name}", 400
    else:
        response = "".join([str((k, v)) for k, v in measurements])
        result = render_template('airPollution.html', townName=town_name, data=response)
        return result, 200, {'Content-Type': 'text/html'}
