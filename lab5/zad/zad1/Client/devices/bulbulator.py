from devices.device import Device


class Bulbulator(Device):
    def __init__(self, name, proxy):
        super().__init__(name, proxy)
        self.commands.extend(["is_bulbulator_saturator", "make_noise"])

    def action(self, name):
        super().action(name)
        if name == "is_bulbulator_saturator":
            self.is_bulbulator_saturator()
        if name == "make_noise":
            print("Pass repeat number")
            repeat_number = input()
            self.make_noise(int(repeat_number))

    def is_bulbulator_saturator(self):
        try:
            print(self.proxy.isBulbulatorSaturator())
        except Exception as e:
            print(e)

    def make_noise(self, repeatNumber):
        try:
            print(self.proxy.makeNoise(repeatNumber))
        except Exception as e:
            print(e)
