"""Server for antHiveConnect app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
# from oauthlib.oauth2 import WebApplicationClient
import requests
import os
import json
import crud
from datetime import time, date, datetime, timedelta
# import humanize
import datetime as dt


from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY", None)
app.jinja_env.undefined = StrictUndefined


@app.route("/friends")
def friends():
    """View friends."""

    return {"friends": ["Friend1", "Friend2", "Friend3"]}


@app.route("/register")
def register():
    """View Signup form."""

    return {"friends": ["Friend1", "Friend2", "Friend3"]}


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)
