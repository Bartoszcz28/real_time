import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import threading
import datetime
from kafka import KafkaConsumer
from json import loads

# Global variable to store data
data = []

# Kafka Consumer Configuration
consumer = KafkaConsumer(
    "aml",
    bootstrap_servers=["broker:9092"],
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="bootstrap-server3",
    value_deserializer=lambda x: loads(x.decode("ISO-8859-1")),
)

# Function to consume data from Kafka
def consume_kafka():
    global data
    for message in consumer:
        message_value = message.value
        data.append(message_value)

# Start Kafka consumer in a separate thread
thread = threading.Thread(target=consume_kafka)
thread.daemon = True
thread.start()

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Kafka Data Dashboard"),
        html.Div(
            style={"display": "flex"},
            children=[
                dcc.Graph(id="live-update-graph", style={"flex": "50%"}),
                dcc.Graph(id="live-update-pie", style={"flex": "50%"}),
            ],
        ),
        html.Div(
            style={"display": "flex"},
            children=[
                dcc.Graph(id="live-update-country-bar", style={"flex": "50%"}),
                dcc.Graph(id="live-update-amount-hist", style={"flex": "50%"}),
            ],
        ),
        dcc.Interval(
            id="interval-component", interval=1 * 1000, n_intervals=0  # in milliseconds
        ),
    ]
)

def filter_recent_data(data, window_minutes=10):
    current_time = datetime.datetime.utcnow()
    window_start = current_time - datetime.timedelta(minutes=window_minutes)
    return [msg for msg in data if datetime.datetime.strptime(msg["time"], "%Y-%m-%d %H:%M:%S.%f") >= window_start]

@app.callback(
    Output("live-update-graph", "figure"), [Input("interval-component", "n_intervals")]
)
def update_graph_live(n):
    global data
    recent_data = filter_recent_data(data)
    timestamps = [
        datetime.datetime.strptime(msg["time"], "%Y-%m-%d %H:%M:%S.%f") for msg in recent_data
    ]
    amounts = [msg["amount"] for msg in recent_data]

    fig = go.Figure(
        data=[go.Scatter(x=timestamps, y=amounts, mode="markers")],
        layout=go.Layout(
            title="Live Data from Kafka",
            xaxis=dict(title="Time"),
            yaxis=dict(title="Amount"),
        ),
    )

    return fig

@app.callback(
    Output("live-update-pie", "figure"), [Input("interval-component", "n_intervals")]
)
def update_pie_chart(n):
    global data
    recent_data = filter_recent_data(data)
    aml_counts = {1: 0, -1: 0}
    for msg in recent_data:
        aml_value = msg.get("aml", None)
        if aml_value in aml_counts:
            aml_counts[aml_value] += 1

    labels = ['AML = 1', 'AML = -1']
    values = [aml_counts[1], aml_counts[-1]]

    fig = go.Figure(
        data=[go.Pie(labels=labels, values=values)],
        layout=go.Layout(
            title="AML Transaction Ratio (Last 10 minutes)"
        )
    )

    return fig

@app.callback(
    Output("live-update-country-bar", "figure"), [Input("interval-component", "n_intervals")]
)
def update_country_bar_chart(n):
    global data
    recent_data = filter_recent_data(data)
    country_counts = {}
    for msg in recent_data:
        country = msg.get("country", "Unknown")
        country_counts[country] = country_counts.get(country, 0) + 1

    countries = list(country_counts.keys())
    counts = list(country_counts.values())

    fig = go.Figure(
        data=[go.Bar(x=countries, y=counts)],
        layout=go.Layout(
            title="Transactions by Country (Last 10 minutes)",
            xaxis=dict(title="Country"),
            yaxis=dict(title="Count"),
        ),
    )

    return fig

@app.callback(
    Output("live-update-amount-hist", "figure"), [Input("interval-component", "n_intervals")]
)
def update_amount_histogram(n):
    global data
    recent_data = filter_recent_data(data)
    amounts = [msg["amount"] for msg in recent_data]

    fig = go.Figure(
        data=[go.Histogram(x=amounts)],
        layout=go.Layout(
            title="Transaction Amount Distribution (Last 10 minutes)",
            xaxis=dict(title="Amount"),
            yaxis=dict(title="Count"),
        ),
    )

    return fig

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4040, debug=True)