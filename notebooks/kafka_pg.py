import psycopg2
import random
from datetime import datetime
from kafka import KafkaConsumer
from json import loads

conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432",
)

cur = conn.cursor()

# -- Drop the 'messages' table if it exists
cur.execute("DROP TABLE IF EXISTS messages;")

# -- Create the 'messages' table
cur.execute(
    """CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP,
    message_id VARCHAR(255),
    client_id INTEGER,
    amount INTEGER);"""
)

consumer = KafkaConsumer(
    "streaming",
    bootstrap_servers=["broker:9092"],
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="bootstrap-server",
    value_deserializer=lambda x: loads(x.decode("ISO-8859-1")),
)

try:
    for message in consumer:
        cur.execute(
            "INSERT INTO messages (time, message_id, client_id, amount) VALUES (%s, %s, %s, %s)",
            (
                message.value["time"],
                message.value["message_id"],
                message.value["client_id"],
                message.value["amount"],
            ),
        )

        conn.commit()

except Exception as e:
    print(f"Błąd: {e}")
    conn.rollback()

finally:
    cur.close()
    conn.close()
