import requests 
import json
import userinput

def recipe_list(data):
   result = []
   for recipe in data['results']:
      title = recipe["title"]
      source_url = recipe["sourceUrl"]
      serving_price= (recipe["pricePerServing"]/100)
      servings = recipe["servings"]
      totalPrice = round(serving_price * servings, 2)
      result.append([title, totalPrice, source_url])
   return result

def print_bold(text):
    return f"\033[1m{text}\033[0m"

def main(): 
   dietary = userinput.get_dietary_restrictions()
   cuisines = userinput.get_cuisines()
   meal_type = userinput.get_meal_type()
   meals = userinput.get_num_of_meals()
   serving_size = userinput.get_serving_size()

   API_KEY = "de9a68661df04656bf8240a057bbf72a"
   url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}" \
   f"&number={meals}&cuisine={cuisines}&diet={dietary}&type={meal_type}" \
   f"&minServings={serving_size}&addRecipeInformation=True"

   response = requests.get(url)
   data = response.json()

   recipes = recipe_list(data)
   
   print("\nWith your inputs in mind, here is your ChefBot approved Meal Plan: \n")

   for i, recipe in enumerate(recipes, 1):
      result = ""
      title, price, source_url = recipe
      print(f"\nRecipe {i}: {title}")
      print(f"    Total Price of Recipe: ${price}")
      sen = "Learn more about the recipe, including ingredients and instuctions for preparation"
      hyperlink = f"\033]8;;{source_url}\a{sen}\033]8;;\a" 
      result += hyperlink + "\n"
      print(f"    {result}")


if __name__ == "__main__":
   main()
