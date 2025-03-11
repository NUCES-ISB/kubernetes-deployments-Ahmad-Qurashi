from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.close()
        return "Connected to PostgreSQL!"
    except Exception as e:
        return f"Database connection error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
