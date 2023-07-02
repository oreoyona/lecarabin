from functools import wraps
import random
import string
from typing import Type
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from sqlalchemy import select
from flask_login import current_user
from models import Post, User
from flask import abort, redirect, url_for

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}

ROLES = {
    'admin': 0,
    'editor': 1,
    'user': 2
}

ACCESS_LEVELS = {
    'admin': ['admin', 'editor', 'user'],
    'editor': ['editor', 'user'],
    'user': ['user']
}

def save_to_db(dbs: SQLAlchemy, data: Type[Model | Post]):
    """Saves the model data to the database"""

    dbs.session.add(data)

    dbs.session.commit()


def write_log(e: Exception):
    """ Writes an exception to the log file"""

    with open('./lc_contents/data_logs/', 'a') as log_file:

        log_file.write(f"An error occurred: ")

        log_file.write(f"{e}")


def save_new_data(model: Type[Model or Post], dbs: SQLAlchemy):
    """ Saves the data from a form to the database"""

    try:
        save_to_db(dbs, model)

        return 0

    except Exception as e:

        write_log(e)

        return -1


def delete_from_db(dbs: SQLAlchemy, model: Type[Model | Post]):
    """ Deletes the model from the database"""

    dbs.session.delete(model)

    dbs.session.commit()

    dbs.session.close()


def data_formater(data):
    """ Formats the data by sorting it """

    results = []

    for post in data:

        dict_data = {
            'title': post.title,
            'content': post.content,
            'category': post.category,
            'date': post.created_at,
            'author': post.author,
            'tag': post.tag,
            'image_banner': post.image_banner
        }

        results.append(dict_data)

    return results


def get_data_from_db(dbs: SQLAlchemy, model: Type[Model | Post]):
    """ Get all the models inside a dbs"""

    return dbs.session.execute(select(model).order_by(model.id)).scalars()


def get_formated_data_from_db(dbs: SQLAlchemy, model: Type[Model | Post]):
    """ Get all the models inside a dbs and returns a formated response of it"""

    return data_formater(get_data_from_db(dbs, model))


def find_datum(dbs: SQLAlchemy, model: Type[Model | Post], model_id: int):
    """ finds an article from the database using the id of the article"""

    return dbs.get_or_404(model, model_id)

def find_user(dbs: SQLAlchemy, identifier: str):
    """ finds a user by email from the databse """

    return dbs.session.query(User).filter_by(email=identifier).first()


def role_required(role):
    """ Decorator function to check and require role of the user"""

    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            """ Checks if the user is authenticated"""

            if not current_user.is_authenticated:
                return redirect(url_for('login'))

            if current_user.role not in ACCESS_LEVELS[role]:
                abort(403)
            return fn(*args, **args)

        return decorated_view

    return wrapper


def check_pwd(pwd:str, pwd2: str):
  """ Checks if two given password are the same"""

  if pwd == pwd2:

    return pwd

  return None


def generate_username(name: str):
    """Generates a username based on the provided name"""
    # Split the name into words
    words = name.split()

    # Combine the first letter of each word into a string
    initials = ''.join([word[0] for word in words])

    # Generate a random string of alphanumeric characters
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    # Combine the initials and random characters to form the username
    username = initials + random_chars

    # Truncate the username to a maximum of 10 characters
    username = username[:10]

    return username
