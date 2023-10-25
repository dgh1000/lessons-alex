from turtle import *
# pendown()
# forward(100)
# penup()
# forward(100)
# left(90)
# pendown()
# forward(100)
# # always ends in mainloop
# mainloop()

bgcolor("black")
speed(0)
# pendown()
# for i in range(360):
#     forward(1)
#     left(1)

penup()
backward(150)
pendown()
red = 1.0
green = 0
blue = 0
color(red, green, blue)
for i in range(72):
    green += 0.01
    green = min(1.0, green)
    color(red, green, blue)
    forward(300)
    left(175)


mainloop()