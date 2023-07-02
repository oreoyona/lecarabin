"""The entry point of lecarabin"""

import mimetypes

from flask_migrate import Migrate

from flask_minify import Minify

from base import app, db

import routes

from api.api import *

app.register_blueprint(api_bp)

migrate = Migrate(app=app, db=db)

Minify(app=app, html=True, js=True, cssless=True  )
#############################################################################

mimetypes.add_type('application/javascript', '.js')

mimetypes.add_type('text/css', '.css')


#############################################################################

if __name__ == "__main__":

    # TODO: run this config in production
    # app.run(ssl_context=('cert.pem', 'key.pem'))
    app.run()
