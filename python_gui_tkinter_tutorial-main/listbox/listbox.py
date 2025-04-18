import tkinter as tk
from tkinter import ttk
from calendar import month_name

root = tk.Tk()

root.title("ListBox")
root.geometry("300x200")

months = [month_name[m] for m in range(1, 13)]
selected_month = tk.StringVar()

def get_month_name(month_index):
    if(len(month_index) != 0):
        selected_month.set(f'Selected month is {months[month_index[0]]}')

listbox = tk.Listbox(root, height=6)
for idx, month in enumerate(months):
    listbox.insert(idx, month)
listbox.pack()

button = ttk.Button(root, text='Click me', command=lambda:get_month_name(listbox.curselection()))
button.pack()

label = ttk.Label(root, textvariable=selected_month)
label.pack()

root.mainloop()