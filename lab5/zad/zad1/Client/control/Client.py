from threading import Thread

import Ice

import Home
from control.Connection import Connection
from control.utils import get_connected_devices
from devices.bulbulator import Bulbulator
from devices.smart_light_blub import SmartLightBlub
from devices.smart_oven import SmartOven


class Client:
    def __init__(self, communicator):
        self.devices_names = ["bulbulator1", "bulbulator2", "smartLightBulb", "smarterLightBulb",
                              "theSmartestLightBulb", "smartOven", "smarterOven", "theSmartestOven"]
        self.server1_devices = ["bulbulator1", "smartLightBulb", "smarterLightBulb",
                                "theSmartestLightBulb"]
        self.server2_devices = ["bulbulator2", "smartOven", "smarterOven", "theSmartestOven"]
        self.devices = dict()
        self.communicator = communicator
        self.connections = []

    def init_devices(self):
        for name in self.devices_names:
            base = self.communicator.propertyToProxy(name + '.Proxy')
            try:
                if name.startswith("bulbulator"):
                    self.devices[name] = (Bulbulator(name, Home.BulbulatorIPrx.uncheckedCast(base)))
                elif name.endswith("LightBulb"):
                    self.devices[name] = (SmartLightBlub(name, Home.LightBulbIPrx.uncheckedCast(base)))
                elif name.endswith("Oven"):
                    self.devices[name] = (SmartOven(name, Home.OvenIPrx.uncheckedCast(base)))
            except Ice.ConnectionRefusedException:
                print(f"Cannot connect {name}")

        for connection_name, devices in [("connection1", self.server1_devices),
                                         ("connection2", self.server2_devices)]:
            base = self.communicator.propertyToProxy(connection_name + '.Proxy')
            try:
                connection = Connection(connection_name, Home.ConnectionIPrx.uncheckedCast(base),
                                        {k: v for k, v in self.devices.items() if v.name in devices})
            except Ice.ConnectionRefusedException:
                print(f"Cannot connect {name}")
        self.connections.append(connection)
        Thread(daemon=True, target=connection.scheduler).start()

    def run_io(self):
        while True:
            print("Checking connection...")
            connected_devices = get_connected_devices(self.devices)
            print("Connected devices: " + " ".join(map(lambda device: device.name, connected_devices)))
            print("Pass device's name")
            name = input()
            if not name:
                continue
            if name not in self.devices_names:
                print("Pass correct device's name")
                continue
            while True:
                device = self.devices[name]
                commands = device.get_commands() + ["change_device"]
                print("Pass action: " + " ".join(commands))
                command = input()
                if command not in commands:
                    print("Pass correct device's command")
                elif command == "change_device":
                    break
                else:
                    device.action(command)
