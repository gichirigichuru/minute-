from email.policy import default
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
import enum

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class PitchCategoryEnum(enum.Enum):
    pickupline = 'Pick Up Line'
    interviewpitch = 'Interview Pitch'
    productpitch = 'Product Pitch'
    promotionpitch = 'Promotion Pitch'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    category = db.Column(db.Enum(PitchCategoryEnum),
                default=PitchCategoryEnum.productpitch,
                nullable=False)
    posted = db.Column(db.Time,default=datetime.utcnow())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(user_id=id).all()
        return pitches



class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

    id = db.Column(db.Integer,primary_key = True)
    pic_path = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


class User(UserMixin, db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255),index = True)
  email = db.Column(db.String(255),unique = True,index = True)
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())


  password_hash = db.Column(db.String(255))
  photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")
#   reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

  @property
  def password(self):
      raise AttributeError('You cannnot read the password attribute')

  @password.setter
  def password(self, password):
      self.password_hash = generate_password_hash(password)


  def verify_password(self,password):
      return check_password_hash(self.password_hash,password)


  def save_user(self):
      db.session.add(self)
      db.session.commit()

  def __repr__(self):
      return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'user {self.name}'
