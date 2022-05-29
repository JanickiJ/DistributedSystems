import com.rabbitmq.client.*;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.apache.log4j.BasicConfigurator;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

@Slf4j
public class Team implements Runnable {
    private final String name;
    private final static String EXCHANGE_NAME = "exchange_name";
    private final Set<String> queueNames;
    private final Scanner scanner;
    private Channel channel;
    private Connection connection;

    @SneakyThrows
    public Team() {
        this.scanner = new Scanner(System.in);
        log.info("Pass name");
        this.name = scanner.nextLine();
        this.queueNames = new HashSet<>();
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        this.connection = factory.newConnection();
        this.channel = connection.createChannel();
    }

    public static void main(String[] args) {
        BasicConfigurator.configure();
        Team team = new Team();
        team.setup();
        Runtime.getRuntime().addShutdownHook(new Thread(team::onShutDown));
        while (true){
            team.run();
        }
    }

    @SneakyThrows
    public void onShutDown(){
        channel.close();
        connection.close();
    }

    @SneakyThrows
    public void setup() {
        String logPrefix = "[name] ";
        log.info(logPrefix + "started");

        Consumer adminConsumer = new DefaultConsumer(channel) {
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
                String message = new String(body, StandardCharsets.UTF_8);
                log.info("Received admin message: " + message);
            }
        };


        channel.exchangeDeclare(EXCHANGE_NAME, BuiltinExchangeType.TOPIC);

        String queue = channel.queueDeclare().getQueue();
        channel.queueBind(queue, EXCHANGE_NAME, "receiver.*.team");
        channel.basicConsume(queue, true, adminConsumer);

    }

    @Override
    public void run() {
        log.info("Pass order");
        String good = scanner.nextLine();
        send(good,channel);
    }

    @SneakyThrows
    public void send(String good, Channel channel) {
        String message = name+"#"+good;
        if (!queueNames.contains(good)) {
            channel.queueDeclare(good, false, false, false, null);
            channel.queueBind(good, EXCHANGE_NAME, good);
            queueNames.add(good);
        }
        channel.basicPublish(EXCHANGE_NAME, good, null, message.getBytes(StandardCharsets.UTF_8));
    }
}
