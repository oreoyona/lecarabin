"""The entry point of lecarabin"""


import mimetypes
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_migrate import Migrate
from sqlalchemy import select

from forms import ArticleForm, AsideArticleForm, CategoryForm
from models import db, Post, Category
from flask_ckeditor import CKEditor
import os
from werkzeug.utils import secure_filename
from config import UPLOAD_IMAGE_PATH

app = Flask(__name__, static_url_path='', static_folder='templates/', template_folder='templates')

app.config.from_object('config.devConfig')

app.config['DEBUG'] = True

ckeditor = CKEditor(app)

db.init_app(app)

migrate = Migrate(app=app, db=db)

#############################################################################

mimetypes.add_type('application/javascript', '.js')

mimetypes.add_type('text/css', '.css')


############################################################################


#############################################################################
# Routes config

@app.route("/")
def go_to_home():

    """Defines the home route"""

    return render_template('index.html')


@app.route("/dashboard")
def go_to_admin():

    articles = Post.query.all()

    return render_template('admin.html', title="Dashboard", articles=articles)


@app.route("/new-article", methods=['GET', 'POST'])
def go_to_new_article():

    """Defines the new article route"""

    form = ArticleForm()

    if request.method == "POST":

        if form.validate_on_submit():

            filename = secure_filename(form.image_banner.data.filename)

            post = Post(

              title=form.title.data,

              content=form.content.data,

              image_banner=UPLOAD_IMAGE_PATH + filename)
            try:

                db.session.add(post)

                db.session.commit()

                form.image_banner.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                flash("The article was successfully published")
            except Exception as e:

                flash("Something went wrong, please try later")

            finally:

                db.session.close()

        return redirect(url_for('go_to_new_article'))

    return render_template('pages/new-article.html', form=form)


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def go_to_edit(post_id):

    """Defines the edit-post route"""

    article = db.get_or_404(Post, int(post_id))

    form = ArticleForm()

    aside_form = AsideArticleForm()
    
    cat_form = CategoryForm()
    
    catergories = db.session.execute(select(Category).order_by(Category.name)).scalars()
    
    cat_choices = []
    
    for el in catergories:
        cat_choices.append((el, el))
        
    aside_form.category.choices = cat_choices

    if article:

        form = ArticleForm(title=article.title, content=article.content, image_banner=article.image_banner)

    if request.method == "POST" and form.validate_on_submit() and aside_form.validate_on_submit():

        filename = secure_filename(form.image_banner.data.filename)

        image_banner = UPLOAD_IMAGE_PATH + filename

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        try:

            if os.path.exists(filepath):

                article.title = form.title.data

                article.content = form.content.data

                article.update()

            else:

                article.title = form.title.data

                article.content = form.content.data

                article.image_banner = image_banner

                form.image_banner.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                article.update()

                flash("The article was updated")

        except Exception as e:
        #//TODO: send every error in a log file

            flash("Something wrong happened, try later")

        finally:

            db.session.close()

            return redirect(url_for('go_to_edit', post_id=1))

    return render_template('pages/edit-article.html', article=article, form=form, aside_form=aside_form, cat_form=cat_form)


if __name__ == "__main__":

    app.run()
