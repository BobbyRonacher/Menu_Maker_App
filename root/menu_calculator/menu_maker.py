import pandas as pd
import nutrition
import random as rand
import os
import copy

# num_recipes = 0
recipes_needed = 4


def get_all_recipes():
    # https://qr.ae/prwWFb
    script_dir = os.path.dirname(__file__)
    recipe_df_path = os.path.join(script_dir, '../recipe_scraper/recipe_scraper/spiders/recipes.csv')
    recipe_block_path = os.path.join(script_dir,
                                     '../recipe_scraper/recipe_scraper/spiders/master_blocked_recipes.csv')
    my_recipe_df_path = os.path.join(script_dir, 'my_recipes.csv')

    recipe_df = pd.read_csv(recipe_df_path)

    nutrition.clean_up_recipes(recipe_df)
    block_df = pd.read_csv(recipe_block_path)
    # merge two DataFrames and create indicator column
    df_all = recipe_df.merge(block_df.drop_duplicates(),
                             on=['calories', 'carbs', 'fat', 'nutrition', 'protein', 'rating', 'reviewCount', 'source',
                                 'title', 'url', 'category'],
                             how='left', indicator=True)

    # create DataFrame with rows that exist in first DataFrame only
    unblock_recipe_df = df_all[df_all['_merge'] == 'left_only']
    # Need to reset the index so when the index of blocked recipes comes up
    # as a random number it does not error
    unblock_recipe_df = unblock_recipe_df.drop('_merge', axis=1).reset_index()


    try:
        my_recipe_df = pd.read_csv(my_recipe_df_path)
        unblock_recipe_df = pd.concat(objs=(my_recipe_df, unblock_recipe_df))
        unblock_recipe_df = unblock_recipe_df.reset_index(drop=True).drop(columns='index')
    except:
        pass

    # return a df that is rows from recipe_df that aren't in block_df
    return unblock_recipe_df

def select_recipes(titles, indexes):
    # with a list of titles and indexes, this creates a new list of the titles at those indexes
    output = []
    for index in indexes:
        output.append(titles[index])
    return output


def make_menu(df):
    menu = nutrition.Menu()
    get_menu_with_recipes(menu, df)
    return menu


def update_menu(menu, df):
    print('menu being updated')
    menu.recipes_df = menu.recipes_df.loc[menu.recipes_df['keep'] == True]
    menu.aggregate_nutrition()
    menu.calculate_nutrition_percentages()
    menu.check_is_balanced_menu()
    get_menu_with_recipes(menu, df)
    return menu, df


def get_menu_with_recipes(menu, df):
    counter = 0
    while not menu.balanced and counter < 1000:
        try:
            # Set the keep df based on kept menu items
            keep_df = menu.recipes_df[menu.recipes_df['keep'] == True]
        except:
            keep_df = []
        menu.reset_nutrition()
        counter += 1
        num_recipes = len(df.index)
        titles = df['title']

        # new one
        recipe_indexes = []
        while len(recipe_indexes) < recipes_needed - len(keep_df):
            rand_num = rand.randint(0, num_recipes - 1)
            if rand_num not in recipe_indexes:
                recipe_indexes.append(rand_num)
        # print(recipe_indexes)
        week_recipes = select_recipes(titles, recipe_indexes)

        # https://www.dataquest.io/blog/settingwithcopywarning/ search  for .copy()
        new_df = df[df['title'].isin(week_recipes)].copy()
        new_df.loc[:, 'keep'] = False

        try:
            menu.recipes_df = pd.concat([keep_df, new_df])
        except:
            menu.recipes_df = new_df

        menu.aggregate_nutrition()
        menu.calculate_nutrition_percentages()
        menu.check_is_balanced_menu()

    # print('keep df:\n ', keep_df)
    # print('new df:\n ', new_df)
    print(f'menu created in {counter} attempts')
    return menu

def get_potential_options(menu):

    ##Create a list of menus where all kept recipes are included, and every other combination of other recipes if included.
    ##Exclude any menu that fails is_balanced_menu.
    try:
        # Set the keep df based on kept menu items
        keep_df = menu.recipes_df[menu.recipes_df['keep'] == True]
    except:
        keep_df = []

    df = get_all_recipes()
    titles = df['title']
    option_list = []

    if len(keep_df) == 3:
        for i in range(len(df) - len(keep_df) + 1):
            option_list.append(select_recipes(titles, [i])[0])
    else:
        return False

    return_list = []
    for option in option_list:

        temp_menu = copy.copy(menu)

        new_df = df[df['title'].isin([option])].copy()
        new_df.loc[:, 'keep'] = False

        temp_menu.recipes_df = pd.concat([keep_df, new_df])

        temp_menu.reset_nutrition()
        temp_menu.aggregate_nutrition()
        temp_menu.calculate_nutrition_percentages()
        temp_menu.check_is_balanced_menu()

        if temp_menu.balanced:
            return_list.append(option)
        else:
            pass

    print(option_list)
    print('Option List Generated Successfully')

    # print('option_list menu_maker', len(option_list))
    return return_list







def __main__(menu):
    # if menu is empty, make new menu.
    # is menu isn't empty, recalculate menu
    df = get_all_recipes()
    if menu.empty:
        menu = make_menu(df)
    elif len(menu.recipes_df[menu.recipes_df['keep'] == True]) == 4:
        print('No need to press that. Menu is full')
    else:
        update_menu(menu, df)
        # print('updated menu df')
        # print(menu.recipes_df)
    menu.recipes_df = menu.recipes_df.reset_index(drop=True)
    return df, menu
