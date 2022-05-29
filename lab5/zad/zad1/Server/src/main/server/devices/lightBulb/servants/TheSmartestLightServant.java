package main.server.devices.lightBulb.servants;

import Home.Colors;
import main.server.devices.lightBulb.adapters.TheSmartestLightBulbAdapter;

public class TheSmartestLightServant extends SmartLightServant {
    public TheSmartestLightServant(String name) {
        super(name);
        this.smartLightBlobInstance = new TheSmartestLightBulbAdapter(name, false, Colors.WHITE);
    }
}
