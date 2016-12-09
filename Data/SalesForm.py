from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField, IntegerField
from wtforms.validators import Email, Length, DataRequired, EqualTo

class SalesForm(FlaskForm):
    NumberofUnits = IntegerField('Number of units', validators=[DataRequired()])
    submit = SubmitField('Submit')