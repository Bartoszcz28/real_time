import json
import random
import sys
from datetime import datetime, timedelta
from time import sleep
from kafka import KafkaProducer

if __name__ == "__main__":
    SERVER = "broker:9092"

    producer = KafkaProducer(
        bootstrap_servers=[SERVER],
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        api_version=(3, 7, 0),
    )

    message_id = 0
    try:
        while True:
            message_id += 1
            t = datetime.now() + timedelta(seconds=random.randint(-15, 0))

            message = {
                "time": str(t),
                "message_id": message_id,
                "client_id": random.randint(0, 100),
                "amount": random.randint(-1000, 1000),
            }

            producer.send("streaming", value=message)
            sleep(1)
    except KeyboardInterrupt:
        producer.close()
