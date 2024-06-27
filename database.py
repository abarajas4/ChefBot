import requests
import sqlalchemy as db
import pandas as pd
import recipe_recommend

"""
# API Configuration
API_URL = "https://api.spoonacular.com/recipes/random"
API_KEY = ""
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
"""

engine = db.create_engine('sqlite:///chefbot.db')

#def create_tables():


def add_recipe_to_db(title, source_url, price):
    with engine.connect() as connection:
        query = db.text("INSERT INTO recipes (title, source_url, price) VALUES (:title, :source_url, :price)")
        connection.execute(query, {"title": title, "source_url": source_url, "price": price})

def fetch_all_recipes():
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM recipes;")).fetchall()
        return pd.DataFrame(query_result, columns=['recipe_id', 'title', 'source_url', 'price'])

def main():
    metadata = db.MetaData()
    
    recipes = db.Table('recipes', metadata,
        db.Column('recipe_id', db.Integer, primary_key=True, autoincrement=True),
        db.Column('title', db.String),
        db.Column('source_url', db.String), 
        db.Column('price', db.Float))
    
    metadata.create_all(engine)
    # Fetch recipes data from recipe_recommend function
    data = recipe_recommend.recipe_list(recipe_recommend.data)

    # Parse the return string and add recipes to the database
    for line in data.strip().split("\n"):
        title, source_url, price = line.split(',')
        add_recipe_to_db(title, source_url, float(price))
    
    # Fetch and display all recipes from the database
    recipes_df = fetch_all_recipes()
    print(recipes_df)

if __name__ == "__main__":
    main()
