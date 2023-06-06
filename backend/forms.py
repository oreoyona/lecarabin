from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
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

