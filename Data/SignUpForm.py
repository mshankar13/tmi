from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField
from wtforms.validators import Email, Length, DataRequired, EqualTo

class SignUpForm(FlaskForm):
    lastname = StringField("Last Name",validators=[DataRequired()])
    firstname = StringField("First Name",validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired(),Length(min=3,max=14)])
    password = PasswordField('New Password', [
        DataRequired(),
        Length(min=6,max=14),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    address = StringField('Address')
    city = StringField('City')
    state = StringField('State')
    states=["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID", "IL",
     "IN","KS","KY","LA","MA","MD","ME","MH","MI","MN","MO","MS","MT","NC","ND","NE",
     "NH","NJ","NM","NV","NY", "OH","OK","OR","PA","PR","PW","RI","SC","SD","TN","TX",
     "UT","VA","VI","VT","WA","WI","WV","WY"]
    userType = StringField('User Type')
    userTypes = ["manager","company","user"]
    submit = SubmitField('Submit')

