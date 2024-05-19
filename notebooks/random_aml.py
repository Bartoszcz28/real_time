from kafka import KafkaConsumer, KafkaProducer
from json import loads, dumps
import random
import time

time.sleep(30)


# Consumer configuration
consumer = KafkaConsumer(
    "streaming",
    bootstrap_servers=["broker:9092"],
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="bootstrap-server",
    value_deserializer=lambda x: loads(x.decode("ISO-8859-1")),
)

# Producer configuration
producer = KafkaProducer(
    bootstrap_servers=["broker:9092"],
    value_serializer=lambda x: dumps(x).encode("utf-8")
)
# try:
for message in consumer:
    # Receive the message
    message_value = message.value
    # print(f"Original message: {message_value}")

    # Change the value of "aml" randomly to 1 (positive) or -1 (negative)
    if "aml" in message_value:
        message_value["aml"] = random.choice([1, -1])

        # Wyślij zmodyfikowaną wiadomość na temat "aml"
        producer.send("aml", value=message_value)
        producer.flush()
        # print(f"Modified message: {message_value}")

    # Add a loop break condition if you want to process only one message
    # break

# Close consumer and producer
consumer.close()
producer.close()