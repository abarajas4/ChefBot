import requests 
import json
import userinput

dietary = userinput.get_dietary_restrictions()
cuisines = userinput.get_cuisines()
#meal_type = userinput.get_meal_type()
meals = userinput.get_num_of_meals()

API_KEY = "de9a68661df04656bf8240a057bbf72a"
url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}" \
f"&number={meals}&cuisine={cuisines}&diet={dietary}"
f"&addRecipeInformation=True&instructionsRequired=True&addRecipeInstructions=True"

response = requests.get(url)
data = response.json()
print(json.dumps(data))

"""
for recipe in data['results']:
   title = recipe["title"]
   source_url = recipe["sourceUrl"]
   serving_price= (recipe["pricePerServing"]/10)
   rounded_price = round(serving_price, 2)
   print(serving_price)
   print(rounded_price)
"""


#testing if Yuneydy can push
