import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Message boxes")
root.geometry("500x400")

def open_messagebox():
    # result = messagebox.showinfo("info title", "This is an information")
    # result = messagebox.showwarning("warning title", "This is a warning")
    # result = messagebox.showerror("error title", "This is an error")

    # label = ttk.Label(root, text=result)
    # label.pack()
    
    # value = tk.StringVar()
    # result = messagebox.askokcancel("sample title", "you are hacked")
    # if result==1:
    #     value.set("Click OK")
    # elif result==0:
    #     value.set("Click CANCEL")
    # label = ttk.Label(root, text=value.get())
    # label.pack()


    # result = messagebox.askquestion("sample title", "have you do it?")
    result = messagebox.askretrycancel("sample title", "something went wrong")

    label = ttk.Label(root, text=result)
    label.pack()

    


button = ttk.Button(root, text='Click me', command= open_messagebox)
button.pack()

root.mainloop()