from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField
from wtforms.validators import Email, Length, DataRequired, EqualTo

class LoginForm(FlaskForm):
    userID = StringField('User',validators = [DataRequired()], render_kw={"placeholder": "username"})
    password = PasswordField('Password', validators = [DataRequired()], render_kw={"placeholder": "password"})
    login = SubmitField('Sign In')
