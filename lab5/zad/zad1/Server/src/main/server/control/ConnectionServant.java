package main.server.control;
import Home.ConnectionI;
import com.zeroc.Ice.Current;
import main.server.control.ConnectionAdapter;


public class ConnectionServant implements ConnectionI {

    ConnectionAdapter connectionAdapter;
    String name;
    public ConnectionServant(String name){
        this.name = name;
        this.connectionAdapter = new ConnectionAdapter();
    }
    @Override
    public void ping(String[] devices, Current current) {
        connectionAdapter.ping(devices,current);
    }
}
