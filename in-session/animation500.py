from turtle import *

# bgcolor("black")
# color("white")
pensize(5)
speed(0)

# 1) global variable
x_pos = 0

def draw():
    # 2) "global" statement
    global x_pos
    # clearscreen resets all colors as well as
    # making the screen blank
    # position and orientation.
    clearscreen()
    bgcolor("black")
    color("white")
    speed(0)
    pensize(5)
    penup()
    forward(x_pos)
    x_pos += 10 
    side_length = 150
    pendown()
    forward(side_length)
    left(90)
    forward(side_length)
    left(90)
    forward(150)
    left(90)
    forward(150)
    # start a 100 millisecond timer
    # call draw again when t
    # he timer finishes
    # 3) a call to ontimer()
    ontimer(draw, 100)

draw()
mainloop()
