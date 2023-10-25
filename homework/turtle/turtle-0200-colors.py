# PREREQUISITE: basic familiarity with drawing simple
# lines with turtle, including the following commands:
# forward, backward, left, right, penup, pendown, pensize

# EXPLANATION: this should be the first line of code
# in any turtle file. Don't put other code above it.
from turtle import *

# EXPLANATION: colors can be described with words.
# Those words are called "CSS color properties."
# (CSS is a term that comes from the web.) You
# can find a list of these names and their corresponding
# colors here: https://www.w3.org/wiki/CSS/Properties/color/keywords

# EXAMPLE A
bgcolor("navy")
color("red")

# EXPLANATION: the following line of code 
# gives the "pensize" which is the width of the
# line that the turtle draws. The number is in pixels.
pensize(5)

# Question #1:

# Write turtle code to draw a shape. Using color names
# from the link above, modify the code in EXAMPLE A
# to draw a shape with a different background color
# and a different line color.

# Answer: 
pendown()
forward(100)
left(90)
color("peachpuff")
forward(100)
left(90)
color("salmon")
forward(100)
left(90)
color("silver")
forward(100)
left(90)

# Question #2:
# Draw a shape that has a different color and pensize for
# every line. 

# Don't forget to put this line at the end of your file.
mainloop()


