from flask_wtf import FlaskForm as Form
import wtforms
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Required


class LoginForm(Form):
    username = StringField('username', [DataRequired(message='请填写用户名')])
    password = PasswordField('password', [DataRequired(message='请填写密码')])
