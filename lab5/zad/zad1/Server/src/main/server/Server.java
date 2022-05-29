package main.server;

import com.zeroc.Ice.Communicator;
import com.zeroc.Ice.Identity;
import com.zeroc.Ice.ObjectAdapter;
import com.zeroc.Ice.Util;
import main.server.control.ConnectionServant;
import main.server.devices.bulbulator.servants.BulbulatorServant;
import main.server.devices.lightBulb.servants.SmartLightServant;
import main.server.devices.lightBulb.servants.SmarterLightServant;
import main.server.devices.lightBulb.servants.TheSmartestLightServant;
import main.server.devices.oven.servants.SmartOvenServant;
import main.server.devices.oven.servants.SmarterOvenServant;
import main.server.devices.oven.servants.TheSmartestOvenServant;

public class Server {
    public static void main(String[] args) {
        Server app = new Server(args);
    }

    public Server(String[] args) {
        int status = 0;
        Communicator communicator = null;
        try	{
            communicator = Util.initialize(args);

            ObjectAdapter adapter = communicator.createObjectAdapter("Adapter");

            // 3. Stworzenie serwanta/serwantów
            BulbulatorServant bulbulatorServant1 = new BulbulatorServant("bulbulator1");
            BulbulatorServant bulbulatorServant2 = new BulbulatorServant("bulbulator2");
            SmartLightServant smartLightServant = new SmartLightServant("smartLight");
            SmarterLightServant smarterLightServant = new SmarterLightServant("smarterLight");
            TheSmartestLightServant theSmartestLightServant = new TheSmartestLightServant("theSmartestLight");
            SmartOvenServant smartOvenServant = new SmartOvenServant("smartOven");
            SmarterOvenServant smarterOvenServant = new SmarterOvenServant("smarterOven");
            TheSmartestOvenServant theSmartestOvenServant = new TheSmartestOvenServant("theSmartestOven");
            ConnectionServant connectionServant = new ConnectionServant("connectionServant");

            // 4. Dodanie wpisów do tablicy ASM, skojarzenie nazwy obiektu (Identity) z serwantem
            adapter.add(bulbulatorServant1, new Identity("bulbulator1", "bulbulator"));
            adapter.add(bulbulatorServant2, new Identity("bulbulator2", "bulbulator"));
            adapter.add(smartLightServant, new Identity("smartLight", "light"));
            adapter.add(smarterLightServant, new Identity("smarterLight", "light"));
            adapter.add(theSmartestLightServant, new Identity("theSmartestLight", "light"));
            adapter.add(smartOvenServant, new Identity("smartOven", "oven"));
            adapter.add(smarterOvenServant, new Identity("smarterOven", "oven"));
            adapter.add(theSmartestOvenServant, new Identity("theSmartestOven", "oven"));
            adapter.add(connectionServant, new Identity("connectionServant", "connection"));
            // 5. Aktywacja adaptera i wejście w pętlę przetwarzania żądań
            adapter.activate();

            System.out.println("Entering event processing loop...");

            communicator.waitForShutdown();

        }
        catch (Exception e) {
            System.err.println(e.toString());
            status = 1;
        }
        if (communicator != null) {
            try {
                communicator.destroy();
            }
            catch (Exception e) {
                System.err.println(e.toString());
                status = 1;
            }
        }
        System.exit(status);
    }
}
