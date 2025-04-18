import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Checkbox')
root.geometry('300x200')

# check1_var = tk.StringVar()
# check2_var = tk.StringVar()

label_var = tk.StringVar()
checkbox_values = [tk.StringVar(), tk.StringVar()]

def checkbox_results():
    output_str = "Selected languages: "
    for i in checkbox_values:
        output_str = output_str + i.get() +" "
    label_var.set(output_str)

check1 = ttk.Checkbutton(root, text='Python', variable=checkbox_values[0], onvalue='Python', offvalue="")
check1.pack()

check2 = ttk.Checkbutton(root, text='Java', variable=checkbox_values[1], onvalue='Java', offvalue="")
check2.pack()

button = ttk.Button(root, text="Click Me", command=checkbox_results)
button.pack()

label = ttk.Label(root, textvariable=label_var)
label.pack()

root.mainloop()