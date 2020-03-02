# Mahdi Amini
# P.Conc: drawing in pygame

# Assignment NO: 2

# Question NO: 4

# this program draw the Canada flag and red stars in random spots


from turtle import *
from random import randint


def rand_star():
    "drawing stars in random places"
    up()
    color("red", "yellow") # the color of stars is red

    while True:
        goto(randint(-200, 200), randint(-200, 200))  # go to random spots
        for i in range(15):  # drawing 15 stars in random spots
            speed(9)
            down()
            begin_fill()
            forward(20)
            left(170)
            end_fill()
        up()


# change the color to red
color('red', 'red')
# change the shape of the turtle to turtle
shape("turtle")
# the beginning of the coloring part
begin_fill()

up()  # not to draw any thing
goto(-60, -60)  # go to the position
down()  # start drawing
left(90)  # drawing the left side og the flag
forward(120)
left(90)
forward(60)
left(90)
forward(120)
left(90)
forward(60)
end_fill()  # coloring the rectangle
up()  # not draw any thing
goto(180, -60)  # move to other position
down()  # drawing the right side of the flag
begin_fill()
left(90)
forward(120)
left(90)
forward(60)
left(90)
forward(120)
left(90)
forward(60)
end_fill()  # coloring the rectangle
up()  # not draw any thing
goto(40, -60)  # move to logo position
down()  # start drawing the logo
begin_fill()
forward(6)
left(100)
forward(30)
right(120)
forward(20)
left(105)
forward(10)
right(45)
forward(50)
left(120)
forward(10)
right(100)
forward(20)
left(120)
forward(20)
right(80)
forward(10)
left(120)
forward(27)
right(135)
forward(40)
left(135)
forward(15)
right(100)
forward(30)
left(120)
forward(30)
right(110)
forward(15)
left(145)
forward(40)
right(130)
forward(27)
left(130)
forward(10)
right(90)
forward(20)
left(110)
forward(20)
right(100)
forward(10)
left(125)
forward(50)
right(50)
forward(10)
left(120)
forward(20)
right(125)
forward(30)
goto(40, -60)
end_fill()  # color the logo
hideturtle()  # the the drawing turtle
rand_star()  # calling the function rand_star
done()  # finish the process
