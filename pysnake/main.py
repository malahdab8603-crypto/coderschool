from tkinter import *
import random

GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 60
SPACE_SIZE = 60
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    pass

class Food:

    def __init__(self):

        x= random.randint(0, GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y= random.randint(0, GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

def check_collisions():
    pass

def game_over():
    pass


window = Tk()
window.title("Snake")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=("Arial", 20))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

window.update()

window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width= window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int ((screen_width/2 - window_width/2))
y = int((screen_height/2 - window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()
window.mainloop()

