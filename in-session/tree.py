from turtle import*

penup()
goto(-25,-100)
pendown()
backward(50)

for i in range(5):
    backward(40)
    left(45)
    forward(80)
    right(45)

penup()
goto(-25,-100)
pendown()
forward(115)

for i in range(5):
    forward(40)
    right(45)
    backward(80)
    left(45)

penup()
goto(-5,-100)
pendown()

right(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)

# backward(50)
# left(45)
# forward(75)
# right(45)

# backward(50)
# left(45)
# forward(75)
# right(45)

mainloop()