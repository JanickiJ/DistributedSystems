from flask import Blueprint, render_template

from youtube.youtube_service import YoutubeService

youtube_controller = Blueprint('youtube_controller', __name__, template_folder='templates')
youtube_server = YoutubeService()


@youtube_controller.route('/api/v1/town_info/youtube/<title>')
def get_youtube(title):
    data = youtube_server.get_most_popular_film_url(title)
    if not data:
        return f"Couldn't find youtube video for {title}", 400
    return render_template('youtube.html', data=data), 200, {'Content-Type': 'text/html'}
