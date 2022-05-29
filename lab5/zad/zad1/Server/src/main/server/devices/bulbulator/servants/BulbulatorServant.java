package main.server.devices.bulbulator.servants;

import Home.*;
import com.zeroc.Ice.Current;
import com.zeroc.Ice.Object;
import main.server.devices.bulbulator.adapters.BulbulatorAdapter;

import java.util.Map;

public class BulbulatorServant implements BulbulatorI {
    public String name;
    public BulbulatorAdapter bulbulatorInstance;

    public BulbulatorServant(String name) {
        this.name = name;
        this.bulbulatorInstance = new BulbulatorAdapter(name, false, name, (short) 3);
    }

    @Override
    public boolean isBulbulatorSaturator(Current current) {
        return bulbulatorInstance.isBulbulatorSaturator(current);
    }

    @Override
    public String makeNoise(short repeatNumber, Current current) throws TurnOnToMakeNoiseException{
        return bulbulatorInstance.makeNoise(repeatNumber, current);
    }

    @Override
    public void turnDeviceOn(Current current) throws isAlreadyONException {
        bulbulatorInstance.turnDeviceOn(current);
    }

    @Override
    public void turnDeviceOff(Current current) throws isAlreadyOFFException {
        bulbulatorInstance.turnDeviceOff(current);
    }

    @Override
    public Map<String, String> getDeviceParameters(Current current) {
        return bulbulatorInstance.getDeviceParameters(current);
    }

    @Override
    public void setParameters(Map<String, String> deviceParameters, Current current) throws InvalidParameterException {
        bulbulatorInstance.setParameters(deviceParameters, current);
    }
}
