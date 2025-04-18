from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class snake :
    pass

class food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def collisions():
    pass

def game_over():
    pass

#******* def is end.


window = Tk()



window.title("Snek Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text = "score:{}".format(score), font = ('consolas', 45))
label.pack() 

Canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
Canvas.pack()

window.update()

window_width = window.winfo_width()
window.height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()



window.mainloop()






