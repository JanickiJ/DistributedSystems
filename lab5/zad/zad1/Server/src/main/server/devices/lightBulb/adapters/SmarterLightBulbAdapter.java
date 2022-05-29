package main.server.devices.lightBulb.adapters;

import Home.Colors;

public class SmarterLightBulbAdapter extends SmartLightBulbAdapter {
    public static Colors[] possibleColors= {Colors.WHITE,Colors.BLUE,Colors.GREEN,Colors.RED};
    public SmarterLightBulbAdapter(String name, boolean isOn, Colors color) {
        super(name, isOn, color);
        this.possibleLightBlubColors = possibleColors;
    }

    public SmarterLightBulbAdapter(String name){
        super(name);
        this.possibleLightBlubColors = possibleColors;
    }
}
