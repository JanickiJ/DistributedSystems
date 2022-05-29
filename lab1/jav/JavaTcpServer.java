package jav;//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class JavaTcpServer {
    public JavaTcpServer() {
    }

    public static void main(String[] var0) throws IOException {
        System.out.println("JAVA TCP SERVER");
        short var1 = 12345;
        ServerSocket var2 = null;

        try {
            var2 = new ServerSocket(var1);

            while(true) {
                Socket var3 = var2.accept();
                System.out.println("client connected");
                PrintWriter var4 = new PrintWriter(var3.getOutputStream(), true);
                BufferedReader var5 = new BufferedReader(new InputStreamReader(var3.getInputStream()));
                String var6 = var5.readLine();
                System.out.println("received msg: " + var6);
                var4.println("Pong Java Tcp");
            }
        } catch (IOException var10) {
            var10.printStackTrace();
        } finally {
            if (var2 != null) {
                var2.close();
            }

        }

    }
}
