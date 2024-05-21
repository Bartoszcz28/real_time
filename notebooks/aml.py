from kafka import KafkaConsumer, KafkaProducer
from json import loads, dumps
import random
import time
from haversine import haversine
import psycopg2
import pandas as pd
from datetime import datetime

# PostgreSQL database connection settings
conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432",
)

cur = conn.cursor()

cur.execute("SELECT * FROM location_national_capital")
df = cur.fetchall()
location_national_capital = pd.DataFrame(df, columns=['country_id', 'latitude', 'longitude'])

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

for message in consumer:
    # Receive the message
    message_value = message.value
    # print(f"Original message: {message_value}")

    if "aml" in message_value:
        cur.execute(f"""
            SELECT client_id, SUM(amount), country_id 
            FROM aml_true 
            WHERE client_id = {message_value["client_id"]} 
            GROUP BY client_id, country_id
        """)
        dt = cur.fetchall()

        if dt:
            sum_amount = dt[0][1]
            country_id = dt[0][2]

            if message_value["aml"] + sum_amount > 0:
                # Use .loc with a boolean condition to get the correct row
                national_capital_row = location_national_capital.loc[location_national_capital['country_id'] == country_id]
                client_row = location_national_capital.loc[location_national_capital['country_id'] == message_value["country_id"]]

                if not national_capital_row.empty and not client_row.empty:
                    lon1, lat1 = national_capital_row.iloc[0][['longitude', 'latitude']]
                    lon2, lat2 = client_row.iloc[0][['longitude', 'latitude']]
                    distance = haversine(lat1, lon1, lat2, lon2)

                    if distance < 1300:
                        message_value["aml"] = 1
                    else:
                        message_value["aml"] = -1
                else:
                    print(f"Missing data for country_id {country_id} or client_id {message_value['client_id']}")
                    message_value["aml"] = 1  # Set aml to 1 if data is missing
            else:
                message_value["aml"] = -1
        else:
            print(f"No data found for client_id: {message_value['client_id']}")
            message_value["aml"] = 1  # Set aml to 1 if no data is found

        # Debug: Print modified message
        # print(f"Modified message: {message_value}")

        # Send the modified message to topic "aml"
        producer.send("aml", value=message_value)
        producer.flush()
    else:
        print("AML key is missing in the message")

# Close consumer and producer
consumer.close()
producer.close()