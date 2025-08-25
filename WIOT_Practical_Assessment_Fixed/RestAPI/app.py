from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Load DB connection details from environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "apiuser")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "apipass")
MYSQL_DB = os.getenv("MYSQL_DB", "webapi")

def get_db_connection():
    """Return a new MySQL connection with SSL disabled"""
    return mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        ssl_disabled=True  # disables SSL requirement
    )

@app.route('/log-ip', methods=['POST'])
def log_ip():
    try:
        client_ip = request.remote_addr
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert client IP into your table
        cursor.execute("INSERT INTO log_ips (ip_address) VALUES (%s)", (client_ip,))
        conn.commit()

        cursor.close()
        conn.close()
        return jsonify({"status": "success", "message": f"IP {client_ip} logged"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/')
def home():
    return "REST API is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
