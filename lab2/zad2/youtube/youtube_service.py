from youtube.youtube_requester import YoutubeRequester
from config import Config as config

class YoutubeService:
    def __init__(self):
        self.youtube_requester = YoutubeRequester()

    def get_most_popular_film_url(self, title):
        request_data = self.youtube_requester.get_most_popular_film_json(title)
        url = config.YT_BASE.__add__(request_data['items'][0]['id']['videoId'])
        return url

