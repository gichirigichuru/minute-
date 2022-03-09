import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, EqualTo
from wtforms import ValidationError
from ..models import User
