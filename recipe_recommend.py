import requests 
import json


API_KEY = "de9a68661df04656bf8240a057bbf72a"
url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}" \
"&number=5&cuisine=American&addRecipeInstructions=True&instructionsRequired=True&addRecipeInformation=True"

response = requests.get(url)
data = response.json()

for recipe in data['results']:
   print(recipe["title"])
   print(recipe["sourceUrl"])
   print((recipe["pricePerServing"])/100)

#testing if Yuneydy can push