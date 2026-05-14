from flask import Flask
import os
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Pipeline Working!"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.route("/create-db")
def create_db():
    try:
        connection = pymysql.connect(
            host=os.environ["DB_HOST"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            connect_timeout=5
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS appdb")
        connection.commit()
        cursor.close()
        connection.close()
        return "Database appdb created successfully!"
    except Exception as e:
        return f"Create DB Failed: {str(e)}", 500
