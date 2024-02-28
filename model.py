"""Models for antHiveConnect app."""

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

db = SQLAlchemy()


def connect_to_db(flask_app, db_uri="postgresql:///antHiveConnect", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


class User(db.Model):
    """A user data."""

    __tablename__ = "user_data"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False)
    user_password = db.Column(db.String)
    avatar_url = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    register_date = db.Column(db.Date)
    country = db.Column(db.String)
    city = db.Column(db.String)

    
    
    def __repr__(self):
        return f"{self.user_name}"


class UserMessages(db.Model):
    """User messages."""

    __tablename__ = "user_messages"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_receiver_id = db.Column(db.Integer, db.ForeignKey("user_data.user_id"))
    user_sender_id = db.Column(db.Integer, db.ForeignKey("user_data.user_id"))
    message = db.Column(db.String)
    date = db.Column(db.Date)
    status = db.Column(db.String)


class UserPosts(db.Model):
    """User posts."""

    __tablename__ = "user_posts"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_data.user_id"))
    text = db.Column(db.String)


class Friends(db.Model):
    """A friends data."""

    __tablename__ = "friends"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_data.user_id"))
    friend_id = db.Column(db.Integer, db.ForeignKey("user_data.user_id"))
    status_acceptance = db.Column(db.Boolean)

    # user = db.relationship('User', back_populates="friends")

    def __repr__(self):
        return f"<Friend user_id={self.user_id} friend_id={self.friend_id} status={self.status_acceptance}>"


class FriendRequest(db.Model):
    """Friend request data."""
    __tablename__ = "friend_request"

    user_receiver_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_sender_id = db.Column(db.Integer, db.ForeignKey(
        "user_data.user_id"), primary_key=True)
    friendship_status = db.Column(db.Boolean)
    friendship_start_date = db.Column(db.Date)
    request_status = db.Column(db.String)





Posts: id, date, user id, text, image url, status (posted, deleted, edited).

Likes: id, date, post_id, user_id, number.+

Dislike: id, date, post_id, user_id, number.-

Adding friend: id, user_receiver_id, user_sender id, status, friend_request id.

Removing friend:  id, user_receiver_id, user_sender id, status, friend_request id.

Blocking friend:  id, user_receiver_id, user_sender id, status, friend_request id.

avatar pics: id, user_id, url.










if __name__ == "__main__":
    from server import app
    connect_to_db(app)

    with app.app_context():
        db.create_all()
        example_data()
