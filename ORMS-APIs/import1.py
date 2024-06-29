import os
import csv

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
DB_PATH = "test.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getenv('DB_PATH', '/home/deeznuts/ORMS-APIs/test.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("RL.csv")
    reader = csv.reader(f)
    for rank, peaking_rank, rank_id in reader:
        rl = Rl(rank=rank, peaking_rank=peaking_rank, rank_id=rank_id)
        db.session.add(rl)
        print(f"Added rank {rank} with peaking rank {peaking_rank} and the rank id of {rank_id}.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
