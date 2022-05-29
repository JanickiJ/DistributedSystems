#ifndef _HOME_ICE
#define _HOME_ICE

module Home
{
  enum DeviceType {OVEN,BULBULATOR,LIGHTBULB};
  enum Colors {RED,GREEN,BLUE,WHITE,RAINBOW};
  enum OvenMode {FAN,CONVENTIONALHEATING,BOTTOMHEAT,
   FANWITHGRILL, GRILL,
   DEFROSTING, LIGHT};

   sequence<Colors> possibleLightBulbColors;
   sequence<OvenMode> possibleOvenMods;
   dictionary<string,string> DeviceParameters;

   exception Exception{
    string message;
   };
   exception InvalidParameterException extends Exception{};
   exception isAlreadyONException extends InvalidParameterException{};
   exception isAlreadyOFFException extends InvalidParameterException{};
   exception UnsupportedColorException extends InvalidParameterException{};
   exception UnsupportedOvenModeException extends InvalidParameterException{};
   exception TemperatureOutOfScope extends InvalidParameterException{};
   exception OvenOpenCantPerformActionException extends InvalidParameterException{};
   exception TurnOnToMakeNoiseException extends Exception{};

   class Device{
    string name;
    DeviceType type;
    bool isOn;
   };

   interface DeviceI{
    void turnDeviceOn() throws isAlreadyONException;
    void turnDeviceOff() throws isAlreadyOFFException;
    idempotent DeviceParameters getDeviceParameters();
    void setParameters(DeviceParameters deviceParameters) throws InvalidParameterException;
   };

   class LightBulb extends Device{
    possibleLightBulbColors possibleLightBulbColors;
    Colors color;
   };

   interface LightBulbI extends DeviceI{
    void setColor(Colors color) throws UnsupportedColorException;
   };

   class Oven extends Device {
    possibleOvenMods possibleOvenMods;
    OvenMode ovenMode;
    short temperature;
    bool isOpen;
   };

   interface OvenI extends DeviceI {
    void setOvenMode(OvenMode ovenMode) throws UnsupportedOvenModeException, OvenOpenCantPerformActionException;
    void setTemperature(short temperature) throws TemperatureOutOfScope;
   };

   class Bulbulator extends Device{
    string phrase;
    short repeatNumber;
   };

   interface BulbulatorI extends DeviceI {
    bool isBulbulatorSaturator();
    string makeNoise(short repeatNumber) throws TurnOnToMakeNoiseException;
   };

   class DeviceName{
    string name;
   };

   sequence<string> Devices;
   class Connection{
       Devices devices;
   };
   interface ConnectionI {
    void ping(Devices devices);
   };

};


#endif
