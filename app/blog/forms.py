from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Edit your bio',validators = [Required()])
    submit = SubmitField('Edit bio')
