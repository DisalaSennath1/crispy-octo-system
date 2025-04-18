import tkinter as tk
from tkinter import ttk
from calendar import month_name

root = tk.Tk()

root.title("Combobox")
root.geometry("300x200")

combo_var = tk.StringVar()

months = [month_name[m] for m in range(1, 13)]
print(months)

combobox = ttk.Combobox(root, values=months, textvariable=combo_var)
combobox.pack()

# combo_var.set(months[0])

label = ttk.Label(root, textvariable=combo_var)
label.pack()

root.mainloop()