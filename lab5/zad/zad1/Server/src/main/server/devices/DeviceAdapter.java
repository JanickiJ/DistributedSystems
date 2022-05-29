package main.server.devices;

import Home.*;
import Home.Exception;
import com.zeroc.Ice.Current;
import com.zeroc.Ice.InputStream;
import com.zeroc.Ice.OutputStream;

import java.util.List;
import java.util.Map;

public abstract class DeviceAdapter extends Device implements DeviceI {
    public String name;
    public DeviceType type;
    public boolean isOn;
    public List<String> parametersNames;

    public DeviceAdapter(String name, DeviceType type, boolean isOn) {
        this.name = name;
        this.type = type;
        this.isOn = isOn;
        this.parametersNames = List.of("name","type","isOn");
    }

    @Override
    public void turnDeviceOn(Current current) throws isAlreadyONException {
        if (isOn) {
            throw new isAlreadyONException("["+name+"] Object is already on");
        } else {
            this.isOn = true;
        }
    }

    @Override
    public void turnDeviceOff(Current current) throws isAlreadyOFFException {
        if (!isOn) {
            throw new isAlreadyOFFException("["+name+"] Object is already off");
        } else {
            this.isOn = false;
        }
    }

    @Override
    public Map<String, String> getDeviceParameters(Current current) {
        return Map.of(
                "name", this.name,
                "type", String.valueOf(this.type),
                "isOn", String.valueOf(this.isOn)
        );
    }

    @Override
    public void setParameters(Map<String, String> deviceParameters, Current current) throws InvalidParameterException {
        for (var entry : deviceParameters.entrySet()) {
            if(parametersNames.contains(entry.getKey())){
                switch (entry.getKey()){
                    case "name": this.name = entry.getValue();
                    case "type": this.type = DeviceType.valueOf(entry.getValue());
                    case "isOn": this.isOn = Boolean.parseBoolean(entry.getValue());
                    default:
                }
            }else {
                throw new InvalidParameterException("["+name+"] Invalid parameter: " + entry.getKey() + " Possible parameters: " + parametersNames);
            }
        }
    }

    @Override
    public void _iceWriteImpl(OutputStream ostr) {
        DeviceI.super._iceWriteImpl(ostr);
    }

    @Override
    public void _iceReadImpl(InputStream istr) {
        DeviceI.super._iceReadImpl(istr);
    }
}
