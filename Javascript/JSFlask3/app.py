import os

import requests

from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "mysecretkey") 
socketio = SocketIO(app)

votes = {"yes": 0, "no": 0, "maybe": 0}

@app.route('/')
def index():
    return render_template("index.html", votes=votes)

@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    votes[selection] += 1
    emit("Total Votes", votes, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)
