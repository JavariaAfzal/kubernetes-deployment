
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = "/data/database.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    return jsonify({
        "service": "Database Microservice",
        "message": "SQLite database service is running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400

    conn = get_db_connection()

    try:
        cursor = conn.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (data["name"], data["email"])
        )
        conn.commit()

        return jsonify({
            "id": cursor.lastrowid,
            "name": data["name"],
            "email": data["email"]
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 409

    finally:
        conn.close()


@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    return jsonify([dict(user) for user in users])


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
