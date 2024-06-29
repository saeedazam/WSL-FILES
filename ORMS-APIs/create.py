from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Rl, Users
import os

app = Flask(__name__)
DB_PATH = "test.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getenv('DB_PATH', '/home/deeznuts/ORMS-APIs/test.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    try:
        with app.app_context():
            print("Calling db.create_all()")
            db.create_all()
            print("Tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")

if __name__ == "__main__":
        main()
