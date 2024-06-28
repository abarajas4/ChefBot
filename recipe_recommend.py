import requests 
import json
import userinput
import pandas as pd

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

   print("\nThank you for choosing ChefBot. We hope you enjoy your meals!\n")
   
   #recipes_data = recipe_list(data)
   # Define the column names
   columns = ["Recipe", "Price", "Link"]
   # Create a DataFrame from the nested list
   df = pd.DataFrame(recipes, columns=columns)
   # Display the table
   print(df)

if __name__ == "__main__":
   print("\nWelcome to ChefBot, the #1 program for designing your personal meal plan\n")
   print("So how does ChefBot work?\n")
   print("""     Chefbot will ask you a range of questions, from your dietary restrictions, 
     to your preferred cuisines, and even how many meals you would like in your meal plan\n""")
   print("""     By giving ChefBot the most accurate information about yourself, we can tailor
     your mealplan directly to your wants and needs\n""")
   print("""     Along with the name of a diverse set of dishes, ChefBot will include information
     on the price, ingredients, and preparation instructions to ensure any recipe on your
     meal plan is accessible and easy to follow along\n""")
   print("""     Through ChefBot, we want to make cooking easier for all students to avoid any nightly 
     ramen or otherwise plain meals. Let's make cooking fun!\n""")
   
   user_input = input("How does that sound? Are you ready to get started with ChefBot? y/n: ")
   if user_input.lower() == "y":
      main()
   else:
      print("\nWe're sorry to hear that. We hope to see you again soon!\n")
