from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


class RecipeForm(FlaskForm):
    title = StringField('Title')
    ingredients = TextAreaField('Ingredients')
    instructions = TextAreaField('Instructions')
    submit = SubmitField('Submit')


class Recipe():
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

@app.route('/add_recipe')
def show_recipe_form():
    recipe_form = RecipeForm()
    return render_template('recipe_form.html', form=recipe_form)


if __name__ == '__main__':
    app.run(debug=True)
