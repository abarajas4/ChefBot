import requests
import sqlalchemy as db
import pandas as pd
from userinput import get_dietary_restrictions, get_cuisines, get_meal_type, get_serving_size, get_num_of_meals
import recipe_recommend

# API Configuration
API_URL = "https://api.spoonacular.com/recipes/random"
API_KEY = "de9a68661df04656bf8240a057bbf72a"
# Database Configuration
engine = db.create_engine('sqlite:///chefbot.db')

def fetch_random_recipe(diet=None, cuisines=None, meal_type=None, serving_size=None, num_of_meals=1):
    params = {
        "apiKey": API_KEY,
        "number": num_of_meals,
        "diet": diet,
        "cuisine": cuisines,
        "type": meal_type
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()["recipes"]
    else:
        response.raise_for_status()

def create_tables():
    metadata = db.MetaData()
    
    recipes = db.Table('recipes', metadata,
                       db.Column('recipe_id', db.Integer, primary_key=True),
                       db.Column('title', db.String),
                       db.Column('ingredients', db.Text),
                       db.Column('instructions', db.Text),
                       db.Column('prep_time', db.Integer),
                       db.Column('cook_time', db.Integer),
                       db.Column('nutrition_info', db.Text))
    
    metadata.create_all(engine)

def add_recipe_to_db(recipe):
    df = pd.DataFrame([recipe])
    df.to_sql('recipes', con=engine, if_exists='replace', index=False)

def fetch_all_recipes():
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM recipes;")).fetchall()
        return pd.DataFrame(query_result)

def main():
    # Get user preferences
    diet = get_dietary_restrictions()
    cuisines = get_cuisines()
    meal_type = get_meal_type()
    serving_size = get_serving_size()
    num_of_meals = get_num_of_meals()
    
    # Create tables
    create_tables()
    
    # Fetch random recipes from the API
    recipes = fetch_random_recipe(diet=diet, cuisines=cuisines, meal_type=meal_type, serving_size=serving_size, num_of_meals=num_of_meals)
    
    # Extract and format the recipes data
    for recipe in recipes:
        recipe_data = {
            'recipe_id': recipe['id'],
            'title': recipe['title'],
            'ingredients': ", ".join([ingredient['name'] for ingredient in recipe['extendedIngredients']]),
            'instructions': recipe['instructions'],
            'prep_time': recipe.get('prepTime', None),
            'cook_time': recipe.get('cookTime', None),
            'nutrition_info': recipe.get('nutrition', {}).get('nutrients', [{}])[0].get('amount', None)
        }
        # Add the recipe to the database
        add_recipe_to_db(recipe_data)
    
    # Fetch and display all recipes from the database
    recipes_df = fetch_all_recipes()
    print(recipes_df)

if __name__ == "__main__":
    main()
