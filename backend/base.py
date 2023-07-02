from flask import Flask, request, g
from flask_ckeditor import CKEditor
from flask_cors import CORS
from flask_login import LoginManager, current_user
from models import User, db


app = Flask(__name__, static_url_path='',
            static_folder='templates/', template_folder='templates')

app.config.from_object('config.DevConfig')

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'loginUser'

login_manager.session_protection = "strong"

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))

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


@app.before_request
def before_request():
    g.current_user = current_user
