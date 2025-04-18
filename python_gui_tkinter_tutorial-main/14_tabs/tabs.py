import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tabs")
root.geometry("500x400")

def add_name(name):
    table.insert('', index=tk.END, values=(name.get()))
    entry_name.set('')

################### NOTEBOOK

notebook = ttk.Notebook(root)


################### TAB 01
frame1 = ttk.Frame(notebook, width=200, height=100, relief=tk.GROOVE)
frame1.pack_propagate(False)
frame1.pack()

entry_name = tk.StringVar()

entry = ttk.Entry(frame1, textvariable=entry_name)
entry.pack(pady=10)

button = ttk.Button(frame1, text='Submit', command=lambda: add_name(entry_name))
button.pack()

################### TAB 02
frame2 = ttk.Frame(notebook, width=200, height=100, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack()

table = ttk.Treeview(frame2, columns=('names'), show='headings')
table.column('names', width=198)
table.heading('names', text='Names')
table.pack()

# names = ["kamal", "saman"]
# for idx, value in enumerate(names):
#     table.insert('', index=idx, values=(names[idx]))

###################

notebook.add(frame1, text="Input")
notebook.add(frame2, text="Output")
notebook.pack()


root.mainloop()