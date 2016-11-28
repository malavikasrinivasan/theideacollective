from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField, SelectField, BooleanField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired
import sqlite3 as sql

class LoginForm(Form):
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class ProfileForm(Form):
    email = EmailField('email', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    bio = StringField('bio', validators=[DataRequired()])
    # skills = BooleanField('skills', validators=[DataRequired()])

class IdeaForm(Form):
    idea_name = StringField('idea_name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])

class CommentForm(Form):
    comment = StringField('comment', validators=[DataRequired()])
