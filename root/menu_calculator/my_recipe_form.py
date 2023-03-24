import tkinter as tk
from tkinter import *
import nutrition as n
import pandas as pd

def main():

    def submit():
        if entry_source.get() == '':
            entry_source.insert(0, 'myself')
        if entry_rating.get() == '':
            entry_rating.insert(0, 0)
        if entry_reviewCount.get() == '':
            entry_reviewCount.insert(0, 0)
        nutrition = {'calories': entry_calories.get(), 'carbs': entry_carbs.get(),
                     'protein': entry_protein.get(), 'fat': entry_fat.get()}
        d = {'calories': entry_calories.get(), 'carbs': entry_carbs.get(), 'category': entry_category.get(), 'fat': entry_fat.get(),
              'nutrition': str(nutrition), 'protein': entry_protein.get(), 'rating': entry_rating.get(),
              'reviewCount': entry_reviewCount.get(), 'source': entry_source.get(), 'title': entry_title.get(),
              'url': entry_url.get()}
        df = pd.DataFrame(data=d, index=[0])

        recipe = n.Recipe()
        submitted = recipe.add_to_my_recipes(df)

        if not submitted == 'missing':
            add_window.destroy()

    add_window = tk.Tk()
    frame_add = tk.Frame(master=add_window, relief=tk.SUNKEN, borderwidth=3)
    frame_add.pack()

    entry_title = tk.Entry(master=frame_add, width=10)
    entry_url = tk.Entry(master=frame_add, width=10)
    entry_category = tk.Entry(master=frame_add, width=10)
    entry_source = tk.Entry(master=frame_add, width=10)
    entry_calories = tk.Entry(master=frame_add, width=10)
    entry_carbs = tk.Entry(master=frame_add, width=10)
    entry_fat = tk.Entry(master=frame_add, width=10)
    entry_protein = tk.Entry(master=frame_add, width=10)
    entry_rating = tk.Entry(master=frame_add, width=10)
    entry_reviewCount = tk.Entry(master=frame_add, width=10)
    text_title = tk.Label(text="title", master=frame_add, fg="black", bg="white", width=10, height=1)
    text_url = tk.Label(text="url", master=frame_add, fg="black", bg="white", width=10, height=1)
    text_category = tk.Label(text="category", master=frame_add, fg="black", bg="white", width=10, height=1)
    text_source = tk.Label(text="source", master=frame_add, fg="black", bg="white", width=10, height=1)
    text_calories = tk.Label(text="calories", master=frame_add, fg="black", bg="white", width=10, height=1)
    text_carbs = tk.Label(text="carbs", master=frame_add, fg="black", bg="white", width=10, height=1)
    text_fat = tk.Label(text="fat", master=frame_add, fg="black", bg="white", width=10, height=1)
    text_protein = tk.Label(text="protein", master=frame_add, fg="black", bg="white", width=10, height=1)
    text_rating = tk.Label(text="rating", master=frame_add, fg="black", bg="white", width=10, height=1)
    text_reviewCount = tk.Label(text="reviewCount", master=frame_add, fg="black", bg="white", width=10, height=1)

    entries = [entry_title, entry_url, entry_category, entry_source, entry_calories, entry_carbs, entry_fat, entry_protein,
               entry_rating, entry_reviewCount]
    texts = [text_title, text_url, text_category, text_source, text_calories, text_carbs, text_fat, text_protein,
             text_rating, text_reviewCount]

    for i in range(len(entries)):
        entries[i].grid(row=i, column=1, sticky='nsew')
    for i in range(len(entries)):
        texts[i].grid(row=i, column=0, sticky='nsew')

    button_submit = tk.Button(master=frame_add, width=5, height=3, text='submit', command=submit)
    button_submit.grid(row=len(entries) + 1, column=0, columnspan=2)

    add_window.mainloop()