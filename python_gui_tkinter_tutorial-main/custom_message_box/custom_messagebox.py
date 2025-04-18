import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Message boxes")
root.geometry("500x400")

users = ["Kamal", "Saman"]

def set_welcome_message(value):
    if value == 'yes':
          welcome_label.configure(text=f"Welcome {users_menu.get()}")
    pop.destroy()
    
          

def verify_user():
    if(users_menu.get() != "Select User"):
        global pop
        pop = tk.Toplevel(root)
        pop.title("Confirmation")
        pop.grab_set()
        pop.geometry("300x200")

        pop_label = ttk.Label(pop, text=f"Are you {users_menu.get()} ?")
        pop_label.pack()

        popup_frame = ttk.Frame(pop)
        popup_frame.pack(pady=5)

        yes_button = ttk.Button(popup_frame, text='YES', command=lambda:set_welcome_message("yes"))
        yes_button.grid(row=0, column=0, padx=10)

        no_button = ttk.Button(popup_frame, text='NO',  command=lambda:set_welcome_message("no"))
        no_button.grid(row=0, column=1)
    else:
        messagebox.showinfo("Incorrect user", "Please find a correct user") 

users_menu = ttk.Combobox(root, values=users, state='readonly')
users_menu.set("Select User")
users_menu.pack()

submit_button = ttk.Button(root, text='Submit', command=verify_user)
submit_button.pack()

welcome_label = ttk.Label(root)
welcome_label.pack()

root.mainloop()