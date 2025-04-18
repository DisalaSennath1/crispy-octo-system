import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Events")
root.geometry("300x200")

btn = ttk.Button(root, text="Click Me")
btn.pack()

# =========================
# root.bind('<Key>', lambda event: print("Hello"))

# ==========================
# # if any key pressed
# root.bind('<Key>', lambda event: print(event))

# ==========================
# # if any key pressed
# root.bind('<Alt-KeyPress-z>', lambda event: print(event))

# # ==========================
# root.bind('<Motion>', lambda event: print(event))

# # ==========================
# root.bind('<Enter>', lambda event: print(event))

# # ==========================
# root.bind('<Leave>', lambda event: print(event))

# # ==========================
# btn.bind('<Enter>', lambda event: print("Enter to button"))
# btn.bind('<Leave>', lambda event: print("Leave from button"))

# # ==========================
entry = ttk.Entry(root)
entry.pack()
entry.bind('<FocusIn>', lambda event: print("Entry field selected"))
entry.bind('<FocusOut>', lambda event: print("Entry field deselected"))

# run
root.mainloop()