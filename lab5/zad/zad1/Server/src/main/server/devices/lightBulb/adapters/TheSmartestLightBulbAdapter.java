package main.server.devices.lightBulb.adapters;

import Home.Colors;

public class TheSmartestLightBulbAdapter extends SmartLightBulbAdapter {
    public static Colors[] possibleColors = {Colors.WHITE, Colors.BLUE, Colors.GREEN, Colors.RED, Colors.RAINBOW};

    public TheSmartestLightBulbAdapter(String name, boolean isOn, Colors color) {
        super(name, isOn, color);
        this.possibleLightBlubColors = possibleColors;
    }

    public TheSmartestLightBulbAdapter(String name) {
        super(name);
        this.possibleLightBlubColors = possibleColors;
    }
}
