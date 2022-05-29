package main.server.devices.lightBulb.servants;

import Home.Colors;
import main.server.devices.lightBulb.adapters.SmarterLightBulbAdapter;

public class SmarterLightServant extends SmartLightServant{
    public SmarterLightServant(String name) {
        super(name);
        this.smartLightBlobInstance = new SmarterLightBulbAdapter(name,false, Colors.WHITE);
    }
}
