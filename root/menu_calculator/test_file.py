import unittest
import nutrition as n
import pandas as pd

cal1, carb1, fat1, protein1 = 400, 400*.5/4, 400*.25/9, 400*.25/4
cal2, carb2, fat2, protein2 = 1000, 1000*.5/4, 1000*.25/9, 1000*.25/4

healthy_test_data = {'calories': [cal1], 'carbs': [carb1], 'category': ['Dinner'], 'fat': [fat1],
             'nutrition': ["{'calories': '10', 'carbohydrateContent': '10g', 'proteinContent': '5g', 'fatContent': '10g'}"],
             'protein': [protein1], 'rating': [5], 'reviewCount': [10],
             'source': ['test'], 'title': ['Test Recipe'], 'url': ['N/A']}
unhealthy_test_data = {'calories': [cal2], 'carbs': [carb2], 'category': ['Dinner'], 'fat': [fat2],
             'nutrition': ["{'calories': '10', 'carbohydrateContent': '10g', 'proteinContent': '5g', 'fatContent': '10g'}"],
             'protein': [protein2], 'rating': [5], 'reviewCount': [10],
             'source': ['test'], 'title': ['Test Recipe'], 'url': ['N/A']}
df = pd.DataFrame(data=healthy_test_data)
df2 = pd.DataFrame(data=unhealthy_test_data)
test_recipe1 = n.Recipe(df.copy())
test_recipe2 = n.Recipe(df.copy())
test_recipe3 = n.Recipe(df.copy())
test_recipe4 = n.Recipe(df.copy())
test_recipe5 = n.Recipe(df2.copy())
test_recipes = [test_recipe1, test_recipe2, test_recipe3, test_recipe4]
for i in range(0, len(test_recipes)):
    test_recipes[i].calories = test_recipes[i].recipe_df['calories']
    test_recipes[i].carbs = test_recipes[i].recipe_df['carbs']
    test_recipes[i].protein = test_recipes[i].recipe_df['protein']
    test_recipes[i].fat = test_recipes[i].recipe_df['fat']
    test_recipes[i].recipe_df['title'] = 'Test Recipe ' + str(i + 1)


test_menu = n.Menu()
test_menu.recipes_df = pd.concat([test_recipe1.recipe_df, test_recipe2.recipe_df, test_recipe3.recipe_df, test_recipe4.recipe_df])
test_menu.aggregate_nutrition()
test_menu.calculate_nutrition_percentages()
test_menu.check_is_balanced_menu()

test_menu_2 = n.Menu()
test_menu_2.recipes_df = pd.concat([test_recipe2.recipe_df, test_recipe3.recipe_df, test_recipe4.recipe_df, test_recipe5.recipe_df])
test_menu_2.aggregate_nutrition()
test_menu_2.calculate_nutrition_percentages()
test_menu_2.check_is_balanced_menu()

class TestMethods(unittest.TestCase):
    def test_menu_calories(self):
        self.assertEqual(test_menu.calories, 4*cal1)
        self.assertEqual(test_menu_2.calories, 3*cal1 + cal2)
    def test_menu_carbs(self):
        self.assertEqual(test_menu.carbs, 4*carb1)
        self.assertEqual(test_menu_2.carbs, 3*carb1 + carb2)
    def test_menu_fat(self):
        self.assertEqual(test_menu.fat, 4*fat1)
        self.assertEqual(test_menu_2.fat, 3*fat1 + fat2)
    def test_menu_protein(self):
        self.assertEqual(test_menu.protein, 4*protein1)
        self.assertEqual(test_menu_2.protein, 3*protein1 + protein2)

    def test_balanced_menu(self):
        self.assertTrue(test_menu.balanced)
        self.assertFalse(test_menu_2.balanced)

if __name__ == '__main__':
    unittest.main()