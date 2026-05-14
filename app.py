from flask import Flask, request, jsonify
import os
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        connect_timeout=5
    )

@app.route("/")
def home():
    return "Backend API Running!"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.route("/create-table")
def create_table():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(150),
            phone VARCHAR(50),
            company VARCHAR(150),
            service VARCHAR(100),
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        connection.commit()

        cursor.close()
        connection.close()

        return "Leads table created successfully!"

    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route("/api/leads", methods=["POST"])
def create_lead():
    try:
        data = request.json

        connection = get_connection()
        cursor = connection.cursor()

        sql = """
        INSERT INTO leads
        (name, email, phone, company, service, message)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            data.get("name"),
            data.get("email"),
            data.get("phone"),
            data.get("company"),
            data.get("service"),
            data.get("message")
        )

        cursor.execute(sql, values)
        connection.commit()

        lead_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return jsonify({
            "status": "success",
            "message": "Lead saved successfully",
            "lead_id": lead_id,
            "data": data
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/api/leads", methods=["GET"])
def get_leads():
    try:
        connection = get_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM leads ORDER BY id DESC")

        leads = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(leads)

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
