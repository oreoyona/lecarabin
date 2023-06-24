"""The entry point of lecarabin"""
from api.api import *

import mimetypes

from flask_migrate import Migrate

from base import app, db

import routes

from api.api import *

migrate = Migrate(app=app, db=db)

#############################################################################

mimetypes.add_type('application/javascript', '.js')

mimetypes.add_type('text/css', '.css')


#############################################################################

if __name__ == "__main__":
    
    app.run()
