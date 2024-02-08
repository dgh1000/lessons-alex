import math
from turtle import *

# bgcolor("black")
# color("white")
pensize(5)
speed(0)

# 1) global variable
angle = 0

def draw():
    global angle
    clearscreen()
    speed(0)
    angle += 0.03
    x = angle * 260
    y = 100 * abs(math.sin(x))
    penup()
    goto(x,y)
    pendown()
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    ontimer(draw, 10)

draw()
mainloop()
