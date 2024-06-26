

"""
types a user can input: cuisine, diet, 
min/max servings, calories, protein
"""

def get_dietary_restrictions():
    options = {
        "Gluten Free", 
        "Ketogenic", 
        "Vegetarian", 
        "Lacto-Vegetarian", 
        "Ovo-Vegetarian", 
        "Vegan", 
        "Pescatarian", 
        "Paleo", 
        "Primal", 
        "Whole30"
    }

    initial = input("Do you have any dietary restrictions? y/n")
    if initial == "y" or "Y":
        print("Please choose from the list below by entering")