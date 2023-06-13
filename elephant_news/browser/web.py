from enum import Enum, auto
import glob
from pathlib import Path
from flask import Flask, request, jsonify
import logging


app = Flask(__name__) #,  static_url_path="/plugin", static_folder='../plugin')

@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def static_file(path):
    path1 = app.instance_path
    return app.send_static_file(path)


@app.route("/ask", methods=["POST"])

# message / reply format
@app.route("/chat", methods=["POST", "GET"])
def chat():
    message = request.json["message"]
    return {"reply": "Message Received!" + message}


@app.route("/sendpage", methods=["POST", "GET"])
def semdpage():
    doc = request.json["message"]
    url = doc['url']
    title = doc['title']
    body = doc['body']

    return {"reply": "Analysis Complete!"}
