import tkinter as tk

def create_entry_boxes(parent):
    entry_vars = {}
    for i in range(1, 6):
        label_text = f"Value {i}:"
        label = tk.Label(parent, text=label_text)
        label.grid(row=i, column=0)
        var = tk.StringVar()
        entry = tk.Entry(parent, textvariable=var)
        entry.grid(row=i, column=1)
        entry_vars[f"Value {i}"] = var
    return entry_vars

def print_entry_values(entry_vars):
    for key, value in entry_vars.items():
        print(key, value.get())

root = tk.Tk()
entry_vars = create_entry_boxes(root)
button = tk.Button(root, text="Print Entry Values", command=lambda: print_entry_values(entry_vars))
button.grid(row=6, column=0, columnspan=2)
root.mainloop()
