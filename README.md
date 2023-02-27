# Menu_Maker_App

menu_calculator:
  The menu calculator is the core of the app's calculation.
  
  
  _cd_ to menU_calculator
  run _python app.py_
  
  app.py:
    This file runs the tkinter menu app.
    This app will come up with a macronutrient balanced menu of 4 recipes.
  
  menu_maker.py:
    This file pulls recipe data from recipes.csv and generates each menu
  
  nutrition.py:
    This file contains the menu and recipe classes as well as clean up and block recipe functions
    
    
    Criteria for a balanced menu:
      < 1500 calories
      Between 45% and 65% carbohydrate calories
      Between 25% and 35% fat calories
      Between 10% and 30% protein calories

recipe_scraper:
  Recipe scraper pulls public recipes from various websites to be used in the menu calculator
  
  _cd_ to _recipe_scraper/recipe_scraper/spiders_
  run _scrapy runspider taste_of_home.py & scrapy runspider hello_fresh.py & scrapy runspider food
_network.py & scrapy runspider delish.py_

  
