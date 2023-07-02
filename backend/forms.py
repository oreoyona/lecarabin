from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, SelectField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired


class ImageForm(FlaskForm):

    """Defines the Image Form"""

    name = StringField('filename', validators=[DataRequired()])

    description = StringField('description', validators=[DataRequired()])


class ArticleForm(FlaskForm):

    """Defines the Article Form"""

    title = StringField('title', validators=[DataRequired()])

    image_banner = FileField('image_banner')

    content = CKEditorField('content', validators=[DataRequired()])

    submit = SubmitField('Publier')


class AsideArticleForm(FlaskForm):

    """Defines the second form to be defined aside from the main article form"""

    author = SelectField(u'author', validators=[DataRequired()])

    category = SelectField(u'category', validators=[DataRequired()])

    tag = StringField('tag', validators=[DataRequired()])


class CategoryForm(FlaskForm):

    """ Defines the Category form """

    name = StringField("name", validators=[DataRequired()])

    submit = SubmitField("Enregistrer")


class LoginUserForm(FlaskForm):

    """ Defines the LoginUser form"""

    email = StringField('email', validators=[DataRequired()])

    password = StringField('password', validators=[DataRequired()])

    submit = SubmitField('Connexion')


class InscrptionForm(FlaskForm):

    """ Defines the inscriptionUser form"""

    name = StringField('name', validators=[DataRequired()])

    email = StringField("email", validators=[DataRequired()])

    password = StringField('password', validators=[DataRequired()])

    sec_password = StringField('sec_password', validators=[DataRequired()])


    submit = SubmitField('Enregister')
