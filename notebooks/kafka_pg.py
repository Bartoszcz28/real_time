import psycopg2
import random
from datetime import datetime
from kafka import KafkaConsumer
from json import loads

# Ustawienia połączenia do bazy danych PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432",
)

cur = conn.cursor()

# Ustawienia konsumenta Kafka
consumer = KafkaConsumer(
    "aml",
    bootstrap_servers=["broker:9092"],
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="bootstrap-server2",
    value_deserializer=lambda x: loads(x.decode("utf-8")),
)

try:
    for message in consumer:
        if message.value["aml"] == 1:
            table = 'aml_true'
        else:
            table = 'aml_false'
        cur.execute(
            f"""INSERT INTO {table} (
                time, message_id, client_id, amount, first_name, last_name, email, 
                gender, country_id, country, capital, atm_id, atm_number, aml
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                message.value["time"],
                message.value["message_id"],
                message.value["client_id"],
                message.value["amount"],
                message.value["first_name"],
                message.value["last_name"],
                message.value["email"],
                message.value["gender"],
                message.value["country_id"],
                message.value["country"],
                message.value["capital"],
                message.value["atm_id"],
                message.value["atm_number"],
                message.value["aml"],
            ),
        )

        conn.commit()

except Exception as e:
    print(f"Błąd: {e}")
    conn.rollback()

finally:
    cur.close()
    conn.close()
    consumer.close()