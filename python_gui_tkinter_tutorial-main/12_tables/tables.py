import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tree View")
root.geometry("500x400")

###########################
# table = ttk.Treeview(root)
# table.pack()

##########################
# table = ttk.Treeview(root, columns=('name', 'age', 'email'), show='headings')
# table.column('age', width=100)
# table.heading('name', text='Name')
# table.heading('age', text='Age')
# table.heading('email', text='Email')
# table.pack()

##########################
# table = ttk.Treeview(root, columns=('name', 'age', 'email'), show='headings')
# table.column('age', width=100)
# table.heading('name', text='Name')
# table.heading('age', text='Age')
# table.heading('email', text='Email')
# table.pack()

# table.insert('', index=0, values=('kamal', 23, 'kamal@gmail.com'))
# table.insert('', index=1, values=('saman', 54, 'saman@gmail.com'))

##########################
# table = ttk.Treeview(root, columns=('name', 'age', 'email'), show='headings')
# table.column('age', width=100)
# table.heading('name', text='Name')
# table.heading('age', text='Age')
# table.heading('email', text='Email')
# table.pack()

# names = ['Kamal', 'Saman', 'Nuwan', 'Gayan', 'Pawan']
# ages = [43, 54, 23, 23, 42]

# for idx, value in enumerate(names):
#     table.insert('', index=idx, values=(names[idx], ages[idx], f'{names[idx]}@gmail.com'))

##########################
# table = ttk.Treeview(root, columns=('name', 'age', 'email'), show='headings')
# table.column('age', width=100)
# table.heading('name', text='Name')
# table.heading('age', text='Age')
# table.heading('email', text='Email')
# table.pack()

# names = ['Kamal', 'Saman', 'Nuwan', 'Gayan', 'Pawan']
# ages = [43, 54, 23, 23, 42]

# for idx, value in enumerate(names):
#     table.insert('', index=idx, values=(names[idx], ages[idx], f'{names[idx]}@gmail.com'))

# def selected_item(event):
#     print(table.selection())
#     print(table.item(table.selection()))

# table.bind('<<TreeviewSelect>>', lambda event: selected_item(event))


##########################
table = ttk.Treeview(root, columns=('name', 'age', 'email'), show='headings')
table.column('age', width=100)
table.heading('name', text='Name')
table.heading('age', text='Age')
table.heading('email', text='Email')
table.pack()

label = ttk.Label(root)
label.pack()

names = ['Kamal', 'Saman', 'Nuwan', 'Gayan', 'Pawan']
ages = [43, 54, 23, 23, 42]

for idx, value in enumerate(names):
    table.insert('', index=idx, values=(names[idx], ages[idx], f'{names[idx]}@gmail.com'))

def selected_item(event):
    print(table.selection())
    print(table.item(table.selection()))
    label.configure(text=table.item(table.selection())['values'][0])

table.bind('<<TreeviewSelect>>', lambda event: selected_item(event))

root.mainloop()