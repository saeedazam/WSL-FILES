from flask import Flask, render_template, request, redirect, url_for
from models import *
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
DB_PATH = "test.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getenv('DB_PATH', '/home/deeznuts/ORMS-APIs/test.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    rls = Rl.query.all()
    return render_template("index.html", rls=rls)

@app.route("/book", methods=["POST"])
def book():
    """Book A rank."""

    name = request.form.get("username")
    try:
        rank_id = int(request.form.get("rank_id"))
    except ValueError:
        return render_template("error.html", message="Invalid rank id.")

    rl = Rl.query.get(rank_id)
    if rl is None:
        return render_template("error.html", message="No such rank with that id.")

    user = Users(username=name, rank_id=rank_id)
    db.session.add(user)
    db.session.commit()
    return render_template("success.html")


@app.route("/ranks")
def ranks():
    """Lists of all ranks."""
    rls = Rl.query.all()
    return render_template("rls.html", rls=rls)

@app.route("/ranks/<int:rank_id>")
def rank():
    """Details about this"""

    rl = Rl.query.get(rank_id)
    if rl is None:
        return render_template("error.html", message="No such rank id.")

    users = Users.query.filter_by(rank_id=rank_id).all()
    return render_template("rls.html", rl=rl, users=users)
