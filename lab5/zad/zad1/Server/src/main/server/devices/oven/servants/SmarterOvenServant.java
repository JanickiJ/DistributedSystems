package main.server.devices.oven.servants;

import Home.OvenMode;
import main.server.devices.oven.adapters.SmarterOvenAdapter;

public class SmarterOvenServant extends SmartOvenServant {
    public SmarterOvenServant(String name) {
        super(name);
        this.smartOvenAdapterInstance = new SmarterOvenAdapter(name, false, OvenMode.FAN, (short) 10, false);
    }
}