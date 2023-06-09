"""The entry point of lecarabin"""
import mimetypes
from flask_wtf import FlaskForm
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_migrate import Migrate
from forms import ArticleForm
from models import db, User, Post, Image
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
#############################################################################
@app.route("/")
def go_to_home():
  return render_template('index.html')


@app.route("/dashboard")
def go_to_admin():
  articles = Post.query.all()
  return render_template('admin.html', title="Dashboard", articles=articles)


@app.route("/new-article", methods=['GET', 'POST'])
def go_to_new_article():
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
        print("post added")
        db.session.commit()
        form.image_banner.data.save(os.path.join(app.config['UPLOAD_FOLDER'] ,filename))
        flash("The article was successfully published")
      except Exception as e:
        print(e)

        flash("Something went wrong, please try later")
      finally:
        db.session.close()

    return redirect(url_for('go_to_new_article'))
  return render_template('pages/new-article.html', form=form)

@app.route("/edit-post/<id>", methods=["GET", "POST"])
def image_upload(id:int):

  pass


if __name__ == "__main__":
  app.run(debug=True)
