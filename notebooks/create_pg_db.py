import psycopg2

conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432",
)

cur = conn.cursor()

# -- Drop the 'messages' table if it exists
cur.execute("DROP TABLE IF EXISTS messages;")

# -- Create the 'messages' table
cur.execute(
    """CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    time TIMESTAMP,
    message_id VARCHAR(255),
    client_id INTEGER,
    amount INTEGER);"""
)

conn.commit()

cur.close()
conn.close()
