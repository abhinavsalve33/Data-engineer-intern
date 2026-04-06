# Generated from: main.ipynb
# Converted at: 2026-04-06T13:58:52.508Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# 0 3 * * * python run_pipeline.py

# # !pip install fastapi uvicorn
# # !pip install psycopg2-binary
# from fastapi import FastAPI
# import psycopg2

# app = FastAPI()

# @app.get("/jobs")
# def get_jobs():

#     conn = psycopg2.connect(
#         host="localhost",
#         database="HackerDB1",
#         user="root",
        # password="root"/
#     )

#     cur = conn.cursor()

#     cur.execute("SELECT * FROM hackernews_data LIMIT 50")

#     rows = cur.fetchall()

#     cur.close()
#     conn.close()

#     return rows

from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "API is running 🚀"

@app.route('/jobs')
def get_jobs():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hackernews_data LIMIT 50")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)