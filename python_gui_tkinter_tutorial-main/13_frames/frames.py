import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Frames")
root.geometry("500x400")


frame = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')

entry = ttk.Entry(frame)
entry.pack(pady=10)

button = ttk.Button(frame, text='Submit')
button.pack()

frame2 = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
frame2.pack(side='bottom')

label2 = ttk.Label(frame2, text="Welcome")
label2.pack(pady=40)

button2 = ttk.Button(frame2, text='Submit')
button2.pack(pady=10, padx=10)


root.mainloop()