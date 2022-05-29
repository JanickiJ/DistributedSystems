
class Device:
    def __init__(self, name, base):
        self.name = name
        self.proxy = base
        self.commands = ["turn_device_on", "turn_device_off", "get_device_parameters", "set_parameters"]

    def action(self, name):
        if name == "turn_device_on":
            self.turn_device_on()
        if name == "turn_device_off":
            self.turn_device_off()
        if name == "get_device_parameters":
            self.get_device_parameters()
        if name == "set_parameters":
            parameters_to_set = dict()
            parameters = self.get_device_parameters()
            while True:
                print("Type parameter name or \"exit\"")
                parameter_name = input()
                if parameter_name == "exit":
                    break
                elif parameter_name not in parameters:
                    print("Pass correct parameter's name")
                else:
                    print("Pass value")
                    parameter_value = input()
                    parameters_to_set[parameter_name] = parameter_value
            print(parameters_to_set)
            self.set_parameters(parameters_to_set)

    def turn_device_on(self):
        try:
            self.proxy.turnDeviceOn()
            print("Device turned on")
        except Exception as e:
            print(e)

    def turn_device_off(self):
        try:
            self.proxy.turnDeviceOff()
            print("Device turned off")
        except Exception as e:
            print(e)

    def get_device_parameters(self):
        parameters = []
        try:
            parameters = self.proxy.getDeviceParameters()
            print(f'Parameters: {self.proxy.getDeviceParameters()}')
        except Exception as e:
            print(e)
        return parameters

    def set_parameters(self, deviceParameters):
        try:
            self.proxy.setParameters(deviceParameters)
            print("Device parameters set")
        except Exception as e:
            print(e)

    def get_commands(self):
        return self.commands
