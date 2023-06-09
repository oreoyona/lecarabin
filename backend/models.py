import datetime
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
db = SQLAlchemy()


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  email = db.Column(db.String(255))
  password = db.Column(db.String(100), nullable=False)

  def __repr__(self):
    return f'<User {self.username}>'

  def set_password(self, password):
    """Password checker"""
    self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

  def check_password(self, password):
    """Check password"""
    return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))


class Post(db.Model):
  """Class defining the Post model"""

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), nullable=False)
  content = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
  image_banner = db.Column(db.String(100))

  def __repr__(self):
    return f'<Post {self.title}'


class Image(db.Model):
    """Defines the Image Model"""

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    image = db.Column(db.LargeBinary(length=(2 * 3) - 1), nullable=False)

    def __repr__(self):
      return f'<Image {self.filename}> for <Article {self.post_id}'
