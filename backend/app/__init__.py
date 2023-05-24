# app.py
import mimetypes
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://posgresql:0000@localhost/lecarabin'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# the code below allows the js in our index.html file to be read properly
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')
app = Flask(__name__, static_url_path='',
            static_folder='templates', template_folder='templates')


@app.route("/")
def index():

    return render_template("index.html")


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
# Migrations
# To create the database tables, run the following command:
# flask db migrate

# To update the database tables, run the following command:
# flask db upgrade

if __name__ == "__main__":
    app.run()
