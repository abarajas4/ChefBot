import requests
import userinput
import pandas as pd


def recipe_list(data):
    result = []
    for recipe in data['results']:
        title = recipe["title"]
        source_url = recipe["sourceUrl"]
        serving_price = (recipe["pricePerServing"] / 100)
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

    A_KEY = ""
    url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={A_KEY}" \
          f"&number={meals}&cuisine={cuisines}&diet={dietary}" \
          f"&type={meal_type}&minServings={serving_size}" \
          f"&addRecipeInformation=True"

    response = requests.get(url)
    data = response.json()

    recipes = recipe_list(data)

    print("\nHere is your personalized, ChefBot approved Meal Plan: \n")

    for i, recipe in enumerate(recipes, 1):
        result = ""
        title, price, source_url = recipe
        print(f"\nRecipe {i}: {title}")
        print(f"    Total Price of Recipe: ${price}")
        sen = """Learn more about the recipe,
        including ingredients and instructions for preparation"""
        hyperlink = f"\033]8;;{source_url}\a{sen}\033]8;;\a"
        result += hyperlink + "\n"
        print(f"    {result}")

    print("\nThank you for choosing ChefBot. We hope you enjoy your meals!\n")

    # Define the column names
    columns = ["Recipe", "Price", "Link"]
    # Create a DataFrame from the nested list
    df = pd.DataFrame(recipes, columns=columns)
    # Display the table
    #print(df)


if __name__ == "__main__":
    print("\nWelcome to ChefBot!\n")
    print("We are the #1 program for designing a personal meal plan\n")
    print("So how does ChefBot work?\n")
    print("  Chefbot will ask questions about your dietary restrictions,")
    print("  preferred cuisines, and how many meals you'd like in your plan\n")
    print("  By giving ChefBot the most accurate information, we can tailor")
    print("  your mealplan directly to your wants and needs\n")
    print("  Along with the recipes, ChefBot will include information")
    print("  on the price, ingredients, and preparation instructions\n")
    print("  This ensures meal plans are easy to follow along\n")
    print("  Through ChefBot, we want to make cooking easier.")
    print("  Let's make cooking fun!\n")

    user_input = input("Are you ready to get started with ChefBot? y/n: ")
    if user_input.lower() == "y":
        main()
    else:
        print("\nWe're sorry to hear that. We hope to see you again soon!\n")
