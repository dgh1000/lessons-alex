from turtle import *

speed(0)
pendown()
hideturtle()
x_pos = 0
def draw():
    global x_pos
    clearscreen()
    hideturtle()
    speed(0)
    x_pos += 10
    penup()
    goto(x_pos, 0)
    pendown()
    left(90)
    forward(10)
    right(45)
    forward(14)
    left(90)
    forward(14)
    left(45)
    forward(10)
    ontimer(draw, 100)

draw()
mainloop()
