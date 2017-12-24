package com.ljja.production.http;

import org.eclipse.jetty.server.Server;

public class HttpServer {
    
    private static int serverPort = 40080;

    public static void main(String[] args) {

        try {

            if (null != args && args.length > 1) {
                serverPort = Integer.valueOf(args[0]);
            }

            Server server = new Server(serverPort);

            server.setHandler(new NaiveBayesHandler());

            System.out.println("server start port:" + serverPort);
            server.start();

            System.out.println("server join");
            server.join();

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            System.out.println("server exit");
        }
    }
}
