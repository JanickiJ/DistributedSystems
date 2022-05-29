from devices.device import Device
from control.utils import string_to_color


class SmartLightBlub(Device):
    def __init__(self, name, proxy):
        super().__init__(name, proxy)
        self.commands.extend(["set_color"])

    def action(self, name):
        super().action(name)
        if name == "set_color":
            print("Pass color")
            color = string_to_color(input())
            print(color)
            if color:
                self.set_color(string_to_color(color))
            else:
                print("Unsupported color")

    def set_color(self, color):
        try:
            self.proxy.setColor(color)
            print("Color set")
        except Exception as e:
            print(e)
