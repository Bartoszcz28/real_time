import pandas as pd
import numpy as np

import json
import random
import sys
from datetime import datetime, timedelta
from time import sleep
from kafka import KafkaProducer

sleep(20)

atm = pd.read_csv("notebooks/data/atm.csv")
country = pd.read_csv("notebooks/data/country.csv")
person = pd.read_csv("notebooks/data/person.csv")

result = pd.merge(atm, country, how="inner", on=["country_id", "country_id"])

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
            t = datetime.now()  # + timedelta(seconds=random.randint(-15, 0))

            # Random customer selection from DataFrame person
            client_id = random.choice(person["customer_id"].unique())

            # Selecting rows from the DataFrame result corresponding to the selected client
            customer_info = result.sample(n=1).iloc[0]

            # Selecting a row from the DataFrame person corresponding to the selected client
            person_info = person[person["customer_id"] == client_id].iloc[0]

            message = {
                "time": str(t),
                "message_id": int(message_id),  # Conversion to int
                "client_id": int(client_id),  # Conversion to int
                "amount": int(random.randint(-1000, 1000)),  # Conversion to int
                "first_name": str(person_info["first_name"]),
                "last_name": str(person_info["last_name"]),
                "email": str(person_info["email"]),
                "gender": str(person_info["gender"]),
                "country_id": int(customer_info["country_id"]),  # Conversion to int
                "country": str(customer_info["country"]),
                "capital": str(customer_info["capital"]),
                "atm_id": int(customer_info["atm_id"]),  # Conversion to int
                "atm_number": str(customer_info["atm_number"]),
                "aml": int(0),
            }

            producer.send("streaming", value=message)
            sleep(1)

    except KeyboardInterrupt:
        producer.close()
