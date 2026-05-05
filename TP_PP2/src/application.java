import javax.xml.ws.Endpoint;

public class application {
    public static void main(String[] args) {
        System.out.println("deploying Service web!!");
        String url = "http://localhost:8080/";
        Endpoint.publish(url, new serviceweb());
        System.out.println("Service web started!!");
    }
}
