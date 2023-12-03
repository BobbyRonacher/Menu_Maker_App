import os
import pandas as pd
import nutrition
import numpy as np
import menu_maker
import tkinter as tk

script_dir = os.path.dirname(__file__)
# print(script_dir)
recipe_block_path = os.path.join(script_dir, 'recipe_log.csv')

try:
    tmp_df = pd.read_csv(recipe_block_path)
    tmp_df = tmp_df.drop(['index', 'keep'], axis=1)
    print('reading csvs')
    # print(tmp_df)
except:
    print('no saved csvs to read')
#
import matplotlib.pyplot as plt
import seaborn as sns

def sources_chart(df):
    sources = df.source.drop_duplicates()
    counts = df.source.value_counts()
    df.source.value_counts().plot(kind='bar')
    for i in range(len(sources)):
        plt.text(i, counts[i], counts[i])
    plt.show()

def nutrition_by_week(df):
    dates = df.date.drop_duplicates()
    calories = []
    carbs = []
    protein = []
    fat = []

    for date in dates:
        date_df = df[df['date'] == date]
        date_df_menu = nutrition.Menu()
        date_df_menu.recipes_df = date_df
        date_df_menu.reset_nutrition()
        date_df_menu.aggregate_nutrition()
        calories.append(date_df_menu.calories)
        carbs.append(date_df_menu.carbs)
        protein.append(date_df_menu.protein)
        fat.append(date_df_menu.fat)

    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=.175)
    index = np.arange(len(dates))
    bar_width = 0.2

    # Plot the bars for each nutrient
    ax.bar(index - bar_width, calories, bar_width, color='r', label='Calories')
    ax.bar(index, carbs, bar_width, color='g', label='Carbs')
    ax.bar(index + bar_width, protein, bar_width, color='b', label='Protein')
    ax.bar(index + 2 * bar_width, fat, bar_width, color='y', label='Fat')

    # Add labels and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_title('Nutrition Values by Date')
    ax.set_xticks(index)
    ax.set_xticklabels(dates, rotation=45)
    ax.legend()

    plt.show()

#Create a graphic of the last 9 weeks and list the recipes on each week
def last_nine_weeks(df):
    df['date'] = pd.to_datetime(df['date'])
    df['date_rank'] = df.date.rank(method='dense', ascending='False')
    df_top_9 = df[df['date_rank'] <= 9]
    dates = df_top_9.date.drop_duplicates().reset_index()

    root = tk.Tk()

    # create the frames
    frames = [[tk.Frame(root, borderwidth=2, relief="solid") for _ in range(3)] for _ in range(3)]

    # create the labels and add them to the frames
    for i in range(3):
        for j in range(3):
            try:
                date = dates.loc[3*i + j]['date']
                recipes = df_top_9[df_top_9['date'] == date]
                # print(date)
                # print(recipes)
                for k in range(len(recipes)+1):
                    if k == 0:
                        label = tk.Label(frames[i][j], text=f"Date {date}")
                        label.pack(side="top", padx=10, pady=5)
                    else:
                        recipe_title = recipes.iloc[k-1]['title']
                        label = tk.Label(frames[i][j], text=f"{recipe_title}")
                        label.pack(side="top", padx=10, pady=5)

            except:
                label = tk.Label(frames[i][j])
                label.pack(side="top", padx=10, pady=5)

    # place the frames in a 3x3 grid
    for i in range(3):
        for j in range(3):
            frames[i][j].grid(row=i, column=j, padx=10, pady=5)

    root.mainloop()

sources_chart(tmp_df)
# nutrition_by_week(tmp_df)
# last_nine_weeks(tmp_df)



#
# tmp_df['title'] = tmp_df['title'].str.replace(r'\?|\.|\'', ' ')
# list_of_words = ' '.join(tmp_df['title']).split()
# print(list_of_words)



