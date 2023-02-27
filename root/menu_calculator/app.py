import tkinter as tk
import pandas as pd
import menu_maker
import nutrition as n
import webbrowser

def make_new_recipes():
    global df, menu
    try:
        menu
    except:
        menu=pd.DataFrame({'A': []})
    df, menu = menu_maker.__main__(menu)
    recipes = menu.recipes_df
    recipe_1, recipe_2, recipe_3, recipe_4 = recipes.iloc[0]['title'], recipes.iloc[1]['title'], recipes.iloc[2]['title'], recipes.iloc[3][
        'title']
    url_1, url_2, url_3, url_4 = recipes.iloc[0]['url'], recipes.iloc[1]['url'], recipes.iloc[2]['url'], recipes.iloc[3][
        'url']
    calories, carbs, fat, protein = menu.calories, menu.carbs, menu.fat, menu.protein,
    nutrition_text = f'calories: {calories}\ncarbs: {carbs}\nfat: {fat}\nprotein: {protein}'

    label_recipe1_text.config(text=recipe_1)
    label_recipe2_text.config(text=recipe_2)
    label_recipe3_text.config(text=recipe_3)
    label_recipe4_text.config(text=recipe_4)
    label_recipe_1_url.config(text=url_1)
    label_recipe_2_url.config(text=url_2)
    label_recipe_3_url.config(text=url_3)
    label_recipe_4_url.config(text=url_4)
    label_recipe_1_url.bind("<Button-1>", lambda e: callback(label_recipe_1_url.cget("text")))
    label_recipe_2_url.bind("<Button-1>", lambda e: callback(label_recipe_2_url.cget("text")))
    label_recipe_3_url.bind("<Button-1>", lambda e: callback(label_recipe_3_url.cget("text")))
    label_recipe_4_url.bind("<Button-1>", lambda e: callback(label_recipe_4_url.cget("text")))

    label_nutrition.config(text=nutrition_text)

    if not menu.recipes_df.loc[0, 'keep']:
        button_keep_recipe_1.config(fg='white', bg='black')
    else:
        button_keep_recipe_1.config(fg='black', bg='blue')
    if not menu.recipes_df.loc[1, 'keep']:
        button_keep_recipe_2.config(fg='white', bg='black')
    else:
        button_keep_recipe_2.config(fg='black', bg='blue')
    if not menu.recipes_df.loc[2, 'keep']:
        button_keep_recipe_3.config(fg='white', bg='black')
    else:
        button_keep_recipe_3.config(fg='black', bg='blue')
    if not menu.recipes_df.loc[3, 'keep']:
        button_keep_recipe_4.config(fg='white', bg='black')
    else:
        button_keep_recipe_4.config(fg='black', bg='blue')

def keep_recipe(menu, num):
    num = num -1
    if menu.recipes_df.loc[num, 'keep'] == True:
        print(f'stop keeping recipe {num+1}')
        menu.recipes_df.loc[num, 'keep'] = False
        if num == 0:
            button_keep_recipe_1.config(fg='white', bg='black')
        elif num == 1:
            button_keep_recipe_2.config(fg='white', bg='black')
        elif num == 2:
            button_keep_recipe_3.config(fg='white', bg='black')
        elif num == 3:
            button_keep_recipe_4.config(fg='white', bg='black')
    else:
        print(f'keep recipe {num+1}')
        menu.recipes_df.loc[num, 'keep'] = True
        if num == 0:
            button_keep_recipe_1.config(fg='black', bg='blue')
        elif num == 1:
            button_keep_recipe_2.config(fg='black', bg='blue')
        elif num == 2:
            button_keep_recipe_3.config(fg='black', bg='blue')
        elif num == 3:
            button_keep_recipe_4.config(fg='black', bg='blue')
    return menu


def block_menu_recipe(title, df):
    def block_recipe(title, df):

        recipe_df = df[df['title'] == title].drop('index', axis=1)
        n.block_recipe(title, recipe_df)
        window2.destroy()

    window2 = tk.Tk()
    frame_block_screen = tk.Frame(window2, relief=tk.SUNKEN, borderwidth=3)
    frame_block_screen.pack()
    label_title = tk.Label(
        text="Block Recipe Form",
        master=frame_block_screen,
        font=('Helvetica 15 underline'),
        fg="black",  # Set the text color
        bg="white",  # Set the background color
    )
    button_submit = tk.Button(
        text="submit",
        master=frame_block_screen,
        bg="black",
        fg="white",
        command=lambda: block_recipe(title, df)
    )
    entry_title = tk.Entry(fg="yellow", master=frame_block_screen, bg="white")
    entry_note = tk.Entry(fg="yellow", master=frame_block_screen, bg="white")
    label_title.grid(row=0, column=0, sticky='nesw')
    entry_title.grid(row=2, column=0, sticky='nsew')
    entry_note.grid(row=3, column=0, sticky='nsew')
    button_submit.grid(row=4, column=0, sticky='ns')
    window.mainloop()

def callback(url):
   webbrowser.open_new_tab(url)


window = tk.Tk()
frame_main = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frame_main.pack()

label_title = tk.Label(
    text="Recipes",
    master=frame_main,
    font= ('Helvetica 15 underline'),
    fg="black",  # Set the text color
    bg="white",  # Set the background color
    width=10,  # set the width
    height=1  # set the height
)
label_url_header = tk.Label(
    text="URLs",
    master=frame_main,
    font= ('Helvetica 15 underline'),
    fg="black",  # Set the text color
    bg="white",  # Set the background color
)

label_recipe1 = tk.Label(
    text="Recipe1:",
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
#    width=10,  # set the width
    height=1  # set the height
)
label_recipe1_text = tk.Label(
    text='',
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
    height=1  # set the height
)
label_recipe_1_url = tk.Label(
    text='',
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
    height=1  # set the height
)
label_recipe2 = tk.Label(
    text="Recipe2:",
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
#    width=10,  # set the width
    height=1  # set the height
)
label_recipe2_text = tk.Label(
    text='',
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
    height=1  # set the height
)
label_recipe_2_url = tk.Label(
    text='',
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
    height=1  # set the height
)
label_recipe3 = tk.Label(
    text="Recipe3:",
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
#    width=10,  # set the width
    height=1  # set the height
)
label_recipe3_text = tk.Label(
    text='',
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
    height=1  # set the height
)
label_recipe_3_url = tk.Label(
    text='',
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
    height=1  # set the height
)
label_recipe4 = tk.Label(
    text="Recipe4:",
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
#    width=10,  # set the width
    height=1  # set the height
)
label_recipe4_text = tk.Label(
    text='',
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
    height=1  # set the height
)
label_recipe_4_url = tk.Label(
    text='',
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
    height=1  # set the height
)
button_keep_recipe_1 = tk.Button(
    text="Keep",
    master=frame_main,
    width=5,
    height=1,
    bg="black",
    fg="white",
    command=lambda: keep_recipe(menu, 1)
)
button_keep_recipe_2 = tk.Button(
    text="Keep",
    master=frame_main,
    width=5,
    height=1,
    bg="black",
    fg="white",
    command=lambda: keep_recipe(menu, 2)
)
button_keep_recipe_3 = tk.Button(
    text="Keep",
    master=frame_main,
    width=5,
    height=1,
    bg="black",
    fg="white",
    command=lambda: keep_recipe(menu, 3)
)
button_keep_recipe_4 = tk.Button(
    text="Keep",
    master=frame_main,
    width=5,
    height=1,
    bg="black",
    fg="white",
    command=lambda: keep_recipe(menu, 4)
)

button_drop_recipe_1 = tk.Button(
    text="Drop",
    master=frame_main,
    width=5,
    height=1,
    bg="black",
    fg="red",
    command=lambda: block_menu_recipe(label_recipe1_text.cget("text"), df)
)
button_drop_recipe_2 = tk.Button(
    text="Drop",
    master=frame_main,
    width=5,
    height=1,
    bg="black",
    fg="red",
    command=lambda: block_menu_recipe(label_recipe2_text.cget("text"), df)
)
button_drop_recipe_3 = tk.Button(
    text="Drop",
    master=frame_main,
    width=5,
    height=1,
    bg="black",
    fg="red",
    command=lambda: block_menu_recipe(label_recipe3_text.cget("text"), df)
)
button_drop_recipe_4 = tk.Button(
    text="Drop",
    master=frame_main,
    width=5,
    height=1,
    bg="black",
    fg="red",
    command=lambda: block_menu_recipe(label_recipe4_text.cget("text"), df)
)

label_nutrition = tk.Label(
    text='',
    master=frame_main,
    fg="black",  # Set the text color
    bg="white",  # Set the background color
)

# label_recipe1.pack(fill=tk.X)
# label_recipe2.pack(fill=tk.X)
# label_recipe3.pack(fill=tk.X)
# label_recipe4.pack(fill=tk.X)
# Define a function to show the popup message

button = tk.Button(
    text="Click me!",
    master=frame_main,
    width=25,
    height=5,
    bg="black",
    fg="white",
    command=make_new_recipes
)
entry = tk.Entry(fg="yellow",
    master=frame_main, bg="white")
label_title.grid(row=0, column=1, sticky='nesw')
label_url_header.grid(row=0, column=4, sticky='nesw')

label_recipe1.grid(row=1, column=0, sticky='nsew')
label_recipe1_text.grid(row=1, column=1, sticky='nsew')
button_keep_recipe_1.grid(row=1, column=2)
button_drop_recipe_1.grid(row=1, column=3)
label_recipe_1_url.grid(row=1, column=4, sticky='nsew')

label_recipe2.grid(row=2, column=0, sticky='nsew')
label_recipe2_text.grid(row=2, column=1, sticky='nsew')
button_keep_recipe_2.grid(row=2, column=2)
button_drop_recipe_2.grid(row=2, column=3)
label_recipe_2_url.grid(row=2, column=4, sticky='nsew')

label_recipe3.grid(row=3, column=0, sticky='nsew')
label_recipe3_text.grid(row=3, column=1, sticky='nsew')
button_keep_recipe_3.grid(row=3, column=2)
button_drop_recipe_3.grid(row=3, column=3)
label_recipe_3_url.grid(row=3, column=4, sticky='nsew')

label_recipe4.grid(row=4, column=0, sticky='nsew')
label_recipe4_text.grid(row=4, column=1, sticky='nsew')
button_keep_recipe_4.grid(row=4, column=2)
button_drop_recipe_4.grid(row=4, column=3)
label_recipe_4_url.grid(row=4, column=4, sticky='nsew')

label_nutrition.grid(row=5, column=1, columnspan=3, sticky='nsew')
button.grid(row=5, column=0)
# entry.grid(row=5, column=1, sticky= 'nesw')



make_new_recipes()
window.mainloop()


# tk colors https://www.tcl.tk/man/tcl/TkCmd/colors.html
# tk entry https://www.tutorialspoint.com/python/tk_entry.htm
## retrieve text with .get()
## delete text with .delete()
## insert text with .insert()



## grid(row, column, sticky)
# sticky options:
    #n or N- top-center e or E right-center s or S bottom center w or W left center
    # can combine letters ex. ne or nw