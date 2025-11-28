import time
import redis
import psycopg2
from flask import Flask

app = Flask(__name__)

cache = redis.Redis(host='cache', port=6379)

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host="db",
                database="postgres",
                user="postgres",
                password="password"
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    return None

@app.route('/')
def index():
    count = cache.incr('hits')

    conn = get_db_connection()
    db_status = "Conectado ao Postgres" if conn else "Falha ao conectar no DB"
    if conn: conn.close()

    return f"Desafio 3: Web Services.<br>Visitas (Cache): {count}<br>Database: {db_status}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)       