# Topics covered:
# 1) Putting turtle drawing command into functions.
# 2) Calling functions.
# 3) Moving the turtle between calls to functions.

# Prerequisites: familiarity with drawing letters 
# with the turtle. Familiarity with turtle boilerplate.

# Explanation A:
# 
# Let's take a first look at functions.  We'll start with
# functions that don't take any parameters and don't return
# any values.  We'll use turtle graphics to illustrate the
# concepts.
#
# Here's some turtle code that draws a square: (you will have
# to add the other code that goes in a turtle graphics program)

# Code example 01:
# pendown()
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)

# Now let's put that code into a function called drawSquare.
# Here's the code. This is called a function definition.

# The function has a "def" at the beginning, followed by the
# name of the function, followed by a pair of parentheses,
# followed by a colon.  

# The body of the function is indented.  The body of the function
# is the code that will be executed when the function is called.
# (See below for how to add code that calls the function.)

# Code example 02:
# def drawSquare():
#     pendown()
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)
#     forward(100)
#     left(90)

# Create a turtle file that has the turtle boilerplate plus code
# example 02 in it.  Now we have to add this line to the file
# AFTER the function definition. This is called CALLING THE
# FUNCTION.

# drawSquare()

# Run this program.

# Question #2:
#
# Now modify the function to draw the letter A. 
# 
# 1) Decide what you will name the function. For example you
# could name it drawA(). Then change the code in the body of the
# function. Then call the function. Run your code and verify it
# works.

