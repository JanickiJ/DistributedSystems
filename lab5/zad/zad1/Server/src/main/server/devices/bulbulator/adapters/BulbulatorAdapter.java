package main.server.devices.bulbulator.adapters;

import Home.*;
import com.zeroc.Ice.Current;
import com.zeroc.Ice.InputStream;
import com.zeroc.Ice.OutputStream;

import java.util.List;
import java.util.Map;

public class BulbulatorAdapter extends Bulbulator implements BulbulatorI {
    public static List<String> parametersNames = List.of("name", "type", "isOn", "phrase", "repeatNumber");

    public BulbulatorAdapter(String name, boolean isOn, String phrase, short repeatNumber) {
        super(name, DeviceType.BULBULATOR, isOn, phrase, repeatNumber);
    }

    public BulbulatorAdapter(String name) {
        super(name, DeviceType.BULBULATOR, false, name, (short) 3);
    }

    @Override
    public boolean isBulbulatorSaturator(Current current) {
        return false;
    }

    @Override
    public String makeNoise(short repeatNumber, Current current) throws TurnOnToMakeNoiseException {
        if (isOn) {
            return phrase.repeat(repeatNumber);
        }
        throw new TurnOnToMakeNoiseException("[" + name + "] Turn on before making noise");
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
                "phrase", this.phrase,
                "repeatNumber", String.valueOf(this.repeatNumber)
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
                        {
                            if (Boolean.parseBoolean(entry.getValue())) {
                                turnDeviceOn(current);
                            } else {
                                turnDeviceOff(current);
                            }
                        }
                    }
                    if (entry.getKey().equals("phrase")) {
                        this.phrase = entry.getValue();
                    }
                    if (entry.getKey().equals("repeatNumber")) {
                        this.repeatNumber = Short.parseShort(entry.getValue());
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
        BulbulatorI.super._iceWriteImpl(ostr);
    }

    @Override
    public void _iceReadImpl(InputStream istr) {
        BulbulatorI.super._iceReadImpl(istr);
    }
}
