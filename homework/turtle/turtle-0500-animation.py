from turtle import *

# bgcolor("black")
# color("white")
pensize(5)
speed(0)

orientation = 0

def draw():
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
    ontimer(draw, 100)

draw()
mainloop()
