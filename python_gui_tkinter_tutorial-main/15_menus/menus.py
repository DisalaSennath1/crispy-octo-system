import tkinter as tk

root = tk.Tk()
root.title("Menu")
root.geometry("500x400")

light_result = tk.StringVar(value='off')

# menu
menu = tk.Menu(root)

# sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command=lambda:print("New"))
file_menu.add_command(label='Open', command=lambda:print("Open"))
menu.add_cascade(label='File', menu=file_menu)

# sub menu
result_menu = tk.Menu(menu, tearoff=False)
result_menu.add_command(label='Display', command=lambda:print(light_result.get()))
result_menu.add_checkbutton(label='Light', onvalue='on', offvalue='off', variable=light_result)
menu.add_cascade(label='Options', menu=result_menu)

root.configure(menu=menu)

root.mainloop()