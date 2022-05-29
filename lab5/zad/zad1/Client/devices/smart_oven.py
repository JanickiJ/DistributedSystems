from devices.device import Device
from control.utils import string_to_oven_mode


class SmartOven(Device):
    def __init__(self, name, proxy):
        super().__init__(name, proxy)
        self.commands.extend(["set_oven_mode", "set_temperature"])

    def action(self, name):
        super().action(name)
        if name == "set_oven_mode":
            print("Pass oven mode")
            oven_mode = string_to_oven_mode(input())
            if not oven_mode:
                print("Unsupported oven mode")
            else:
                self.set_oven_mode(oven_mode)
        if name == "set_temperature":
            print("Pass temperature")
            temperature = int(input())
            if not temperature:
                print("Unsupported temperature")
            else:
                self.set_temperature(temperature)

    def set_oven_mode(self, ovenMode):
        try:
            self.proxy.setOvenMode(ovenMode)
            print("Oven mode set")
        except Exception as e:
            print(e)

    def set_temperature(self, temperature):
        try:
            self.proxy.setTemperature(temperature)
            print("Temperature set")
        except Exception as e:
            print(e)
