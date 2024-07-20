from kafka import KafkaProducer
from kafka import KafkaConsumer

# Producer implementation
producer = KafkaProducer(bootstrap_servers='localhost:9092')
future = producer.send('greetings', b'Hello, world of Kafka')


# Consumer implementation
consumer = KafkaConsumer('greetings')
for msg in consumer:
    print(msg)