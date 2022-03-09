import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo
from wtforms import ValidationError
from ..models import User



class LoginForm(FlaskForm):
  email = StringField('Your Email Address', validators=[Required(), Email()])
  password = PasswordField('Password', validators=[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
  email = StringField('Your Email Address', validators=[Required(), Email()])
  username = StringField('Enter your username', validators=[Required()])
  password = PasswordField('Password', validators=[Required(),
  EqualTo('password2', message='Passwords must match')])
  password2 = PasswordField('Confirm Password', validators=[Required()])
  submit = SubmitField('Sign Up')

