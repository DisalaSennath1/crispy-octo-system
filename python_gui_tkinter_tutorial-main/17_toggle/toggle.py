import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Toggle")
root.geometry("500x400")

bulb_state = tk.BooleanVar(value=False)

# ============================================================

def change_state():
    if bulb_state.get():
        bulb.place_forget()
        bulb_state.set(False)
    else:
        bulb.configure(text='ON')
        bulb.place(relx=0.5, rely=0.4)
        bulb_state.set(True)

# switch button
switch = ttk.Button(root, text="Switch", command=change_state)
switch.pack(side='bottom', pady=20)

# label
bulb = ttk.Label()
bulb.place(relx=0.5, rely=0.4)

# ============================================================

# def change_state():
#     if bulb_state.get():
#         bulb.configure(text='OFF')
#         bulb_state.set(False)
#     else:
#         bulb.configure(text='ON')
#         bulb_state.set(True)

# # switch button
# switch = ttk.Button(root, text="Switch", command=change_state)
# switch.pack(side='bottom', pady=20)

# # label
# bulb = ttk.Label(text="OFF")
# bulb.place(relx=0.5, rely=0.4)

# ============================================================

root.mainloop()