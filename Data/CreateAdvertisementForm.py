from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField, RealField, IntegerField
from wtforms.validators import Email, Length, DataRequired, EqualTo

class CreateAdvertisementsForm(FlaskForm):
    merchandisetype = StringField('Type', validators=[DataRequired(),Length(max=50)])
    company = StringField('Company Name', validators=[DataRequired(), Length(max=50)])
    itemname = StringField('Item Name', validators=[DataRequired, Length(max=70)])
    unitprice = RealField('Unit Price', validators=[DataRequired])
    units = IntegerField('No. Units', validators=[DataRequired])
    submit = SubmitField('Submit')