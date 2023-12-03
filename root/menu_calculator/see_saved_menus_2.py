import os
import pandas as pd
import nutrition
import numpy as np
import menu_maker
import tkinter as tk
import matplotlib.pyplot as plt
import seaborn as sns

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

tmp_df['source'].value_counts()[:].plot(kind='bar')
plt.show()





