from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SearchForm(FlaskForm):
    search = StringField(render_kw={'placeholder':'username'})
    submit = SubmitField('Search')
