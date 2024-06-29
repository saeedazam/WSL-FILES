from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rl(db.Model):
    __tablename__ = "rl"
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.String, nullable=False)
    peaking_rank = db.Column(db.String, nullable=False)
    rank_id = db.Column(db.Integer, nullable=False)
    users = db.relationship("Users", backref="rl", lazy=True)

    def add_user(self, username):
        u = Users(username=username, rank_id=self.id)
        db.session.add(u)
        db.session.commit()

class Users(db.Model):
    __tablename__ = "usernames"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("rl.id"), nullable=False)

    