from turtle import *

speed(0)
pendown()
hideturtle()
rotation = 0
def draw():
    global rotation
    clearscreen()
    hideturtle()
    speed(0)
    rotation += 10
    left(rotation)
    # penup()
    forward(100)
    # pendown()
    left(90)
    forward(10)
    right(135)
    forward(14)
    right(90)
    forward(14)
    right(135)
    forward(10)
    ontimer(draw, 100)

draw()
mainloop()
