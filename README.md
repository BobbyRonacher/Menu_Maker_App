# Menu_Maker_App

Setup:

cd to the root folder
run pip install -r requirements.txt
run python menu_calculator/app.py


menu_calculator:
  The menu calculator is the core of the app's calculation.
  
  app.py:
    This file runs the tkinter menu app.
    This app will come up with a macronutrient balanced menu of 4 recipes.
    When a menu is calculated, you can choose to keep or drop a recipe on that menu
      Kept recipes will stay when a menu is recalculated
      Dropped recipes will be added to blocked_recipes and will be excluded from all future menus
  
  menu_maker.py:
    This file pulls recipe data from recipes.csv and blocked_recipes.csv and generates each menu
    All potential recipes are ones in recipes.csv and not in blocked_recipes.csv
  
  nutrition.py:
    This file contains the menu and recipe classes as well as clean up and block recipe functions
   
    Criteria for a balanced menu:
      < 1500 calories
      Between 45% and 65% carbohydrate calories
      Between 25% and 35% fat calories
      Between 10% and 30% protein calories

recipe_scraper:
  Recipe scraper pulls public recipes from various websites to be used in the menu calculator
  Current websites are Delish, Hello Fresh, Taste of Home, and Food Network
  A recipe is saved if it contains all nutritional information, and has sufficient ratings/reviews
  
  To replenish recipes:
  1) delete the recipes.csv file in the spiders directory
  2) _cd_ to _recipe_scraper/recipe_scraper/spiders_
  3) run _scrapy runspider taste_of_home.py & scrapy runspider hello_fresh.py & scrapy runspider food_network.py & scrapy runspider delish.py_

  
  
  
  Future Ideas:
  
  * Log menus to track used recipes and trends
  * Only consider recipes that are considered main_dishes or dinners (others?)
