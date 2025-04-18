import tkinter as tk

root = tk.Tk()
root.title("Canvas")
root.geometry("500x400")

canvas = tk.Canvas(root, bg='white')
canvas.pack()

# =====================
# canvas.create_rectangle((10, 10, 100, 200), fill='gray') #(x1, y1, x2, y2)
# canvas.create_oval((110, 110, 200, 250), fill='green') #(x1, y1, x2, y2)
# canvas.create_polygon((255, 20, 260, 155, 340, 100), fill='blue') #(px1, py1, px2, py2, px3, py3)

# canvas.create_line((0, 0, 300, 250), fill='red', width=5) #(x1, y1, x2, y2)

# ==============
# brush_width = 1
# def draw(event):
#     x = event.x
#     y = event.y
#     canvas.create_oval((x-brush_width, y-brush_width, x+ brush_width, y+brush_width), fill='black')

# canvas.bind('<Motion>', draw)

# # =================
brush_width = 2
def start_drawing(event):
    # Start drawing when mouse button is pressed
    x = event.x
    y = event.y
    canvas.create_oval((x-brush_width, y-brush_width, x+ brush_width, y+brush_width), fill='black')
    canvas.bind('<B1-Motion>', draw)

def draw(event):
    # Continue drawing as long as mouse button is held down and moved
    x = event.x
    y = event.y
    canvas.create_oval((x-brush_width, y-brush_width, x+ brush_width, y+brush_width), fill='black')

def stop_drawing(event):
    # Stop drawing when mouse button is released
    canvas.unbind('<B1-Motion>')

canvas.bind('<Button-1>', start_drawing)
canvas.bind('<ButtonRelease-1>', stop_drawing)


root.mainloop()