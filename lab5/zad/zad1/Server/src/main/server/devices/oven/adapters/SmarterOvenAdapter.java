package main.server.devices.oven.adapters;

import Home.OvenMode;

public class SmarterOvenAdapter extends SmartOvenAdapter {
    public static OvenMode[] possibleOvenModes = {OvenMode.FAN, OvenMode.BOTTOMHEAT, OvenMode.CONVENTIONALHEATING, OvenMode.FANWITHGRILL,OvenMode.GRILL};
    public SmarterOvenAdapter(String name, boolean isOn, OvenMode ovenMode, short temperature,boolean isOpen) {
        super(name,isOn,ovenMode,temperature,isOpen);
        this.possibleOvenMods = possibleOvenModes;
    }

    public SmarterOvenAdapter(String name) {
        super(name);
        this.possibleOvenMods = possibleOvenModes;
    }
}
