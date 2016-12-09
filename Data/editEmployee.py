from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField,FloatField
from wtforms.validators import Email, Length, DataRequired, EqualTo

class editEmployee(FlaskForm):
    lastname = StringField("Last Name")
    firstname = StringField("First Name")
    email = StringField('Email')
    socialsecurity = IntegerField('Social Security No.')
    username = StringField('Username')
    password = PasswordField('New Password'
    )
    confirm = PasswordField('Repeat Password')
    address = StringField('Address')
    city = StringField('City')
    zipcode = IntegerField('Zip Code')
    state = StringField('State')
    states=["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID", "IL",
     "IN","KS","KY","LA","MA","MD","ME","MH","MI","MN","MO","MS","MT","NC","ND","NE",
     "NH","NJ","NM","NV","NY", "OH","OK","OR","PA","PR","PW","RI","SC","SD","TN","TX",
     "UT","VA","VI","VT","WA","WI","WV","WY"]
    telephone = IntegerField('Telephone No.')
    hourlypay = FloatField('Hourly Rate')
    company = StringField('Company Representing')

    submit = SubmitField('Submit')
