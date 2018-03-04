from flask import Flask
from flask import render_template
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


@app.route('/add_user/<uname>')
def add_user(uname):
    db.session.add(User(username=uname))
    db.session.commit()
    return 'Succesfully added user ' + uname


@app.route('/')
def home():
    return "Welcome to my Recipe Site!"


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    ingredients = db.Column(db.String(256))
    instructions = db.Column(db.String(512))
    ingredients_list = []

    def set_title(self, t):
        self.title = t

    def set_ingredient(ingredient, quantity):
        # This could look something like {"chicken breasts": "1 lb"}
        ingredient_d = {ingredient: quantity}
        self.ingredients_list.append(ingredient_d)
        self.ingredients = json.dump(self.ingredients_list)


db.create_all()

if __name__ == '__main__':
    app.run()
