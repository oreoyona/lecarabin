import os
from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_user
from sqlalchemy import select
from base import app, db
from forms import ArticleForm, AsideArticleForm, CategoryForm, LoginUserForm
from lc_core import find_user, save_to_db, write_log, save_new_data, get_formated_data_from_db

from config import UPLOAD_IMAGE_PATH
from werkzeug.utils import secure_filename
from models import *



@app.route("/")
def go_to_home():
    """Defines the home route"""

    return render_template('index.html')


@app.route("/admin/dashboard")
def go_to_admin():
    articles = Post.query.all()

    return render_template('admin.html', title="Dashboard", articles=articles)


@app.route("/admin/new-article", methods=['GET', 'POST'])
def go_to_new_article():
    """Defines the new article route"""

    form = ArticleForm()

    aside_form = AsideArticleForm()

    cat_form = CategoryForm()

    authors = db.session.execute(select())

    if request.method == "POST":

        if form.validate_on_submit():

            filename = secure_filename(form.image_banner.data.filename)

            post = Post(

                title=form.title.data,

                content=form.content.data,

                image_banner=UPLOAD_IMAGE_PATH + filename)
            try:

                save_to_db(db, post)

                form.image_banner.data.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], filename))

                flash("The article was successfully published")
            except Exception as e:

                flash("Something went wrong, please try later")

                write_log(e)

            finally:

                db.session.close()

        return redirect(url_for('go_to_new_article'))

    return render_template('pages/new-article.html', form=form, cat_form=cat_form, aside_form=aside_form)


@app.route("/admin/edit-post/<post_id>", methods=["GET", "POST"])
def go_to_edit(post_id):
    """Defines the edit-post route"""

    article = db.get_or_404(Post, int(post_id))

    form = ArticleForm()

    aside_form = AsideArticleForm()

    cat_form = CategoryForm()

    catergories = db.session.execute(
        select(Category).order_by(Category.name)).scalars()

    cat_choices = []

    tags = db.session.execute(select(Post.tag)).scalars()

    for el in catergories:
        cat_choices.append((el, el))

    aside_form.category.choices = cat_choices

    if article:
        form = ArticleForm(
            title=article.title, content=article.content, image_banner=article.image_banner)

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

                form.image_banner.data.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], filename))

                article.update()

                flash("The article was updated")

        except Exception as e:

            flash("Something wrong happened, try later")

            write_log(e)

        finally:

            db.session.close()

            return redirect(url_for('go_to_edit', post_id=post_id))

    return render_template('pages/edit-article.html',
                           article=article,
                           form=form,
                           aside_form=aside_form,
                           cat_form=cat_form,
                           post_id=post_id,
                           tags=tags)


@app.route("/admin/new-category/<post_id>", methods=["POST"])
def save_new_category(post_id):
    """Defines new-category route to save new articles """

    category = Category(name=request.form.get('name'))

    save_new_data(category, db)

    return redirect(url_for('go_to_edit', post_id=post_id))


@app.route('/admin/login', methods=['GET', 'POST'])
def loginUser():

    """ Log in the user"""

    form = LoginUserForm()

    if request.method == 'POST':

        if form.validate_on_submit():

            user = find_user(dbs=db, identifier=form.email.data)

            password = form.password.data

            if user:

                if check_password_hash(user.password_hash, password):

                    login_user(user)

                    flash("Logged in !")

                    return redirect(url_for('logAdmin'))

                else:

                    flash("Nom d'utilisateur ou mot de passe erronee")

            else:

                flash("Nom d'utilisateur inconnu. Veuillez vous enregistrer")

    return render_template('pages/auth.login.html', form=form)
