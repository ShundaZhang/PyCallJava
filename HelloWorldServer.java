import py4j.GatewayServer;

public class HelloWorldServer {
    public String greet(String name) {
        return "Hello, " + name + " from Py4J!";
    }
    
    public static void main(String[] args) {
        GatewayServer server = new GatewayServer(new HelloWorldServer());
        server.start();
        System.out.println("Gateway Server Started");
    }
}
