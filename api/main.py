from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import extras
import os
import time

time.sleep(30)

conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432",
)
cur = conn.cursor(cursor_factory=extras.RealDictCursor)

app = Flask(__name__)


@app.route("/get-user/<user_id>")
def home(user_id):
    cur.execute(
        f"""
    SELECT first_name, last_name, email, gender, time, amount, country 
        FROM customer_dim c
        JOIN messages m ON c.customer_id = m.client_id
        JOIN country co ON c.country_id = co.country_id
        WHERE client_id ={user_id};"""
    )

    user_data = cur.fetchall()

    conn.commit()

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("FLASK_SERVER_PORT", 5000)))
