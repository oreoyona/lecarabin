from . import app
from . models import db, User
from flask import request, render_template, redirect, url_for


@app.route("/")
def go_to_home():
    return render_template('index.html')
