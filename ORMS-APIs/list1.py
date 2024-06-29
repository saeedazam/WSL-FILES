import os

from flask import Flask, render_template, request
from models import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DB_PATH = "test.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getenv('DB_PATH', '/home/deeznuts/ORMS-APIs/test.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    rl = Rl.query.all()
    if rl:
        print(f"rank is: {rl.rank}, peaking rank is: {rl.peaking_rank}, and rank id is: {rl.rank_id}")
    else:
        print("No record found. Try again.")

if __name__ == "__main__":
    with app.app_context():
        main()
