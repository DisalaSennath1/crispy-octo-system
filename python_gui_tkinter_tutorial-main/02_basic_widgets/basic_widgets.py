import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Basic Widgets')
root.geometry('300x200')
root.iconbitmap('icon.ico')
root.resizable(False, False)

def button_click_func():
    # print("Hello")
    # print(entry.get())
    label.configure(text=entry.get())
    button.configure(state='disabled')

# create an entry
entry = ttk.Entry(root)
entry.pack(FileExistsError)

# create a button
button = ttk.Button(root, text='Click me', command=button_click_func)
button.pack()

# create a label
label = ttk.Label(root)
label.pack()

root.mainloop()