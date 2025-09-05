from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()  # Load environment variables from .env file
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        cursor_factory=RealDictCursor
    )


@app.get("/isbooked")
def read_isbooked():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT isbooked AS \"IsBooked\" FROM couch;")
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        # results will be a list of dicts: [{'IsBooked': value}, ...]
        return {"IsBooked": [row["IsBooked"] for row in results]}

    except Exception as e:
        return {"error": str(e)}