import com.rabbitmq.client.*;
import lombok.AllArgsConstructor;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.apache.log4j.BasicConfigurator;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Scanner;

@Slf4j
@AllArgsConstructor
public class Supplier implements Runnable {
    private final String name;
    private final List<String> goods;
    private final static String EXCHANGE_NAME = "exchange_name";
    private int orderCounter = 0;
    private Channel channel;
    private Connection connection;

    public Supplier() {
        Scanner scanner = new Scanner(System.in);
        log.info("Pass name");
        this.name = scanner.nextLine();
        log.info("Pass products");
        this.goods = List.of(scanner.nextLine().split(","));
    }

    public static void main(String[] args) {
        BasicConfigurator.configure();
        Supplier supplier = new Supplier();
        supplier.setup();
        Runtime.getRuntime().addShutdownHook(new Thread(supplier::onShutDown));
        while (true) {
            supplier.run();
        }
    }

    @Override
    public void run() {
    }

    @SneakyThrows
    public void onShutDown(){
        channel.close();
        connection.close();
    }

    @SneakyThrows
    public void setup() {
        String logPrefix = "[" + name + "] ";
        log.info(logPrefix + "started");

        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        connection = factory.newConnection();
        channel = connection.createChannel();

        Consumer goodsConsumer = new DefaultConsumer(channel) {
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
                orderCounter++;
                String message = new String(body, StandardCharsets.UTF_8);
                List<String> parsedMessage = List.of(message.split("#"));
                log.info("Received order [number: " + orderCounter + "] [from: " + parsedMessage.get(0) + "]: " + parsedMessage.get(1));
                channel.basicAck(envelope.getDeliveryTag(), false);
            }
        };

        Consumer adminConsumer = new DefaultConsumer(channel) {
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
                String message = new String(body, StandardCharsets.UTF_8);
                log.info("Received admin message: " + message);
            }
        };

        channel.exchangeDeclare(EXCHANGE_NAME, BuiltinExchangeType.TOPIC);
        String queue = channel.queueDeclare().getQueue();
        channel.queueBind(queue, EXCHANGE_NAME, "receiver.supplier.*");
        channel.basicConsume(queue, true, adminConsumer);

        for (String good : goods) {
            channel.queueDeclare(good, false, false, false, null);
            channel.queueBind(good, EXCHANGE_NAME, good);
            channel.basicConsume(good, false, goodsConsumer);
        }
    }
}
