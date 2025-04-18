import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Menu")
root.geometry("500x400")

hello_label = ttk.Label(root, text='Hello', background='orange')
welcome_label = ttk.Label(root, text='Welcome', background='yellow')

# pack ==========================================
# hello_label.pack(side='top', expand=True, fill='both')
# welcome_label.pack(side='top', expand=True, fill='x')

# grid ==========================================
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=2)
# root.columnconfigure(2, weight=2)
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)

# hello_label.grid(row=1, column=1, sticky='nsew')
# welcome_label.grid(row=0, column=2, rowspan=2, sticky='nsew')

# place ========================================
# hello_label.place(x=0, y=0)
# hello_label.place(x=100, y=100)
hello_label.place(x=100, y=100, width=100, height=100)
# welcome_label.place(relx=0, rely=0)
welcome_label.place(relx=0.6, rely=0.1, width=100, height=200)

root.mainloop()