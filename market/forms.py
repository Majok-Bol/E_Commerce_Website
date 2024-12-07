#import flask forms to handle forms
from flask_wtf import FlaskForm
#import string field module to handle string input,password and submit fields
from wtforms import StringField,PasswordField,SubmitField
class RegisterForm(FlaskForm):
    username=StringField(label='User name:')
    email_address=StringField(label='Email address:')
    password1=PasswordField(label='Password:')
    password2=PasswordField(label='Confirm Password:')
    submit=SubmitField(label='submit')