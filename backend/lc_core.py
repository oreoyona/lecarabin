from typing import Type
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from sqlalchemy import select

from models import Post

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}


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

    except Exception as e:

        write_log(e)


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