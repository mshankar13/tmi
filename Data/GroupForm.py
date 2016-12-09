from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class GroupForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()], render_kw={'placeholder':'Name'})
    submit = SubmitField('Create')
