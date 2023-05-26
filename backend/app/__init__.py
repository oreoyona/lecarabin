# app.py
import mimetypes
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
from . import config
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# the code below allows the js in our index.html file to be read properly####
#############################################################################
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

############################################################################
app = Flask(__name__, static_url_path='',
            static_folder='templates', template_folder='templates')


from . import routes
from . import models


if __name__ == "__main__":
    app.run()
