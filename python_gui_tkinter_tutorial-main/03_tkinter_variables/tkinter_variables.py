import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Variables')
root.geometry('300x200')

variable_value = tk.StringVar(value="hello")

def click_func():
    # print(entry.get())
    print(variable_value.get())

label = ttk.Label(root, textvariable=variable_value)
label.pack()

entry = ttk.Entry(root, textvariable=variable_value)
entry.pack()

button = ttk.Button(root, text="Click Me", command=lambda:click_func())
button.pack()

root.mainloop()