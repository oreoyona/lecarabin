from typing import Any
from flask_admin.contrib.sqla import ModelView
from forms import ImageForm
from models import Image


class ImageView(ModelView):
    """Defines the View Model of the Image Class"""
    form = ImageForm

    def on_form_prefill(self, form: ImageForm, id) -> Any:
        model = self.get_one(id)
        if model is not None and model.image is not None:
            form.image.data = form.upload_image.data = form.new_upload.data = form.get_uploaded_images(model.image)

    def on_model_change(self, form: ImageForm, model: Image, is_created):
        if form.image.data:
            model.image = form.image.data.read()
        super().on_model_change(form, model, is_created)
