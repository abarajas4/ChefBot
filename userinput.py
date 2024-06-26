

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

    mistake = input("\nAre these restrictions correct? y/n: ")
    mistake.lower()

    if mistake == "n":
        get_dietary_restrictions()

    return selected_restriction

def get_cuisines():
    options = {
        "African", 
        "Asian", 
        "American", 
        "British", 
        "Cajun", 
        "Carribean", 
        "Chinese", 
        "Eastern European", 
        "European", 
        "French", 
        "German", 
        "Greek", 
        "Indian", 
        "Irish", 
        "Italian", 
        "Japanese", 
        "Korean",
        "Latin American", 
        "Mediterranean", 
        "Mexican", 
        "Middle Eastern", 
        "Nordic", 
        "Southern", 
        "Spanish", 
        "Thai", 
        "Vietnamese"
    }

    selected_cuisines = []
    print("""\nDo you have any preferred cuisines?
Enter as many as you like from the list below by separating names with a comma\n""")
    
    for option in options: 
        print(option)

    user_input = input("\nEnter your preferred cuisines: ")
    cuisines = user_input.split(",")

    for cuisine in cuisines:
        if cuisine.strip() in options:
            selected_cuisines.append(cuisine.strip())
    print("\nYou have selected the following preferred cuisines:\n")

    for cuisine in selected_cuisines:
        print(cuisine)

    mistake = input("\nAre these correct? y/n: ")
    mistake.lower()

    if mistake == "n":
        get_cuisines()

    return selected_cuisines


get_dietary_restrictions()
get_cuisines()