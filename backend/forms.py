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

    author = SelectField(u'author', choices=[('Gloire Chabu', 'Chabu, MD'), ('Editor', 'lecarabin')], validators=[DataRequired()])

    category = SelectField(u'category', choices=[('actualites', 'Actualites')], validators=[DataRequired()])

    tag = StringField('tag', validators=[DataRequired()])


