import tkinter as tk
from tkinter import *
import nutrition as n
import pandas as pd


def main(menu):
    def submit(menu_vars, entries):
        for i in range(len(menu_vars)):
            menu_vars[i] = entries[i].get()
        menu.calories_high = int(entries[0].get())
        menu.calories_low = int(entries[1].get())
        menu.carb_pct_high = float(entries[2].get())
        menu.carb_pct_low = float(entries[3].get())
        menu.fat_pct_high = float(entries[4].get())
        menu.fat_pct_low = float(entries[5].get())
        menu.protein_pct_high = float(entries[6].get())
        menu.protein_pct_low = float(entries[7].get())

    def reset_nutrition_targets(menu_vars, entries):
        # print('reset nutrition function called in form successfully')
        menu.reset_nutrition_targets()
        menu_vars = [menu.calories_high, menu.calories_low, menu.carb_pct_high, menu.carb_pct_low, menu.fat_pct_high,
                     menu.fat_pct_low, menu.protein_pct_high, menu.protein_pct_low, 4]
        for i in range(len(entries)):
            entries[i].delete(0, END)
            entries[i].insert(0, menu_vars[i])

    add_window = tk.Tk()
    frame_add = tk.Frame(master=add_window, relief=tk.SUNKEN, borderwidth=3)
    frame_add.pack()

    cal_max_text = tk.StringVar()
    cal_max_text.set(menu.calories_high)
    cal_min_text = tk.StringVar()
    cal_min_text.set(menu.calories_low)

    entry_calories_high = tk.Entry(master=frame_add, width=10)
    entry_calories_low = tk.Entry(master=frame_add, width=10)
    entry_carbs_low = tk.Entry(master=frame_add, width=10)
    entry_carbs_high = tk.Entry(master=frame_add, width=10)
    entry_protein_low = tk.Entry(master=frame_add, width=10)
    entry_protein_high = tk.Entry(master=frame_add, width=10)
    entry_fat_low = tk.Entry(master=frame_add, width=10)
    entry_fat_high = tk.Entry(master=frame_add, width=10)
    entry_num_recipes = tk.Entry(master=frame_add, width=10)
    text_calories_high = tk.Label(text="calories high", master=frame_add, fg="black", bg="white", height=1)
    text_calories_low = tk.Label(text="calories low", master=frame_add, fg="black", bg="white", height=1)
    text_carbs_low = tk.Label(text="carb percentage low", master=frame_add, fg="black", bg="white", height=1)
    text_carbs_high = tk.Label(text="carb percentage high", master=frame_add, fg="black", bg="white", height=1)
    text_protein_low = tk.Label(text="protein percentage low", master=frame_add, fg="black", bg="white", height=1)
    text_protein_high = tk.Label(text="protein percentage high", master=frame_add, fg="black", bg="white", height=1)
    text_fat_low = tk.Label(text="fat percentage low", master=frame_add, fg="black", bg="white", height=1)
    text_fat_high = tk.Label(text="fat percentage high", master=frame_add, fg="black", bg="white", height=1)
    text_num_recipes = tk.Label(text="number of recipes (1-4)", master=frame_add, fg="black", bg="white", height=1)


    menu_vars = [menu.calories_high, menu.calories_low, menu.carb_pct_high, menu.carb_pct_low, menu.fat_pct_high,
                 menu.fat_pct_low, menu.protein_pct_high, menu.protein_pct_low, 4]
    entries = [entry_calories_high, entry_calories_low, entry_carbs_low, entry_carbs_high, entry_fat_low,
               entry_fat_high,
               entry_protein_low, entry_protein_high, entry_num_recipes]

    for i in range(len(entries)):
        entries[i].insert(0, menu_vars[i])

    texts = [text_calories_high, text_calories_low, text_carbs_low, text_carbs_high, text_fat_low, text_fat_high,
             text_protein_low, text_protein_high, text_num_recipes]

    for i in range(len(entries)):
        entries[i].grid(row=i, column=1, sticky='nsew')
    for i in range(len(entries)):
        texts[i].grid(row=i, column=0, sticky='nsew')

    button_submit = tk.Button(master=frame_add, width=5, height=3, text='submit', command=lambda: submit(menu_vars, entries))
    button_submit.grid(row=len(entries) + 1, column=0, columnspan=2)
    button_reset_nutrition_targets = tk.Button(master=frame_add, width=5, height=3, text='reset', command=lambda: reset_nutrition_targets(menu_vars, entries))
    button_reset_nutrition_targets.grid(row=len(entries) + 1, column=2, columnspan=2)

    add_window.mainloop()
