package jav;//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class JavaTcpClient {
    public JavaTcpClient() {
    }

    public static void main(String[] var0) throws IOException {
        System.out.println("JAVA TCP CLIENT");
        String var1 = "localhost";
        short var2 = 12345;
        Socket var3 = null;

        try {
            var3 = new Socket(var1, var2);
            PrintWriter var4 = new PrintWriter(var3.getOutputStream(), true);
            BufferedReader var5 = new BufferedReader(new InputStreamReader(var3.getInputStream()));
            var4.println("Ping Java Tcp");
            String var6 = var5.readLine();
            System.out.println("received response: " + var6);
        } catch (Exception var10) {
            var10.printStackTrace();
        } finally {
            if (var3 != null) {
                var3.close();
            }

        }

    }
}
