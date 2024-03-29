import pandas as pd
import os
from datetime import date, timedelta

class Recipe:
    def __init__(self, recipe_df, calories=0, carbs=0, protein=0, fat=0):
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.recipe_df = recipe_df
        pass

    def add_to_my_recipes(self, df, user_name='master'):
        for column in ['title', 'url', 'category', 'source',
                       'calories', 'carbs', 'fat', 'protein',
                       'rating', 'reviewCount']:
            if (df[column] == '')[0]:
                print('missing ' + column)
                return 'missing'
        else:
            script_dir = os.path.dirname(__file__)
            csv = os.path.join(script_dir, 'my_recipes.csv')
            try:
                tmp_df = pd.read_csv(csv)
                tmp_df = pd.concat(objs=(tmp_df, df))
                tmp_df = tmp_df.drop_duplicates()
                tmp_df.to_csv(csv, index=False)
            except:
                df.to_csv(csv, index=False)


class Menu(Recipe):
    def __init__(self, balanced=False):
        self.balanced = balanced
        self.carb_pct = 100
        self.protein_pct = 100
        self.fat_pct = 100
        self.recipes_df = []
        self.empty = False
        self.is_vegetarian = False
        self.is_vegan = False
        self.calories_high = 3000
        self.calories_low = 1000
        self.carb_pct_high = .65
        self.carb_pct_low = .45
        self.fat_pct_high = .35
        self.fat_pct_low = .25
        self.protein_pct_high = .3
        self.protein_pct_low = .1
        # self.recipes = self.recipes_df[self.recipes_df['title']]
        pass

    def reset_nutrition(self):
        self.calories = 0
        self.carbs = 0
        self.fat = 0
        self.protein = 0

    def reset_nutrition_targets(self):
        # print('reset nutrition function called in class successfully')
        self.calories_high = 3000
        self.calories_low = 1000
        self.carb_pct_high = .65
        self.carb_pct_low = .45
        self.fat_pct_high = .35
        self.fat_pct_low = .25
        self.protein_pct_high = .3
        self.protein_pct_low = .1

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
        self.balanced = (self.carb_pct_low <= self.carb_pct <= self.carb_pct_high
                         and self.fat_pct_low <= self.fat_pct <= self.fat_pct_high
                         and self.protein_pct_low <= self.protein_pct <= self.protein_pct_high
                         and self.calories_low <= self.calories <= self.calories_high)


    def save_menu(self):
        today = date.today()
        year, week_num, day_of_week = today.isocalendar()
        # if day_of_week is 4,5,6,7 then go to 7. If day_of_week is 1,2,3 then go to 0.
        if day_of_week in [1, 2, 3]:
            start_of_week = today - timedelta(days=day_of_week)
        else:

            start_of_week = today + timedelta(days=(7 - day_of_week))
        # convert to string for comparing to dataframe
        start_of_week = str(start_of_week)
        # Only save the kept recipes
        save_menu_df = self.recipes_df[self.recipes_df['keep'] == True]

        # 1) Check that the number of kept recipes is greater than 0
        if len(save_menu_df) == 0:
            print("can't save an empty menu")
            return
        # Set a date column equal to the start date marking the Sunday the menu is applicable for.
        save_menu_df['date'] = start_of_week
        script_dir = os.path.dirname(__file__)
        csv_path = os.path.join(script_dir, 'recipe_log.csv')

        user_input = True

        # If this is the first saved recipe, create the csv and close
        try:
            tmp_df = pd.read_csv(csv_path)

            # 2) Check if the start_of_week is already in the csv
            if max(tmp_df['date'] == str(start_of_week)):
                # get user input to overwrite or pass
                print('check if user wants to overwrite this date')
                user_response = ''
                while user_response not in ('Y', 'N', 'y', 'n'):
                    # Do I want this to be a pop-up tkinter message box?
                    user_response = input(
                        'A menu exists for ' + start_of_week + ' already. Do you want to overwrite it? (Y/N): ')
                if user_response in ('Y', 'y'):
                    print('user will overwrite the data')
                    tmp_df = tmp_df[tmp_df['date'] != start_of_week]
                    tmp_df = pd.concat(objs=(tmp_df, save_menu_df))
                    tmp_df.to_csv(csv_path, index=False)
                    return
                else:
                    print('user will keep the old data')
                    return
            else:
                # start of week is not in the csv
                try:
                    tmp_df = pd.concat(objs=(tmp_df, save_menu_df))
                    tmp_df.to_csv(csv_path, index=False)
                except:
                    save_menu_df.to_csv(csv_path, index=False)
                    pass

        except:
            save_menu_df.to_csv(csv_path, index=False)
        print('menu saved for', start_of_week)


def clean_up_recipes(df):
    # blocked_words = ['dessert', 'cookie', 'muffin', 'cookie', 'pie', 'cake', 'bread', 'fish']
    approved_categories = ['dinner', 'main-dish', 'main dish', 'lunch', 'main course', 'supper', 'unknown']
    blocked_categories = ['breakfast', 'brunch', 'cocktails', 'dessert', 'desserts', 'drink',
                          'snack', 'starter', 'treat']
    blocked_df = df[df['category'].apply(lambda x: any([k in x.lower() for k in blocked_categories]))]
    blocked_df_2 = df[df['category'].apply(lambda x: any([k in x.lower() for k in approved_categories])) == False]

    block_recipe('cleaning up blocked word recipes ', blocked_df)
    block_recipe('non-dinner recipes', blocked_df_2)


def block_recipe(title, recipe: pd.DataFrame, user_name='master'):
    script_dir = os.path.dirname(__file__)
    # print(script_dir)
    recipe_block_path = os.path.join(script_dir,
                                     '../recipe_scraper/recipe_scraper/spiders/master_blocked_recipes.csv')

    try:
        tmp_df = pd.read_csv(recipe_block_path)
        tmp_df = pd.concat(objs=(tmp_df, recipe))
        tmp_df = tmp_df.drop_duplicates()
        tmp_df.to_csv(recipe_block_path, index=False)
        print(title + ' added to blocked recipes list')
    except:
        recipe.to_csv(recipe_block_path, index=False)

        # Take a recipe as a dataframe
        # Add it to the user's blocked recipes file
        # if no username was provided, it will default to a general master_blocked_recipes.csv
