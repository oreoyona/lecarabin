import os
from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_user, login_required, current_user, AnonymousUserMixin, UserMixin
from sqlalchemy import select
from flask_wtf import FlaskForm
from base import app, db
from forms import ArticleForm, AsideArticleForm, CategoryForm, InscrptionForm, LoginUserForm
from lc_core import check_pwd, find_user, get_data_from_db, save_to_db, write_log, save_new_data, get_formated_data_from_db

from config import UPLOAD_IMAGE_PATH
from werkzeug.utils import secure_filename
from models import *


@app.route("/")
def go_to_home():
    """Defines the home route"""

    return render_template('index.html')


@app.route("/admin/dashboard")
@login_required
def go_to_admin():
    articles = get_data_from_db(dbs=db, model=Post)

    return render_template('admin.html', title="Dashboard", articles=articles)


@app.route("/admin/new-article", methods=['GET', 'POST'])
@login_required
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
@login_required
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
@login_required
def save_new_category(post_id):
    """Defines new-category route to save new articles """

    category = Category(name=request.form.get('name'))

    save_new_data(category, db)

    return redirect(url_for('go_to_edit', post_id=post_id))


@app.route('/admin/login', methods=['GET', 'POST'])
def loginUser():
    """ Log in the user"""

    if not isinstance(current_user, AnonymousUserMixin):

      return redirect(url_for('go_to_admin'))

    form = LoginUserForm()

    if request.method == 'POST' and form.validate_on_submit():

      user: User = find_user(dbs=db, identifier=form.email.data)

      password = form.password.data

      if not user == None  and user.verify_password(password):

        login_user(user=user, remember=True)

        flash("Logged in !")

        return redirect(url_for('go_to_admin'))

      else:

          flash("Nom d'utilisateur ou mot de passe errones")

    return render_template('pages/auth.login.html', form=form)


@app.route("/add_user", methods=["GET", "POST"])
def addUser():

    i_form: FlaskForm = InscrptionForm()

    if request.method == "POST":

      print()

      if i_form.validate_on_submit():

        pwd = check_pwd(i_form.password.data, i_form.sec_password.data)

        if not pwd == None:

            i_form.password.data = pwd

            user = User(name=i_form.name.data, email=i_form.email.data, password=i_form.password.data)

            result = save_new_data(dbs=db, model=user)

            if result == 0:

              actualUser = find_user(dbs=db, identifier=i_form.email.data)

              login_user(actualUser, remember=True)

              return redirect(url_for('go_to_admin'))

        else:

            flash(" Something went wrong. The 2 passwords are not the same")

      else:

          flash("Veuillez renseigner tous les champs")

    return render_template('pages/add_new_user.html', i_form=i_form)
