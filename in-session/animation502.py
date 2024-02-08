from turtle import *
import colorsys

speed(0)
pendown()
hideturtle()
rotation = 1000
position = 0
hue = 0
value = 0.5
size = 1
def draw():
    global rotation
    global position
    global hue
    global value
    global size
    # turtle goes back to the middle, pointed
    #   to the right. we have to rotate by an
    #   increasing amount each time to keep
    #   going around the circle
    # clearscreen()
    hideturtle()
    bgcolor("black")
    hue += 0.01
    if hue > 1:
        hue = 0
    value += 0.1
    if value > 1:
        value = 0.5
    size += 1
    if size > 10:
        size = 1
    # c = colorsys.hsv_to_rgb(hue, 1.0, value)
    c = colorsys.hsv_to_rgb (0.1,1.0,0.3)
    color(c)
    speed(0)
    rotation = 10
    position += 3
    left(rotation)
    forward(position)
    width(size)
    # penup()
    # pendown()
    left(90)
    forward(10)
    right(135)
    forward(14)
    right(90)
    forward(14)
    right(135)
    forward(10)
    # 60 fps. 1000/60. 16 ms per frame
    # 10 fps 
    # 100 ms + 300 ms = 400 ms
    # 1000/400 ms 
    # 
    ontimer(draw, 1)

draw()
mainloop()
