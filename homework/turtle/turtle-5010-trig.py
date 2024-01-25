# This program shows another way to move a drawing in a 
# circle. Imagine that we are going around a circle.
# We've already seen how to do that by navigating the 
# turtle around a circle.
#
# Below you will see a comment that starts "THESE TWO LINES
# COMPUTE THE COORDINATES OF A CIRCLE."
#
# These lines are a way of computing the x and
# y coordinates of a circle. By slight modifications
# we can actually draw other rounded shapes besides
# circles. 
#
# Step 1: run this program and see what it does.
#
# Step 2: Change the hue of the square as the drawing
#  goes around the circle. This will involve creating a 
#  hue variable, importing colorsys, using an if statement
#  to keep the hue from getting too big, and so on. Follow
#  what we did in class on Jan. 24.
#
# Step 3: follow the comments below.
#
# Step 4: try drawing other shapes. Try drawing lines 
# from the ceneter out to the squares. Maybe remove
# the penup() and pendown() around the goto().

import math
from turtle import *
bgcolor("black")
color("white")
angle = 0
hideturtle()
speed(0)
def draw():
    global angle
    angle += 0.1
    # clearscreen()
    # hideturtle()
    length = 200
    # THESE TWO LINES COMPUTE THE COORDINATES
    # OF A CIRCLE. Suggestions to try in step 3:
    # change 'angle' on the first or second line
    # to say '2*angle'. Or '3*angle'. What if you
    # make one of them 2*angle and the other one
    # 3*angle ?
    x = length * math.cos(angle)
    y = length * math.sin(angle)
    penup()
    goto(x, y)
    pendown()
    square_length = 10
    forward(square_length)
    left(90)
    forward(square_length)
    left(90)
    forward(square_length)
    left(90)
    forward(square_length)
    left(90)
    ontimer(draw, 10)

draw()
mainloop()
