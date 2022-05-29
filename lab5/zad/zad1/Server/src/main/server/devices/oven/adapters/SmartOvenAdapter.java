package main.server.devices.oven.adapters;

import Home.*;
import com.zeroc.Ice.Current;
import com.zeroc.Ice.InputStream;
import com.zeroc.Ice.OutputStream;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class SmartOvenAdapter extends Oven implements OvenI {
    public static OvenMode[] possibleOvenModes = {OvenMode.FAN, OvenMode.BOTTOMHEAT, OvenMode.CONVENTIONALHEATING};
    public static List<String> parametersNames = List.of("name", "type", "isOn", "ovenMode", "temperature", "isOpen");
    public static short minTemperature = 0;
    public static short maxTemperature = 200;

    public SmartOvenAdapter(String name, boolean isOn, OvenMode ovenMode, short temperature, boolean isOpen) {
        super(name, DeviceType.OVEN, isOn, possibleOvenModes, ovenMode, temperature, isOpen);
    }

    public SmartOvenAdapter(String name) {
        super(name, DeviceType.OVEN, false, possibleOvenModes, OvenMode.FAN, (short) 0, false);
    }


    @Override
    public void setOvenMode(OvenMode ovenMode, Current current) throws OvenOpenCantPerformActionException, UnsupportedOvenModeException {
        if (isOpen) {
            throw new OvenOpenCantPerformActionException("[" + name + "] Close before changing mode");
        } else if (Arrays.asList(this.possibleOvenMods).contains(ovenMode)) {
            this.ovenMode = ovenMode;
        } else {
            throw new UnsupportedOvenModeException("[" + name + "] Unsupported type: " + ovenMode + " Supported types: " + Arrays.toString(this.possibleOvenMods));
        }
    }

    @Override
    public void turnDeviceOn(Current current) throws isAlreadyONException {
        if (isOn) {
            throw new isAlreadyONException("[" + name + "] Object is already on");
        } else {
            this.isOn = true;
        }
    }

    @Override
    public void turnDeviceOff(Current current) throws isAlreadyOFFException {
        if (!isOn) {
            throw new isAlreadyOFFException("[" + name + "] Object is already off");
        } else {
            this.isOn = false;
        }
    }

    @Override
    public void setTemperature(short temperature, Current current) throws TemperatureOutOfScope {
        if (minTemperature < temperature && temperature < maxTemperature) {
            this.temperature = temperature;
        } else {
            throw new TemperatureOutOfScope("[" + name + "] Temperature value between " + minTemperature + "-" + maxTemperature);
        }
    }


    public Map<String, String> getDeviceParameters(Current current) {
        return Map.of(
                "name", this.name,
                "type", String.valueOf(this.type),
                "isOn", String.valueOf(this.isOn),
                "ovenMode", String.valueOf(this.ovenMode),
                "temperature", String.valueOf(this.temperature),
                "isOpen", String.valueOf(this.isOpen)
        );
    }

    @Override
    public void setParameters(Map<String, String> deviceParameters, Current current) throws InvalidParameterException {
        for (var entry : deviceParameters.entrySet()) {
            if (parametersNames.contains(entry.getKey())) {
                try {
                    if (entry.getKey().equals("name")) {
                        this.name = entry.getValue();
                    }
                    if (entry.getKey().equals("type")) {
                        this.type = DeviceType.valueOf(entry.getValue());
                    }
                    if (entry.getKey().equals("isOn")) {
                        if (Boolean.parseBoolean(entry.getValue())) {
                            turnDeviceOn(current);
                        } else {
                            turnDeviceOff(current);
                        }
                    }
                    if (entry.getKey().equals("ovenMode")) {
                        setOvenMode(OvenMode.valueOf(entry.getValue()), current);
                    }
                    if (entry.getKey().equals("temperature")) {
                        setTemperature(Short.parseShort(entry.getValue()), current);
                    }
                    if (entry.getKey().equals("isOpen")) {
                        this.isOpen = Boolean.parseBoolean(entry.getValue());
                    }
                } catch (IllegalArgumentException illegalArgumentException) {
                    throw new InvalidParameterException("[" + name + "] Invalid value: " + entry.getValue());
                }
            } else {
                throw new InvalidParameterException("[" + name + "] Invalid parameter: " + entry.getKey() + " Possible parameters: " + parametersNames);
            }
        }

    }

    @Override
    public void _iceWriteImpl(OutputStream ostr) {
        OvenI.super._iceWriteImpl(ostr);
    }

    @Override
    public void _iceReadImpl(InputStream istr) {
        OvenI.super._iceReadImpl(istr);
    }
}
