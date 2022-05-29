from tokenize import String

import requests as requests
import unidecode as unidecode

from config import Config as config


class AutoFillRequester:
    def __init__(self):
        self.base = config.AUTOFILL_BASE
        self.key = config.AUTO_FILL_KEY

    def request_autofill(self, town_name: String):
        url = self.base.replace('{town}', unidecode.unidecode(str(town_name).lower())).replace('{key}', self.key)
        response = requests.get(url=url)
        return response.json()
