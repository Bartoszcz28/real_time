from flask import Flask, request, jsonify
import psycopg2
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

cur = conn.cursor()

app = Flask(__name__)


@app.route("/get-user/<user_id>")
def home(user_id):

    cur.execute(f"""Select SUM(amount) FROM messages WHERE client_id ={user_id};""")

    user_data = {
        "user_id": user_id,
        "amount": cur.fetchall()[0][0],
    }

    conn.commit()

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("FLASK_SERVER_PORT", 5000)))
