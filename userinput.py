

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
    selected_restriction = []
    initial = input("Do you have any dietary restrictions? y/n: ")
    initial.lower()
    if initial == "n": 
        print ("\n You have selected no dietary restrictions")
        return selected_restriction
    elif initial == "y":
        print("""\nPlease choose from the list below by entering the full diet name as it appears. 
If you have more than one diet, please separate the values with a comma\n""")
        for option in options:
            print(option)
        user_input = input("\nEnter your dietary restrictions, separated by comma: ")
        restrictions = user_input.split(",")
        for restriction in restrictions:
            if restriction.strip() in options: 
                selected_restriction.append(restriction.strip())
    print("\nYou have selected the following dietary restrictions:")
    for res in selected_restriction:
        print(res)
    return selected_restriction

get_dietary_restrictions()