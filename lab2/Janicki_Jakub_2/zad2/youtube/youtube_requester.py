import requests as requests

from config import Config as config

import googleapiclient.discovery


class YoutubeRequester:
    def __init__(self):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.youtube = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, developerKey=config.YT_KEY)

    def get_most_popular_film_json(self, title):
        request = self.youtube.search().list(
            part="id,snippet",
            type='video',
            q=title,
            videoDuration='short',
            videoDefinition='high',
            maxResults=1
        )
        response = request.execute()
        return response
