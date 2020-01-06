from flask_wtf import FlaskForm
from wtforms import Submitfield
from application import app


class SubmitForm(FlaskForm):


    submit = SubmitField('Roll!')
