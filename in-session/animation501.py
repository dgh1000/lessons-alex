from turtle import *

speed(0)
pendown()
hideturtle()
x_pos = 0
x_delta = 10
def draw():
    global x_pos
    global x_delta
    # clearscreen()
    dot(1000,"white")
    hideturtle()
    speed(0)
    x_pos += x_delta
    if x_pos > 400:
        x_pos = -400
    penup()
    goto(x_pos,0)
    pendown()
    forward(50)
    left(120)
    forward(50)
    left(120)
    forward(50)
    left(120)
    penup()
    # goto(0,0)
    # setheading(0)
    right(10)
    ontimer(draw, 100)

draw()
mainloop()
