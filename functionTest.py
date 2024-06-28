import unittest 
import userinput 
import recipe_recommend

class TestUserInput(unittest.TestCase):
    def test_get_dietary_restrictions_yes(self):
        self.assertEqual(userinput.get_dietary_restrictions(), 'Vegetarian,Vegan')

    def test_get_cuisines_yes(self):
        self.assertEqual(userinput.get_cuisines(), 'Italian,Mexican')

    def test_get_meal_type(self):
        self.assertEqual(userinput.get_meal_type(), 'main course,soup')

    def test_get_serving_size(self):
        self.assertEqual(userinput.get_serving_size(), 4)

    def test_get_num_of_meals(self):
        self.assertEqual(userinput.get_num_of_meals(), 3)
    
    def test_recipe_list(self):
        mock_data = {
            "results": [
                {
                    "title": "Spaghetti Carbonara",
                    "sourceUrl": "http://example.com/spaghetti-carbonara",
                    "pricePerServing": 250, 
                    "servings": 4
                },
                {
                    "title": "Chicken Salad",
                    "sourceUrl": "http://example.com/chicken-salad",
                    "pricePerServing": 150,
                    "servings": 2
                }
            ]
        }

        expected_result = [
            ["Spaghetti Carbonara", 10.0, "http://example.com/spaghetti-carbonara"],
            ["Chicken Salad", 3.0, "http://example.com/chicken-salad"]
        ]
        result = recipe_recommend.recipe_list(mock_data)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
