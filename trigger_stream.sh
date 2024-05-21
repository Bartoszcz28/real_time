#!/bin/bash

sleep 20

cd ~

kafka/bin/kafka-topics.sh --bootstrap-server broker:9092 --create --topic streaming
kafka/bin/kafka-topics.sh --bootstrap-server broker:9092 --create --topic aml

python notebooks/create_pg_db.py & 

sleep 10

python notebooks/kafka_pg.py & python notebooks/random_generator.py & python3 notebooks/aml.py & python notebooks/dashboard_asyn.py &