from autoFill.auto_fill_service import AutoFillService
from flask import Blueprint, render_template

auto_fill_controller = Blueprint('auto_fill_controller', __name__, template_folder='templates')
auto_fill_service = AutoFillService()


@auto_fill_controller.route('/api/v1/town_info/auto_fill/<town_name>')
def get_auto_fill(town_name):
    result = render_template('autoFill.html', townName=town_name,
                             data=" ".join(auto_fill_service.get_autofill(town_name)))
    if not result:
        return f"Couldn't find auto fill for: {town_name}", 400
    return result, 200, {'Content-Type': 'text/html'}
