package jav;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Arrays;

public class JavaUdpServer {
    public JavaUdpServer() {
    }

    public static void main(String[] var0) {
        System.out.println("JAVA UDP SERVER");
        DatagramSocket var1 = null;
        int clientPort = 9009;
        int serverPort = 9008;

        try {
            var1 = new DatagramSocket(serverPort);
            byte[] var3 = new byte[1024];
            byte[] var32 = new byte[1024];


            while(true) {
                //===receive
                Arrays.fill(var3, (byte)0);
                DatagramPacket var4 = new DatagramPacket(var3, var3.length);
                var1.receive(var4);
                clientPort=  var4.getPort();
                String var5 = new String(var4.getData());
                System.out.println("received msg: " + var5);
                //===send
                byte[] message = "Ping Java Udp from server".getBytes();
                DatagramPacket packet = new DatagramPacket(message,message.length,var4.getAddress(),clientPort);
                var1.send(packet);
                //===receive bytes
                Arrays.fill(var32, (byte)0);
                DatagramPacket var42 = new DatagramPacket(var32, var32.length);

                var1.receive(var42);
                int nb = ByteBuffer.wrap(var32).order(ByteOrder.LITTLE_ENDIAN).getInt();
                System.out.printf("received msg: %d%n", nb);
                //===send bytes
                byte[] message2 = ByteBuffer.allocate(4).order(ByteOrder.LITTLE_ENDIAN).putInt(nb+1).array();
                DatagramPacket packet2 = new DatagramPacket(message2,message2.length,var42.getAddress(),clientPort);
                var1.send(packet2);

            }
        } catch (Exception var9) {
            var9.printStackTrace();
        } finally {
            if (var1 != null) {
                var1.close();
            }

        }

    }
}
