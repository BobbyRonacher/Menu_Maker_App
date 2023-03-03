import pandas as pd
import os


class Menu:
    def __init__(self, calories=0, carbs=0, protein=0, fat=0, balanced=False):
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.balanced = balanced
        self.carb_pct = 100
        self.protein_pct = 100
        self.fat_pct = 100
        self.recipes_df = []
        self.empty = False
        # self.recipes = self.recipes_df[self.recipes_df['title']]
        pass

    def reset_nutrition(self):
        self.calories = 0
        self.carbs = 0
        self.fat = 0
        self.protein = 0

    def aggregate_nutrition(self):
        self.calories = self.recipes_df['calories'].sum()
        self.carbs += self.recipes_df['carbs'].sum()
        self.protein += self.recipes_df['protein'].sum()
        self.fat += self.recipes_df['fat'].sum()

    def calculate_nutrition_percentages(self):
        if self.calories == 0:
            self.carb_pct = 0
            self.fat_pct = 0
            self.protein_pct = 0
        else:
            # 1 kcal carb = 4 calories. Display percentage as decimal to 2 places.
            self.carb_pct = round((self.carbs * 4) / self.calories, 2)
            # 1 g protein = 4 calories
            self.protein_pct = round((self.protein * 4) / self.calories, 2)
            # 1 g fat = 9 calories.
            self.fat_pct = round((self.fat * 9) / self.calories, 2)

    def check_is_balanced_menu(self):
        self.balanced = (.45 <= self.carb_pct <= .65
                         and .25 <= self.fat_pct <= .35
                         and .1 <= self.protein_pct <= .3
                         and self.calories <= 1500)


class Recipe:
    def __init__(self):
        pass

    def add_to_my_recipes(self, df, user_name='master', csv='my_recipes.csv'):
        # csv = user_name + '_' + csv
        if 'calories' not in df \
                or 'carbs' not in df \
                or 'fat' not in df \
                or 'protein' not in df \
                or 'title' not in df \
                or 'url' not in df:
            return
        else:
            try:
                tmp_df = pd.read_csv(csv)
                tmp_df = pd.concat(objs=(tmp_df, df))
                tmp_df = tmp_df.drop_duplicates()
                tmp_df.to_csv(csv, index=False)
            except:
                df.to_csv(csv, index=False)

def clean_up_recipes(df):
    # blocked_words = ['dessert','cookie','muffin','cookie','pie', 'cake', 'bread', 'fish']
    approved_categories = ['dinner', 'main-dish', 'main dish', 'lunch', 'main course', 'unknown']
    # blocked_df = df[df['title'].apply(lambda x: any([k in x.lower() for k in blocked_words]))]
    blocked_df = df[df['category'].apply(lambda x: any([k in x.lower() for k in approved_categories])) == False]

    # block_recipe('cleaning up recipes ', blocked_df)
    block_recipe('non-dinner recipes', blocked_df)

def block_recipe(title, recipe: pd.DataFrame, user_name='master'):
    script_dir = os.path.dirname(__file__)
    print(script_dir)
    recipe_block_path = os.path.join(script_dir, '../recipe_scraper/recipe_scraper/spiders/master_blocked_recipes.csv')


    try:
        tmp_df = pd.read_csv(recipe_block_path)
        tmp_df = pd.concat(objs=(tmp_df, recipe))
        tmp_df = tmp_df.drop_duplicates()
        tmp_df.to_csv(recipe_block_path, index=False)
        print(title + ' added to blocked recipes list')


    except:
        recipe.to_csv(recipe_block_path, index=False)



        ## Take a recipe as a dataframe
        ## Add it to the user's blocked recipes file
        ## if no username was provided, it will default to a general master_blocked_recipes.csv

