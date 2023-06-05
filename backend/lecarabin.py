"""The entry point of lecarabin"""
import mimetypes

import requests
from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from models import db, User, Post, Image
from flask_ckeditor import CKEditor
import os

app = Flask(__name__, static_url_path='', static_folder='templates/', template_folder='templates')
app.config.from_object('config.devConfig')
ckeditor = CKEditor(app)

db.init_app(app)
migrate = Migrate(app=app, db=db)
#############################################################################
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')


############################################################################

#############################################################################
# Routes config
#############################################################################
@app.route("/")
def go_to_home():
  return render_template('index.html')


@app.route("/dashboard")
def go_to_admin():
  return render_template('admin.html', title="Dashboard")


@app.route("/npost", methods=["GET", "POST"])
def image_upload():
  if requests.method == 'POST':
    file = requests.files['files']
    if file is None:
      redirect(requests.url)

    if file.filename == '':
      pass


if __name__ == "__main__":
  app.run(debug=True)
