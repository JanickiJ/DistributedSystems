package jav.zad1;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Arrays;

public class JavaUdpClient {

    public static void main(String args[]) throws Exception
    {
        System.out.println("JAVA UDP CLIENT");
        DatagramSocket socket = null;
        short clientPort = 9009;
        short serverPort = 9008;

        try {
            socket = new DatagramSocket(clientPort);
            InetAddress address = InetAddress.getByName("localhost");
            byte[] sendBuffer = "Ping Java Udp".getBytes();

            DatagramPacket sendPacket = new DatagramPacket(sendBuffer, sendBuffer.length, address, serverPort);
            socket.send(sendPacket);
            byte[] message = new byte[1024];
            Arrays.fill(message, (byte)0);
            DatagramPacket packet = new DatagramPacket(message, message.length);
            socket.receive(packet);
            System.out.println("received msg: " + new String(packet.getData()));

        }
        catch(Exception e){
            e.printStackTrace();
        }
        finally {
            if (socket != null) {
                socket.close();
            }
        }
    }
}
