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
    initial = input("\nDo you have any dietary restrictions? y/n: ").lower()

    if initial == "n":
        print("\nYou have selected no dietary restrictions")
        return selected_restriction
    elif initial == "y":
        print(
            "\nPlease choose from the list below by entering the full diet "
            "name as it appears. If you have more than one diet, please "
            "separate the values with a comma\n"
        )
        for option in options:
            print(option)
        user_input = input(
            "\nEnter your dietary restrictions, separated by comma: "
        )
        restrictions = user_input.split(",")
        for restriction in restrictions:
            if restriction.strip() in options:
                selected_restriction.append(restriction.strip())

    print("\nYou have selected the following dietary restrictions:")

    for res in selected_restriction:
        print(res)

    mistake = input("\nAre these restrictions correct? y/n: ").lower()

    if mistake == "n":
        return get_dietary_restrictions()

    return ",".join(selected_restriction)


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
    print(
        "\nDo you have any preferred cuisines?\nEnter as many as you like "
        "from the list below by separating names with a comma\n"
    )

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

    mistake = input("\nAre these correct? y/n: ").lower()

    if mistake == "n":
        return get_cuisines()

    return ",".join(selected_cuisines)


def get_meal_type():
    options = {
        "main course",
        "side dish",
        "appetizer",
        "salad",
        "breakfast",
        "soup",
        "snack"
    }
    selected_mealtype = []
    print(
        "\nWhat type of meal recipes would you like to receive?\nPlease "
        "choose options from the list below, separating names with comma\n"
    )

    for option in options:
        print(option)

    user_input = input("\nSelect your preferred dish types: ")
    dishes = user_input.split(",")

    for dish in dishes:
        if dish.strip() in options:
            selected_mealtype.append(dish.strip())

    print("\nYou have selected preference for these meals:")
    for dish in selected_mealtype:
        print(dish)

    mistake = input("\nAre these correct? y/n: ").lower()
    if mistake == "n":
        return get_meal_type()

    return ",".join(selected_mealtype)


def get_serving_size():
    print("\nOur recipes can serve anywhere from 1 person to 8 people")
    user_input = input(
        "\nHow many people will you be cooking for? Please enter an integer: "
    )
    print(
        "\nYou have selected recipes with serving sizes of at least "
        + user_input.strip()
    )
    mistake = input("\nIs this correct? y/n: ").lower()
    if mistake == "n":
        return get_serving_size()
    return int(user_input.strip())


def get_num_of_meals():
    print("\nHow many meals you would like us to help plan.")
    user_input = input(
        "\nInput a number between 1-25 for the number of recipes to receive: "
    )
    print("\nYou have selected to receive " + user_input.strip() + " meal(s)")
    mistake = input("\nIs this correct? y/n: ").lower()
    if mistake == "n":
        return get_num_of_meals()
    return int(user_input.strip())
