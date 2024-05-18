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

result = pd.merge(person, country, how="inner", on=["country_id", "country_id"])
result = pd.merge(result, atm, how="inner", on=["country_id", "country_id"])

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

            # Losowy wybór klienta z DataFrame result
            client_id = random.choice(result["customer_id"].unique())

            # Wybór wierszy z DataFrame result odpowiadających wybranemu klientowi
            customer_info = result[result["customer_id"] == client_id].iloc[0]

            message = {
                "time": str(t),
                "message_id": int(message_id),  # Konwersja na int
                "client_id": int(client_id),  # Konwersja na int
                "amount": int(random.randint(-1000, 1000)),  # Konwersja na int
                "first_name": str(customer_info["first_name"]),
                "last_name": str(customer_info["last_name"]),
                "email": str(customer_info["email"]),
                "gender": str(customer_info["gender"]),
                "country_id": int(customer_info["country_id"]),  # Konwersja na int
                "country": str(customer_info["country"]),
                "capital": str(customer_info["capital"]),
                "atm_id": int(customer_info["atm_id"]),  # Konwersja na int
                "atm_number": str(customer_info["atm_number"]),
                "aml": int(0),
            }

            producer.send("streaming", value=message)
            sleep(1)

    except KeyboardInterrupt:
        producer.close()
