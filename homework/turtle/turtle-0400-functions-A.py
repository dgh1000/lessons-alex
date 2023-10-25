from turtle import *
speed(9)
# Prequisites: basic familiarity with turtle graphics
# including commands like forward, backward, left, right,
# penup, pendown, speed, and color.

# Topics Covered:
# 1) Drawing letters in preparation for turning them into
#    functions.

# Question #1:
#
# Write a turtle graphics program that draws the letter A.
# # draw C
pendown()
left(120)
forward(60)
right(70)
forward(60)
backward(60)
right(-70)
backward(60)
left(-120)

penup()
forward(100)
# run mainloop

# draw A

pendown()
left(70)
forward(100)
right(140)
forward(100)
right(180)
forward(50)
left(70)
forward(35)
left(70)
penup()
forward(50)
left(110)

# Question #2:
#
# Modify your program to draw the letter B also along with the
# letter A. (You can draw them in any order you want.)

# move in position for the next letter
penup()
forward(100)

# draw B
pendown()

left(90)
pendown()
forward(100)
right(120)
forward(50)
right(120)
forward(50)
left(120)
forward(50)
right(120)
forward(50)
left(150)

penup()
forward(100)

mainloop()

# Question #3:
#
# Now modify the program so that when it draws the A or B, it
# ends up at the same place facing the same direction it started.
# (Hint: you will need to use penup and pendown.)

