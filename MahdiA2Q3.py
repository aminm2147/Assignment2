
# ICS3UI-02 for Ms. Harris

# Mahdi Amini

# P.Conc: drawing in Turtle

# Assignment NO: 2

# Question NO: 3


# date started: 02/28/2020
# date finished: 02/29/2020

# this program draw the Canada flag and red stars in random spots
import turtle
from turtle import *  # using turtle library
from random import randint  # using random library and randint module


def rand_star():
    "drawing stars in random places except the flag position"
    turtle.up()
    turtle.color("red", "yellow")  # the color of stars is red

    while True:
        x = randint(-200, 200)
        y = randint(-200, 200)
        turtle.goto(x, y)  # go to random spots
        while True:  # not putting stars on the flag
            if 240 > x > -120 and 60 > y > 60:
                x = randint(-200, 200)
                y = randint(-200, 200)
            else:
                break
        for i in range(15):  # drawing 15 stars in random spots
            turtle.speed(9)
            turtle.down()  # start drawing
            turtle.begin_fill()
            turtle.forward(20)
            turtle.left(170)
            turtle.end_fill()
        turtle.up()  # do not draw any more


# change the color to red
turtle.color('red', 'red')
# change the shape of the turtle to turtle
turtle.shape("turtle")
# the beginning of the coloring part
turtle.begin_fill()
turtle.up()  # not to draw any thing
turtle.goto(-60, -60)  # go to the position
turtle.down()  # start drawing
turtle.left(90)  # drawing the left side og the flag
turtle.forward(120)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(60)
turtle.end_fill()  # coloring the rectangle
turtle.up()  # not draw any thing
turtle.goto(180, -60)  # move to other position
turtle.down()  # drawing the right side of the flag
turtle.begin_fill()
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(60)
turtle.end_fill()  # coloring the rectangle
turtle.up()  # not draw any thing
turtle.goto(40, -60)  # move to logo position
turtle.down()  # start drawing the logo
turtle.begin_fill()
turtle.forward(6)
turtle.left(100)
turtle.forward(30)
turtle.right(120)
turtle.forward(20)
turtle.left(105)
turtle.forward(10)
turtle.right(45)
turtle.forward(50)
turtle.left(120)
turtle.forward(10)
turtle.right(100)
turtle.forward(20)
turtle.left(120)
turtle.forward(20)
turtle.right(80)
turtle.forward(10)
turtle.left(120)
turtle.forward(27)
turtle.right(135)
turtle.forward(40)
turtle.left(135)
turtle.forward(15)
turtle.right(100)
turtle.forward(30)
turtle.left(120)
turtle.forward(30)
turtle.right(110)
turtle.forward(15)
turtle.left(145)
turtle.forward(40)
turtle.right(130)
turtle.forward(27)
turtle.left(130)
turtle.forward(10)
turtle.right(90)
turtle.forward(20)
turtle.left(110)
turtle.forward(20)
turtle.right(100)
turtle.forward(10)
turtle.left(125)
turtle.forward(50)
turtle.right(50)
turtle.forward(10)
turtle.left(120)
turtle.forward(20)
turtle.right(125)
turtle.forward(30)
turtle.goto(40, -60)
turtle.end_fill()  # color the logo
turtle.hideturtle()  # the the drawing turtle
rand_star()  # calling the function rand_star
done()  # finish the process
