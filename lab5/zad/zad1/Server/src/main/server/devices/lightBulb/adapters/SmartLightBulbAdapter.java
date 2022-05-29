package main.server.devices.lightBulb.adapters;

import Home.*;
import com.zeroc.Ice.Current;
import com.zeroc.Ice.InputStream;
import com.zeroc.Ice.OutputStream;

import java.lang.Exception;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class SmartLightBulbAdapter extends LightBlub implements LightBlubI {
    public static List<String> parametersNames = List.of("name", "type", "isOn", "color");
    public static Colors[] supportedColors = {Colors.WHITE};

    public SmartLightBulbAdapter(String name, boolean isOn, Colors color) {
        super(name, DeviceType.LIGHTBULB, isOn, supportedColors, color);
    }

    public SmartLightBulbAdapter(String name) {
        super(name, DeviceType.LIGHTBULB, false, supportedColors, Colors.WHITE);
    }

    @Override
    public void setColor(Colors color, Current current) throws UnsupportedColorException {
        if (Arrays.asList(possibleLightBlubColors).contains(color)) {
            this.color = color;
        } else {
            throw new UnsupportedColorException("[" + name + "] Unsupported color: " + color + " Possible colors: " + Arrays.toString(this.possibleLightBlubColors));
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
    public Map<String, String> getDeviceParameters(Current current) {
        return Map.of(
                "name", this.name,
                "type", String.valueOf(this.type),
                "isOn", String.valueOf(this.isOn),
                "color", String.valueOf(this.color)
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
                    if (entry.getKey().equals("color")) {
                        setColor(Colors.valueOf(entry.getValue()), current);
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
        LightBlubI.super._iceWriteImpl(ostr);
    }

    @Override
    public void _iceReadImpl(InputStream istr) {
        LightBlubI.super._iceReadImpl(istr);
    }
}
