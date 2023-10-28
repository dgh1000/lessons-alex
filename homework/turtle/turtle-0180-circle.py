# Topics covered:
#
# 1) Using the circle() function to draw circles.

# Prerequisites: familiarity basic turtle movement.

# Question #1
# Just run this code. Then figure out why it does what it does,
# and then modify it by playing around with colors, pensize,
# circle size, and circle position.

from turtle import *

bgcolor("black")
color("cyan")
speed(0)
penup()
forward(100)
pendown()
pensize(5)
for r in range(10, 201, 5):
    circle(r)
    right(85)

mainloop()
