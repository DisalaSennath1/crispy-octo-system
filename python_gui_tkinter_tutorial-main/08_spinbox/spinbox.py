import tkinter as tk
from tkinter import ttk
from calendar import month_name

root = tk.Tk()

root.title("SpinBox")
root.geometry('300x200')

# spinbox_value = tk.IntVar(value=5)
# numbers = (1,2,3,4,5,6,7,8,9)
# spinbox = ttk.Spinbox(root, values=numbers, textvariable=spinbox_value)

# spinbox = ttk.Spinbox(root, from_=5, to=15)

# spinbox = ttk.Spinbox(root, from_=5, to=15, increment=2)

months = [month_name[m] for m in range(1, 13)]
spinbox_value = tk.StringVar(value=months[0])
spinbox = ttk.Spinbox(root, values=months, textvariable=spinbox_value)

spinbox.pack()

label = ttk.Label(root, textvariable=spinbox_value)
label.pack()

root.mainloop()