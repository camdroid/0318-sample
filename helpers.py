from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField


class RecipeForm(FlaskForm):
    title = StringField('Title')
    ingredients = TextAreaField('Ingredients')
    instructions = TextAreaField('Instructions')
    submit = SubmitField('Submit')


