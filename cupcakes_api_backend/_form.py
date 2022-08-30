from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL
from models import db, connect_db, Cupcake


class AddCupCakeForm(FlaskForm):
    '''Form to add Cupcakes to the db'''

    flavor = StringField('Flavor: ',  validators=[
        InputRequired(message='Name is Required')])

    size = SelectField('Size: ',  choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')], validators=[
        InputRequired(message='Name is Required')])

    rating = FloatField('Rating: ',  validators=[
        InputRequired(message='Rating is Required')])

    image = StringField('Flavor: ',  validators=[URL(
        require_tld=True, message='Enter Valid URL')])
