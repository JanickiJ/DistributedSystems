import Ice

import Home


def string_to_color(name: str):
    if isinstance(name, Home.Colors):
        return name
    name = name.lower()
    result = ""
    if name == "white":
        result = Home.Colors.WHITE
    if name == "green":
        result = Home.Colors.GREEN
    if name == "blue":
        result = Home.Colors.BLUE
    if name == "red":
        result = Home.Colors.RED
    if name == "rainbow":
        result = Home.Colors.RAINBOW
    return result


def string_to_oven_mode(name: str):
    if isinstance(name, Home.OvenMode):
        return name
    name = name.upper()
    result = ""
    if name == "FAN":
        result = Home.OvenMode.FAN
    if name == "CONVENTIONALHEATING":
        result = Home.OvenMode.CONVENTIONALHEATING
    if name == "BOTTOMHEAT":
        result = Home.OvenMode.BOTTOMHEAT
    if name == "FANWITHGRILL":
        result = Home.OvenMode.FANWITHGRILL
    if name == "GRILL":
        result = Home.OvenMode.GRILL
    if name == "DEFROSTING":
        result = Home.OvenMode.DEFROSTING
    if name == "LIGHT":
        result = Home.OvenMode.LIGHT

    return result


def check_connection(proxy):
    try:
        proxy.ice_ping()
        return True
    except (Ice.ConnectionRefusedException, Ice.ObjectNotExistException) as e:
        return False


def get_connected_devices(devices):
    return list(filter(lambda device: check_connection(device.proxy), devices.values()))
