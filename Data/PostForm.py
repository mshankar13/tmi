from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    post = TextAreaField('Make a post',validators=[DataRequired(),Length(max=255)])
    submit = SubmitField('Post')
