from flask import Blueprint, render_template, session, request, url_for, redirect

dialog_controller = Blueprint('dialog', __name__, template_folder='templates', static_folder='templates')


@dialog_controller.route('/api/v1/')
def root():
    return render_template("index.html"), 200, {'Content-Type': 'text/html'}


@dialog_controller.route('/api/v1/town_info/')
def submit_form():
    town_name = request.args.get('town_name')
    if not town_name:
        return root()
    else:
        auto_fill_link = "auto_fill/".__add__(town_name)
        air_pollution_link = "air_pollution/".__add__(town_name)
        weather_link = "weather/".__add__(town_name)
        youtube_link = "youtube/".__add__(town_name)
        result = render_template("townInformation.html",
                                 auto_fill_link=auto_fill_link,
                                 air_pollution_link=air_pollution_link,
                                 weather_link=weather_link,
                                 youtube_link=youtube_link,
                                 townName=town_name)
        return result, 200, {'Content-Type': 'text/html'}
