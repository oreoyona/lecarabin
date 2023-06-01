# app.py
import mimetypes
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from models import db
from config import devConfig


app = Flask(__name__, static_url_path='', static_folder='templates', template_folder='templates')
app.config.from_object('config.devConfig')

db.init_app(app)
migrate = Migrate(app=app, db=db)

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
    render_template('index.html')



with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)
