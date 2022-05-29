from autoFill.auto_fill_requester import AutoFillRequester


class AutoFillService:
    def __init__(self):
        self.auto_fill_requester = AutoFillRequester()

    def get_autofill(self, town_name):
        request_data = self.auto_fill_requester.request_autofill(town_name)
        towns_names = list(map(lambda x: x["name"], request_data))
        return towns_names
