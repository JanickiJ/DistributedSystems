import com.rabbitmq.client.*;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.apache.log4j.BasicConfigurator;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

@Slf4j
public class Admin implements Runnable {
    private final static String EXCHANGE_NAME = "exchange_name";
    private final static String INFO_QUEUE_NAME = "info_queue_name";
    private final Scanner scanner;
    private final Channel channel;

    @SneakyThrows
    public Admin() {
        this.scanner = new Scanner(System.in);
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        this.channel = connection.createChannel();
    }

    public static void main(String[] args) {
        BasicConfigurator.configure();
        Admin admin = new Admin();
        admin.setup();
        while (true) {
            admin.run();
        }
    }

    @SneakyThrows
    public void setup() {
        log.info("started");
        Consumer consumer = new DefaultConsumer(channel) {
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
                String message = new String(body, StandardCharsets.UTF_8);
                log.info("Message received: " + message);
            }
        };

        channel.exchangeDeclare(EXCHANGE_NAME, BuiltinExchangeType.TOPIC);
        channel.queueDeclare(INFO_QUEUE_NAME, false, false, false, null);
        channel.queueBind(INFO_QUEUE_NAME, EXCHANGE_NAME, "#");
        channel.basicConsume(INFO_QUEUE_NAME, true, consumer);
    }

    @SneakyThrows
    @Override
    public void run() {
        log.info("Pass receiver:");
        log.info("teams: all teams");
        log.info("suppliers: all suppliers");
        log.info("all: all");
        String good = scanner.nextLine();
        String key = switch (good) {
            case "teams" -> "receiver.sth.team";
            case "suppliers" -> "receiver.supplier.sth";
            default -> "receiver.supplier.team";
        };
        log.info("Pass message");
        String message = scanner.nextLine();
        channel.basicPublish(EXCHANGE_NAME, key, null, message.getBytes(StandardCharsets.UTF_8));
    }
}
