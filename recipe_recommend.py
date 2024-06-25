import requests 
import json


API_KEY = ""
url = f'https://api.spoonacular.com/recipes/complexSearch?query=pasta&apiKey={API_KEY}&number=2'

response = requests.get(url)
data = response.json()

for recipe in data["results"]:
    print(recipe["title"])
