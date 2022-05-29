package jav;//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Arrays;

public class JavaUdpClient {
    public JavaUdpClient() {
    }

    public static void main(String[] var0) throws Exception {
        System.out.println("JAVA UDP CLIENT");
        DatagramSocket var1 = null;
        short clientPort = 9009;
        short serverPort = 9008;

        try {
            var1 = new DatagramSocket(clientPort);
            InetAddress var3 = InetAddress.getByName("localhost");
            //====send
            byte[] var4 = "Ping Java Udp from client".getBytes();
            DatagramPacket var5 = new DatagramPacket(var4, var4.length, var3, serverPort);
            var1.send(var5);
            //====receive
            byte[] message = new byte[1024];
            Arrays.fill(message, (byte)0);
            DatagramPacket packet = new DatagramPacket(message, message.length);
            var1.receive(packet);
            System.out.println("received msg: " + new String(packet.getData()));

        } catch (Exception var9) {
            var9.printStackTrace();
        } finally {
            if (var1 != null) {
                var1.close();
            }

        }

    }
}
