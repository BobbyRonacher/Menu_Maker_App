import pandas as pd
import nutrition as n
import menu_maker
recipe1 = {'calories': [100, 200], 'carbs': [10, 20], 'fat': [10, 20], 'protein':[3, 6], 'title': ['recipe a', 'recipe b'], 'url': ['recipea.com','recipeb.com']}
recipe2 = {'carbs': [10, 20], 'fat': [10, 20], 'protein':[3, 6], 'title': ['recipe e', 'recipe f'], 'url': ['recipee.com','recipef.com']}
recipe3 = {'calories': [100, 200], 'carbs': [10, 20], 'fat': [10, 20], 'protein':[3, 6], 'title': ['recipe c', 'recipe d'], 'url': ['recipec.com','reciped.com']}


df1 = pd.DataFrame(data=recipe1)
df2 = pd.DataFrame(data=recipe2)
df3 = pd.DataFrame(data=recipe3)
df4 = pd.concat([df1, df2, df3])
n.block_recipe(df4[df4['title'] == 'recipe a'])
n.block_recipe(df4[df4['title'] == 'recipe b'])
n.block_recipe(df4[df4['title'] == 'recipe b'], 'test')


recipe = n.Recipe()
recipe.add_to_my_recipes(df1, 'test_recipes.csv')
recipe.add_to_my_recipes(df2, 'test_recipes.csv')
recipe.add_to_my_recipes(df3, 'test_recipes.csv')

# check test_csv has recipea, b, c, d
# check test_csv does not have e, f


