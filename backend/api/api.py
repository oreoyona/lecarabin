import datetime
from flask import jsonify, Blueprint, request
from flask_cors import cross_origin
from models import Post

from base import db
from lc_core import get_formated_data_from_db, find_datum, delete_from_db, write_log, save_new_data

api_bp = Blueprint('api', __name__)


@api_bp.route('/api/articles', methods=["GET"])
@cross_origin()
def get_api_articles():
    """ Sends all the article inside the database"""

    articles = get_formated_data_from_db(dbs=db, model=Post)

    if not articles:
        return jsonify({
            'message': 'No articles found',

            'code': 404
        })

    return articles, 200


@api_bp.route('/api/edit-article/<model_id>', methods=["DELETE"])
@cross_origin()
def delete_api_article(model_id):
    """ Deletes an article from the database using an id"""

    article = find_datum(model_id=model_id, dbs=db, model=Post)

    if not article:
        return jsonify({
            'message': 'Article not found',

            'code': 404
        })

    try:
        delete_from_db(db, article)

        return jsonify({
            'message': 'Deleted',

            'code': 201
        })

    except Exception as e:

        write_log(e)

        return jsonify({
            'message': "An error occured",

            'code': 500
        })


@api_bp.route('/api/create-article', methods=["POST"])
@cross_origin()
def create_api_article():
    """ Creates an article in the database"""

    if request.method == "POST":
        data = request.json

        if not data:
            return jsonify({
                'message': 'No data provided',

                'code': 400
            })

        if not data['title'] or not data['content']:
            return jsonify({
                'message': 'Title and content are required',

                'code': 400
            })

        new_article = Post(
            title=data['title'],
            content=data['content'],
            created_at=datetime.datetime.utcnow(),
            image_banner=data['image_banner'],
            category=data['category'],
            tag=data['tag'],
            author=data['author']
        )

        save_new_data(dbs=db, model=new_article)

        return jsonify({
            'message': 'Created',

            'code': 201
        })

    else:
        return jsonify({
            'message': 'Invalid request method',

            'code': 405
        })


@api_bp.route('/api/edit-article/<model_id>', methods=["PUT"])
@cross_origin()
def edit_api_article(model_id):
    """ Edits an article in the database"""

    if request.method == "PUT":

        data = request.json

        if not data:

            return jsonify({
                'message': 'No data provided',

                'code': 400
            })

        article = find_datum(model_id=model_id, dbs=db, model=Post)

        if not article:
            return jsonify({
                'message': 'Article not found',

                'code': 404
            })

        article.title = data['title'] if 'title' in data else article.title

        article.content = data['content'] if 'content' in data else article.content

        article.image_banner = data['image_banner'] if 'image_banner' in data else article.image_banner

        article.category = data['category'] if 'category' in data else article.category

        article.tag = data['tag'] if 'tag' in data else article.tag
