from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError, SelectField, TextField
from wtforms.validators import Required,Email
from ..models import User, Pitch

class PitchForm(FlaskForm):
    title = StringField('Pitch title',validators=[Required()])
    category = SelectField('Category', choices=[(c, c) for c in Pitch.category.property.columns[0].type.enums] ,validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')