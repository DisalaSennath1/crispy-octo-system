import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Radio Buttons')
root.geometry('300x200')

radio_var = tk.StringVar()

def radio_buttons_func():
    label.configure(text=radio_var.get())
  

radio1 = ttk.Radiobutton(root, text='Python', variable=radio_var, value='Python', command=radio_buttons_func)
radio1.pack()

radio2 = ttk.Radiobutton(root, text='Java', variable=radio_var, value='Java', command=radio_buttons_func)
radio2.pack()

radio3 = ttk.Radiobutton(root, text='C++', variable=radio_var, value='C++', command=radio_buttons_func)
radio3.pack()

label = ttk.Label(root)
label.pack()

root.mainloop()