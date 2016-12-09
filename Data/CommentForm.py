from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CommentForm(FlaskForm):
    post = TextAreaField('Make a comment',validators=[DataRequired(),Length(max=255)])
    submit = SubmitField('Comment')