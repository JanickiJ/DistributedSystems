package main.server.devices.oven.servants;

import Home.*;
import com.zeroc.Ice.Current;
import main.server.devices.oven.adapters.SmartOvenAdapter;

import java.util.Map;

public class SmartOvenServant implements OvenI {
    public String name;
    public SmartOvenAdapter smartOvenAdapterInstance;

    public SmartOvenServant(String name) {
        this.name = name;
        this.smartOvenAdapterInstance = new SmartOvenAdapter(name, false, OvenMode.FAN, (short) 10, false);
    }

    @Override
    public void turnDeviceOn(Current current) throws isAlreadyONException {
        smartOvenAdapterInstance.turnDeviceOn(current);
    }

    @Override
    public void turnDeviceOff(Current current) throws isAlreadyOFFException {
        smartOvenAdapterInstance.turnDeviceOff(current);
    }

    @Override
    public Map<String, String> getDeviceParameters(Current current) {
        return smartOvenAdapterInstance.getDeviceParameters(current);
    }

    @Override
    public void setParameters(Map<String, String> deviceParameters, Current current) throws InvalidParameterException {
        smartOvenAdapterInstance.setParameters(deviceParameters, current);
    }

    @Override
    public void setOvenMode(OvenMode ovenMode, Current current) throws OvenOpenCantPerformActionException, UnsupportedOvenModeException {
        smartOvenAdapterInstance.setOvenMode(ovenMode, current);
    }

    @Override
    public void setTemperature(short temperature, Current current) throws TemperatureOutOfScope {
        smartOvenAdapterInstance.setTemperature(temperature, current);
    }

}
