package main.server.devices.lightBulb.servants;

import Home.*;
import com.zeroc.Ice.Current;
import main.server.devices.lightBulb.adapters.SmartLightBulbAdapter;

import java.util.Map;

public class SmartLightServant implements LightBlubI {
    public String name;
    public SmartLightBulbAdapter smartLightBlobInstance;

    public SmartLightServant(String name) {
        this.name = name;
        this.smartLightBlobInstance = new SmartLightBulbAdapter(name,false,Colors.WHITE);
    }

    @Override
    public void turnDeviceOn(Current current) throws isAlreadyONException {
        smartLightBlobInstance.turnDeviceOn(current);
    }

    @Override
    public void turnDeviceOff(Current current) throws isAlreadyOFFException {
        smartLightBlobInstance.turnDeviceOff(current);
    }

    @Override
    public Map<String, String> getDeviceParameters(Current current) {
        return smartLightBlobInstance.getDeviceParameters(current);
    }

    @Override
    public void setParameters(Map<String, String> deviceParameters, Current current) throws InvalidParameterException {
        smartLightBlobInstance.setParameters(deviceParameters,current);
    }

    @Override
    public void setColor(Colors color, Current current) throws UnsupportedColorException {
        smartLightBlobInstance.setColor(color, current);
    }
}