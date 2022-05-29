from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    WEATHER_REQUESTER_BASE = "https://danepubliczne.imgw.pl/api/data/synop/station/"
    AUTOFILL_BASE = "http://api.weatherapi.com/v1/search.json?key={key}&q={town}"
    AUTO_FILL_KEY = "fee73ee5ebba46bb835204043221603"
    YT_KEY = "AIzaSyAmIhXadKNVaS-GXwx1MKWp2bCHzb5EflY"
    YT_BASE = "https://www.youtube.com/embed/"
    SERVER_URL = "127.0.0.1:5000"
    AIR_POLLUTION_FIND_ALL = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
    AIR_POLLUTION_SENSORS = "https://api.gios.gov.pl/pjp-api/rest//station/sensors/"
    AIR_POLLUTION_MEASUREMENT = "https://api.gios.gov.pl/pjp-api/rest/data/getData/"
