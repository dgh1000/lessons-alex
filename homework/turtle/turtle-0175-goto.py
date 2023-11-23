# Topics covered
#
# 1) Using the goto command.

# Prerequisites: familiarity with basic turtle movement.

# Question #1
# Run this code. Notice the use of the goto command
# and see if you can figure out what it's doing.

from turtle import *

# bgcolor("black")
# color("cyan")
# speed(1)
# pensize(5)
# pendown()
# goto(100, 0)
# goto(100,100)
# goto(0,100)
# goto(0,0)
# penup()

# mainloop()

# Explanation: the goto command takes two arguments,
# which are the x and y coordinates of the point you
# want to go to. The x coordinate is the number of
# pixels from the center of the screen to the right, 
# and the y coordinate is the number of pixels from
# the center of the screen to the top. So goto(100, 0)
# goes to the right 100 pixels, and goto(0, 100) goes
# toward the top 100 pixels.

# Question #2
# 
# In the following code, there's a penup() before the
# first goto call. It won't draw a line when it goes
# to the first point. But it will draw lines when it
# goes to the other points.  
#
# Uncomment this code and run it. Then modify it and play
# around with the goto() command to draw other shapes.


# bgcolor("black")
# color("cyan")
# speed(1)
# pensize(5)
# penup()
# goto(100, 0)
# pendown()
# goto(100,100)
# goto(0,100)
# goto(0,0)
# penup()

# this is a triangle

# bgcolor("black")
# color("cyan")
# speed(1)
# pensize(5)
# pendown()
# goto(100, 0)
# goto(0, 100)
# goto(0, 0)

mainloop()

