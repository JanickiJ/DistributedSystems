from time import sleep

from control.utils import get_connected_devices


class Connection:
    def __init__(self, name, base, devices):
        self.name = name
        self.proxy = base
        self.devices = devices

    def ping(self):
        try:
            arg = list(map(lambda device: device.name, get_connected_devices(self.devices)))
            self.proxy.ping(arg)
        except Exception as e:
            print(e)

    def scheduler(self):
        while True:
            sleep(10)
            self.ping()
