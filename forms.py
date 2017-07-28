from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)
from models import User

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('That email already exists.')

def password_not_password(form, field):
    if User.select().where(User.password == 'password'):
        raise ValidationError("Don't use password as your password!")

class RegisterForm(Form):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(), email_exists])

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match'),
            password_not_password])

    password2 = PasswordField(
        'Confirm Password',
        validators = [DataRequired()])

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class TacoForm(Form):
    protein = StringField('Protein', validators=[DataRequired()])
    shell = StringField('Shell', validators=[DataRequired()])
    cheese = BooleanField('Cheese', validators=[DataRequired()])
    extras = TextAreaField('Extras', validators=[DataRequired()])
