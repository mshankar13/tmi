from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField, SubmitField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    subject = StringField('Subject: ', validators=[DataRequired()])
    content = TextAreaField('Message: ',validators=[DataRequired()])
    submit = SubmitField('Send')