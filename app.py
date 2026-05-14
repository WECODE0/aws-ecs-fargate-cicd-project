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

@app.route("/db-test")
def db_test():
    try:
        connection = pymysql.connect(
            host=os.environ["DB_HOST"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            database=os.environ["DB_NAME"],
            connect_timeout=5
        )
        connection.close()
        return "RDS Connected Successfully!"
    except Exception as e:
        return f"RDS Connection Failed: {str(e)}", 500
