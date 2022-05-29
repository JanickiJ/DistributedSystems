package main.server.devices.oven.servants;

import Home.OvenMode;
import main.server.devices.oven.adapters.TheSmartestOvenAdapter;

public class TheSmartestOvenServant extends SmartOvenServant {
    public TheSmartestOvenServant(String name) {
        super(name);
        this.smartOvenAdapterInstance = new TheSmartestOvenAdapter(name, false, OvenMode.FAN, (short) 10, false);
    }
}
