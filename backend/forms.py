from flask_admin.form import ImageUploadField
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired


class ImageForm(FlaskForm):
    """Defines the Image Form"""
    name = StringField('filename', validators=[DataRequired()])
    image = ImageUploadField('image')
    description = StringField('description', validators=[DataRequired()])
    post_id = IntegerField('post_id', validators=[DataRequired()])

class ArticleForm(FlaskForm):
    """Defines the Article Form"""
    title = StringField('title', validators=[DataRequired()])
    content = CKEditorField('content', validators=[DataRequired()])


