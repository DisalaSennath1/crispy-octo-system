import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("ListBox")
root.geometry("300x200")

# scale = ttk.Scale(root, command=lambda value:print(value))

# scale = ttk.Scale(root, command=lambda value:print(value), from_=0, to=100)

# scale = ttk.Scale(root, command=lambda value:print(value), from_=0, to=100, length=300)

# scale = ttk.Scale(root, command=lambda value:print(value), from_=0, to=100, length=300, orient="vertical")

scale_val = tk.DoubleVar(value=50)
scale = ttk.Scale(root, command=lambda value:print(value), from_=0, to=100, length=300, variable=scale_val)

scale.pack()

# progress_bar = ttk.Progressbar(root, value=30)

progress_bar = ttk.Progressbar(root, variable=scale_val)

# progress_bar = ttk.Progressbar(root, variable=scale_val, length=300)

progress_bar.pack()

root.mainloop()