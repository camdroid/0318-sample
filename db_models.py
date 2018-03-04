from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/get_recipes')
def get_recipes():
    recipes = Recipe.query.all()
    print(recipes)
    if recipes:
        return render_template('list_recipes.html', recipes=recipes)
    else:
        return "no recipes found!"


@app.route('/add_recipe/', methods=['GET'])
def show_recipe_form():
    recipe_form = RecipeForm()
    return render_template('recipe_form.html', form=recipe_form)


@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    import pdb; pdb.set_trace()

    db.session.commit()


@app.route('/')
def home():
    return "Welcome to my Recipe Site!"


class RecipeForm(FlaskForm):
    title = StringField('Title')
    ingredients = TextAreaField('Ingredients')
    instructions = TextAreaField('Instructions')
    submit = SubmitField('Submit')


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    ingredients = db.Column(db.String(256))
    instructions = db.Column(db.String(512))

    def __init__(self, title=None, ingredients=None, instructions=None):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def add_ingredient(self, ingredient):
        self.ingredients += ingredient


db.create_all()

if __name__ == '__main__':
    app.run()
