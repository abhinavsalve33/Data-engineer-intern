# Generated from: main.ipynb
# Converted at: 2026-04-06T13:31:04.106Z
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

app = Flask(__name__)

@app.route('/')
def home():
    return "API is running 🚀"

@app.route('/jobs')
def get_jobs():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="HackerDB1"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hackernews_data LIMIT 50")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)