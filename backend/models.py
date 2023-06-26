import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))

    email = db.Column(db.String(255))

    password = db.Column(db.String(100), nullable=False)

    @property
    def password(self):
        """ Returns an error whenever the psw id demanded"""

        raise AttributeError("Password is not a readable entity")


    @password.setter
    def password(self, password):
        """ Sets the password of the user"""

        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """ Checks wether the user's password is correct"""

        return check_password_hash(pwhash=self.password_hash, password=password)



class Post(db.Model):

    """Class defining the Post model"""

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50), nullable=False)

    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    image_banner = db.Column(db.String(100))

    category = db.Column(db.String(100))

    tag = db.Column(ARRAY(db.String(100)))

    author = db.Column(db.String(100), default="lecarabin")
    def __repr__(self):

      return f'Post {self.title}'

    def update(self):

        """Updates the model after a change"""

        db.session.commit()


class Image(db.Model):

    """Defines the Image Model"""

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(200), nullable=False)

    description = db.Column(db.String(100), nullable=False)

    image = db.Column(db.LargeBinary(length=(2 * 3) - 1), nullable=False)

    def __repr__(self):

      return f'<Image {self.filename}> for <Article {self.post_id}'


class Category(db.Model):

    """Defines the Categiory class"""

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    label = db.Column(db.String(100))

    def __repr__(self):

        return f"{self.name}"

    def update(self):

        """ Method to update the Model and saves the result of the operation in a log file"""

        with open('./lc_contents/categories_logs/', 'a') as log_file:

            log_file.write(f"The Category {self.name} was call for modifications")

            try:

                db.session.commit()

                log_file.write(f"Operation succeded at {datetime.datetime.utcnow()}")

                log_file.write(f"{self.name} was modified")

            except Exception as e:

                log_file.write(f"Operation failed at {datetime.datetime.utcnow()}")

                log_file.write(f"The error raised was:")

                log_file.write(e)
