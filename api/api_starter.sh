#!/bin/bash

# # Czekaj na dostępność bazy danych
# while ! nc -z postgres 5432; do
#   sleep 1
# done

sleep 30

# Uruchom aplikację
python main.py