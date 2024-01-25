# Just play around with this.

# the important thing to be aware of is that
# numbers you pass into hsv_to_rgb() must be
# between 0.0 and 1.0. Here, x and y range between
# 0 and 400, so dividing by 400 puts the numbers into
# the range 0.0 and 1.0. If you change the ranges of
# x or y on lines 19 and 20, you must change the number
# you divide by on line 22.

import colorsys
from turtle import *

(r, g, b) = colorsys.hsv_to_rgb(0, 1, 0.5)
bgcolor("white")
color("black")
fillcolor((r, g, b))
speed(0)
pensize(1)
pendown()
penup()
for x in range(-300, 310, 20):
    goto(x, 0)
    (r, g, b) = colorsys.hsv_to_rgb((x + 300)/600, 1, 1)
    color((r, g, b))
    begin_fill()
    circle(10)
    end_fill()

for x in range(-300, 310, 20):
    goto(x, -30)
    (r, g, b) = colorsys.hsv_to_rgb((x + 300)/600,(x + 300)/600, 1)
    color((r, g, b))
    begin_fill()
    circle(10)
    end_fill()


# circle(100)
# for x in range(0, 400, 30):
#     for y in range(0, 400, 30):
#         (r, g, b) = colorsys.hsv_to_rgb(x / 400.0, y / 400.0, 1.0)
#         color(r, g, b)
#         penup()
#         goto(x, y)
#         pendown()
#         circle(10)

mainloop()
