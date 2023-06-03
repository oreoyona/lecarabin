"""The entry point of lecarabin"""
import mimetypes
from flask import Flask, render_template
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from models import db, User, Post, Image
from forms import *
from flask_ckeditor import CKEditor
from views import ImageView
app = Flask(__name__, static_url_path='', static_folder='templates/', template_folder='templates')
app.config.from_object('config.devConfig')
ckeditor = CKEditor(app)

db.init_app(app)
migrate = Migrate(app=app, db=db)
# admin = Admin(app)
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Post, db.session))
# admin.add_view(ImageView(Image, db.session))
# the code below allows the js in our index.html file to be read properly####
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


if __name__ == "__main__":
    app.run()
