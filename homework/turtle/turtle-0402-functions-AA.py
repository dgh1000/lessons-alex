from turtle import *
speed(9)
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
# mainloop()
# Now let's put that code into a function called drawSquare.
# Here's the code. This is called a function definition.

# The function has a "def" at the beginning, followed by the
# name of the function, followed by a pair of parentheses,
# followed by a colon.  

# The body of the function is indented.  The body of the function
# is the code that will be executed when the function is called.
# (See below for how to add code that calls the function.)

# Code example 02:
def drawSquare():
    pendown()
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

def drawA(sc):
    pendown()
    left(70)
    forward(106 * sc)
    right(140)
    forward(106 * sc)
    right(180)
    forward(50 * sc)
    left(70)
    forward(40 * sc)
    left(70)
    penup()
    forward(50 * sc)
    left(110)

def drawhalfA():
    pendown()
    left(70)
    forward(50)
    right(140)
    forward(50)
    right(180)
    forward(25)
    left(70)
    forward(17.5)
    left(70)
    penup()
    forward(25)
    left(110)

def drawBold():
    penup()
    forward(25)
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

def drawB(sc):
    pendown()
    left(90)
    forward(100 * sc)
    right(90)
    forward(50 * sc)
    right(45)
    forward(25 * sc)
    right(45)
    forward(14 * sc)
    right(45)
    forward(25 * sc)
    right(45)
    forward(50 * sc)
    right(180)
    forward(50 * sc)
    right(45)
    forward(25 * sc)
    right(45)
    forward(15 * sc)
    right(45)
    forward(25 * sc)
    right(45)
    forward(50 * sc)
    right(180)

def drawC(sc):
    penup()
    forward(50 * sc)
    pendown()
    left(120)
    forward(60 * sc)
    right(70)
    forward(60 * sc)
    backward(60 * sc)
    right(-70)
    backward(60 * sc)
    left(-120)
    penup()
    backward(50 * sc)

def drawD(sc):
    pendown()
    left(90)
    forward(100 * sc)
    right(90)
    forward(30 * sc)
    right(30)
    forward(25 * sc)
    right(30)
    forward(25 * sc)
    right(30)
    forward(32 * sc)
    right(30)
    forward(25 * sc)
    right(30)
    forward(25 * sc)
    right(30)
    forward(30 * sc)
    right(180)

def drawP(sc):
    pendown()
    left(90)
    forward(100 * sc)
    right(90)
    forward(45 * sc)
    right(45)
    forward(30 * sc)
    right(45)
    forward(10 * sc)
    right(45)
    forward(30 * sc)
    right(45)
    forward(45 * sc)
    left(90)
    forward(48 * sc)
    right(270)

# Create a turtle file that has the turtle boilerplate plus code
# example 02 in it.  Now we have to add this line to the file
# AFTER the function definition. This is called CALLING THE
# FUNCTION.
# penup()
backward(300)
# pendown()
# drawA()
# forward(100)
# drawB()
# forward(70)
# drawA()
# forward(70)
# drawC()
# forward(100)
# drawB()
# forward(50)
# drawA()
# forward(100)
# drawD()

scale = 1
drawA(scale)
forward(100 * scale)
# drawD()
drawB(scale)
forward(100 * scale)
drawD(scale)
forward(100 * scale)
drawP(scale)
forward(100 * scale)
drawA(scale)
goto(-300,100 * scale)
pendown()
forward(500)
# drawSquare()
# right(10)
# drawSquare()
mainloop()
# Run this program.

# Question #2:
#
# Now modify the function to draw the letter A. 
# 
# 1) Decide what you will name the function. For example you
# could name it drawA(). Then change the code in the body of the
# function. Then call the function. Run your code and verify it
# works.

