import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import asyncio
from kafka import KafkaConsumer
from json import loads
import threading
import datetime
import time

time.sleep(70)

# Global variable to store data
data = []

# Kafka Consumer Configuration
consumer = KafkaConsumer(
    "aml",
    bootstrap_servers=["broker:9092"],
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="bootstrap-server",
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

app.layout = html.Div(children=[
    html.H1(children='Kafka Data Dashboard'),
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    global data
    # Convert data to DataFrame if needed, here we just use it as is
    timestamps = [datetime.datetime.strptime(msg['time'], '%Y-%m-%d %H:%M:%S.%f') for msg in data]
    amounts = [msg['amount'] for msg in data]
    
    fig = go.Figure(
        data=[
            go.Scatter(
                x=timestamps,
                y=amounts,
                mode='markers' # lines+markers
            )
        ],
        layout=go.Layout(
            title='Live Data from Kafka',
            xaxis=dict(title='Time'),
            yaxis=dict(title='Amount')
        )
    )

    return fig

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4040, debug=True)