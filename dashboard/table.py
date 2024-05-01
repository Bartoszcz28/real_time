from dash import Dash, dash_table
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import psycopg2
import time

time.sleep(30)

# Create a Dash application instance
app = Dash(__name__)

# Define the layout with the Interval and DataTable components
app.layout = html.Div(
    [
        dcc.Interval(
            id="interval-component",
            interval=1000,  # 10 seconds in milliseconds
            n_intervals=0,
        ),
        dash_table.DataTable(
            id="data-table",
            columns=[
                {"name": "First name", "id": "first_name", "type": "text"},
                {"name": "Last name", "id": "last_name", "type": "text"},
                {"name": "Email", "id": "email", "type": "text"},
                {"name": "Gender", "id": "gender", "type": "text"},
                {"name": "Time", "id": "time", "type": "datetime"},
                {"name": "Amount", "id": "amount", "type": "numeric"},
                {"name": "Country", "id": "country", "type": "text"},
            ],
            data=[],
            filter_action="native",
            style_table={
                "height": "auto",
                # 'overflowY': 'hidden',  # Enable vertical scrolling if needed ('hidden')
            },
            style_data={
                "whiteSpace": "normal",  # Wrap text in cells
                "height": "auto",
                "lineHeight": "15px",
            },
            page_size=25,  # Set number of rows per page
            editable=False,  # Disable cell editing
        ),
    ]
)


# Define the callback function to update the DataTable
@app.callback(
    Output("data-table", "data"), [Input("interval-component", "n_intervals")]
)
def update_data(n):
    conn = psycopg2.connect(
        host="postgres",
        database="postgres",
        user="postgres",
        password="postgres",
        port="5432",
    )
    cur = conn.cursor()

    cur.execute(
        """
        SELECT first_name, last_name, email, gender, time, amount, country 
        FROM customer_dim c
        JOIN messages m ON c.customer_id = m.client_id
        JOIN country co ON c.country_id = co.country_id;
    """
    )

    rows = cur.fetchall()
    columns = [
        "first_name",
        "last_name",
        "email",
        "gender",
        "time",
        "amount",
        "country",
    ]
    df = pd.DataFrame(rows, columns=columns)

    cur.close()
    conn.close()

    return df.to_dict("records")


# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
