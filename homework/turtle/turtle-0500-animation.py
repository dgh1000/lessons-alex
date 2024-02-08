from turtle import *

# bgcolor("black")
# color("white")
pensize(5)
speed(0)

# 1) global variable
orientation = 0

def draw():
    # 2) "global" statement
    global orientation
    clearscreen()
    speed(0)
    pensize(5)
    right(orientation)
    orientation += 10
    forward(150)
    left(90)
    forward(150)
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
