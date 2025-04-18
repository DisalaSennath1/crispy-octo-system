import tkinter as tk

# create a window
root = tk.Tk()

root.title('Hello World')
root.geometry('400x400') # widthxheight
root.iconbitmap('icon.ico')
root.resizable(False, False)
# run the window
root.mainloop()
print("Hello")
# if happen any event on widgets, we can see that because of mainloop
# mainloop stop only when close the app 