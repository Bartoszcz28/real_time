#!/bin/bash

sleep 30

cd ~

kafka/bin/kafka-topics.sh --bootstrap-server broker:9092 --create --topic streaming

python notebooks/kafka_pg.py & python notebooks/random_generator.py &
