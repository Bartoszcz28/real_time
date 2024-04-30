import datetime
import dash
from dash import Dash, dcc, html, Input, Output
import psycopg2

import time

time.sleep(30)

# Create a connection to a PostgreSQL database
conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432",
)
cur = conn.cursor()

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

# Define app layout with placeholders for displaying time and transaction count
app.layout = html.Div(
    [
        html.H1(id="live-update-text", style={"textAlign": "center"}),
        html.H1(id="live-update-count", style={"textAlign": "center"}),
        dcc.Interval(
            id="interval-component", interval=1000, n_intervals=0  # in milliseconds
        ),
    ]
)


# Callback to update the live time and transaction count
@app.callback(
    [Output("live-update-text", "children"), Output("live-update-count", "children")],
    [Input("interval-component", "n_intervals")],
)
def update_metrics(n):
    # Update live time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_output = f"The time is: {current_time}"

    # Update transaction count
    cur.execute("SELECT COUNT(*) FROM messages;")
    transaction_count = cur.fetchone()[0]
    count_output = f"Number of transactions: {transaction_count}"

    return time_output, count_output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
