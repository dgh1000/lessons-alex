# PREREQUISTE: basic familiarity with drawing simple
# lines with turtle, including the following commands:
# forward, backward, left, right, penup, pendown, pensize

# EXPLANATION: this should be the first line of code
# in any turtle file. Don't put other code above it.
from turtle import *
from colorsys import *

# importing colorsys gives us access to a function
# called hsv_to_rgb. We will use this function to
# convert from hsv colors to rgb colors.

# EXPLANATION: colors can be described with words
# as we saw in turtle-0200-colors.py. But they can
# also be described with numbers. Specifically, they
# can be described with three numbers between 0.0 and 1.0.
# Note that we will use decimals, not integers, to specify
# these numbers.
# The first number is the amount of red, the second
# number is the amount of green, and the third number
# is the amount of blue. For example, the color black
# is described with the numbers 0, 0, 0 because there
# is no red, no green, and no blue. The color white
# is described with the numbers 255, 255, 255 because
# there is the maximum amount of red, the maximum
# amount of green, and the maximum amount of blue.
# The color red is described with the numbers 255, 0, 0
# because there is the maximum amount of red, no green,
# and no blue. 

# EXAMPLE A: run the file with just this code and see what
# it does.
# bgcolor(0.0, 0.0, 0.0) # black
# color(1.0, 0.25, 0.0)   # white 
# HSV stands for hue, saturation, and value.
rgb_color = hsv_to_rgb(27/255, 0.4, 1.0)
color(rgb_color)
pensize(10)
pendown()
forward(100)

# Question #1:
# Now modify the line color (the color specified by
# the color command in EXAMPLE A) to be red. Hint:
# you will change the first number. 

# Question #2:
# Now modify the line color to be green. Hint: you
# will change the second number.

# Question #3:
# Now modify the line color to be blue. Hint: you
# will change the third number.

# Question #4:
# Now modify the line color to be something that's not
# exactly red, blue or green. You will change two of the
# numbers. For example, you could change the red and the 
# blue numbers.

# Question #5:
# Now modify the background color (the color specified
# by the bgcolor command in EXAMPLE A) to be red.

# Question #6:
# Now play with anything you like, changing the line
# color, the background color, and the pensize.
# Perhaps make a shape with different colors for each
# line.

mainloop()

