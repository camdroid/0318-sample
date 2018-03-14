from flask import Flask, render_template
import requests
from config import Config
from helpers import SearchForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def hello():
    search_form = SearchForm()
    return render_template('ingredient_search.html', form=search_form)


def call_recipe_puppy_search(ingredients):
    url = 'http://recipepuppy.com/api/'
    # Formatted according to http://www.recipepuppy.com/about/api/
    formatted_ingredients = ingredients.replace(' ', ',')
    params = {'i': formatted_ingredients}
    r = requests.get(url, params=params)
    available_recipes = r.json()['results']
    return available_recipes


@app.route('/search', methods=['POST'])
def search():
    search_form = SearchForm()
    ingredients = search_form.ingredients.data
    recipes = call_recipe_puppy_search(ingredients)
    return render_template('search_results.html', recipes=recipes)


if __name__ == '__main__':
    app.run(debug=True)
