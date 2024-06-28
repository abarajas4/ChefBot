# ChefBot Meal Planner

ChefBot is a personalized meal planning program designed to help users create customized meal plans based on their dietary preferences, cuisine choices, and other meal preferences. This project integrates with the Spoonacular API to fetch recipe data that matches the user's input criteria.

## Features

- **Dietary Restrictions:** Users can specify dietary restrictions such as gluten-free, vegetarian, vegan, etc.
- **Preferred Cuisines:** Users can select preferred cuisines from a comprehensive list of options.
- **Meal Types:** Users can choose from various meal types like main course, appetizer, salad, etc.
- **Serving Size:** Users specify the number of people they are cooking for.
- **Number of Meals:** Users can select the number of meals they want ChefBot to plan for.
- **Output:** ChefBot provides a detailed meal plan including recipe titles, total prices, and links to recipe sources.

## Installation

1. **Clone the repository:**
- git clone 
- cd chefbot 

2. **Install Dependencies**
- pip install -r requirements.txt

3. **API Key**
- Obtain an API Key from [Spoonacular](https://spoonacular.com/food-api) and update `API_KEY` in `main.py`.

## Usage

1. **Run the program**

2. **Follow prompts**
- Respond to prompts to specify dietary restrictions, preferred cuisines, meal types, serving size, and number of meals.

3. **View Results**
- ChefBot will generate a personalized meal plan based on your inputs, displaying recipe titles, total prices, and links to recipe sources.

## Example

*Upon running the program, users will see:*

    Welcome to ChefBot, the #1 program for designing your personal meal plan

    So how does ChefBot work?

    Chefbot will ask you a range of questions, from your dietary restrictions,
    to your preferred cuisines, and even how many meals you would like in your meal plan

    By giving ChefBot the most accurate information about yourself, we can tailor
    your meal plan directly to your wants and needs

    Along with the name of a diverse set of dishes, ChefBot will include information
    on the price, ingredients, and preparation instructions to ensure any recipe on your
    meal plan is accessible and easy to follow along

    Through ChefBot, we want to make cooking easier for all students to avoid any nightly
    ramen or otherwise plain meals. Let's make cooking fun!

    How does that sound? Are you ready to get started with ChefBot? y/n:

## Authors 
- Andre Barajas & Yuneydy Paredes