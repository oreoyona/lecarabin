from flask import Flask, request, redirect
from flask_ckeditor import CKEditor
from flask_cors import CORS
from models import db


app = Flask(__name__, static_url_path='',
            static_folder='templates/', template_folder='templates')

app.config.from_object('config.DevConfig')

app.config['DEBUG'] = True

app.config['CORS_HEADERS'] = 'Content-Type'

db.init_app(app)

CORS(app, resources={r"/api/*": {"origins": "*"}})

ckeditor = CKEditor(app)


@app.after_request
def after_request(response):

    response.headers['Access-Control-Allow-Methods'] = '*'

    response.headers['Access-Control-Allow-Origin'] = '*'

    response.headers['Vary'] = 'Origin'

    return response

# TODO: activate it in production
# @app.before_request
# def require_https():
#     url = request.url
#
#     if not request.is_secure:
#
#         url = request.url.replace("http://", "https://")
#
#     return redirect(url)
