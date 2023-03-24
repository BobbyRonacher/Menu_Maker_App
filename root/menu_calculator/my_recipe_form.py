import tkinter as tk
from tkinter import *
import nutrition as n
import pandas as pd

def main():
    def submit(add_window):
        nutrition = {'calories': recipe_data['calories'].get(), 'carbs': recipe_data['carbs'].get(),
                     'protein': recipe_data['protein'].get(), 'fat': recipe_data['fat'].get()}
        d = {'calories': recipe_data['calories'].get(), 'carbs': recipe_data['carbs'].get(), 'category': recipe_data['category'].get(),
             'fat': recipe_data['fat'].get(),
             'nutrition': str(nutrition), 'protein': recipe_data['protein'].get(), 'rating': recipe_data['rating'].get(),
             'reviewCount': recipe_data['reviewCount'].get(), 'source': recipe_data['source'].get(), 'title': recipe_data['title'].get(),
             'url': recipe_data['url'].get()}

        if d['source'] == '':
            d['source'] = 'myself'
        if d['rating'] == '':
            d['rating'] = 0
        if d['reviewCount'] == '':
            d['reviewCount'] = 0

        df = pd.DataFrame(data=d, index=[0])
        print(df)

        recipe = n.Recipe()
        submitted = recipe.add_to_my_recipes(df)
        if not submitted == 'missing':
            add_window.destroy()


    add_window = tk.Tk()
    recipe_data = {
        "title": tk.StringVar(),
        "url": tk.StringVar(),
        "category": tk.StringVar(),
        "source": tk.StringVar(),
        "calories": tk.StringVar(),
        "carbs": tk.StringVar(),
        "fat": tk.StringVar(),
        "protein": tk.StringVar(),
        "rating": tk.StringVar(),
        "reviewCount": tk.StringVar()
    }

    for i, field in enumerate(recipe_data):
        label = tk.Label(add_window, text=field.capitalize())
        label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)

        entry = tk.Entry(add_window, textvariable=recipe_data[field])
        entry.grid(row=i, column=1, padx=5, pady=5)

    button_submit = tk.Button(add_window, text='submit', width=5, height=3, command=lambda: submit(add_window))
    button_submit.grid(row=len(recipe_data), column=0, columnspan=2)


    add_window.mainloop()

if __name__ == "__main__":
    main()