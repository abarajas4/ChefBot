import requests 
import json
import userinput

dietary = userinput.get_dietary_restrictions()
cuisines = userinput.get_cuisines()
meal_type = userinput.get_meal_type()
meals = userinput.get_num_of_meals()
serving_size = userinput.get_serving_size()

API_KEY = ""
url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}" \
f"&number={meals}&cuisine={cuisines}&diet={dietary}&type={meal_type}" \
f"&minServings={serving_size}&addRecipeInformation=True"

response = requests.get(url)
data = response.json()

for recipe in data['results']:
   title = recipe["title"]
   source_url = recipe["sourceUrl"]
   serving_price= (recipe["pricePerServing"]/100)
   servings = recipe["servings"]
   totalPrice = serving_price * servings
   print(title)
   print(round(totalPrice, 2))
   print(source_url)
