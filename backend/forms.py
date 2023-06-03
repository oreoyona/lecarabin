from flask_admin.form import ImageUploadField
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class ImageForm(FlaskForm):
    """Defines the Image Form"""
    name = StringField('filename', validators=[DataRequired()])
    image = ImageUploadField('image')
    description = StringField('description', validators=[DataRequired()])
    post_id = IntegerField('post_id', validators=[DataRequired()])

