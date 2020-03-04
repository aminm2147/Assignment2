# ICS3UI-02 for Ms. Harris

# Mahdi Amini

# P.Conc: drawing in Turtle

# Assignment NO: 2

# Question NO: 3


# date started: 02/28/2020
# date finished: 02/29/2020

# this program draw a shape and fill its surrounding to a color from rainbow colors
# this program also delete every thing it just drew


import turtle
from turtle import *  # using turtle library
from random import randrange  # using random library and randint module


def undo_maker():  # defining a function to delete every things which have drawn
    for back in range(10000):
        turtle.undo()


def color_rainbow():  # defining a function to set the color to a random
    rancor = randrange(1, 8)
    if rancor == 1:
        turtle.color("#9400D3")  # color VIOLET
    if rancor == 2:
        turtle.color("#4B0082")  # color INDIGO
    if rancor == 3:
        turtle.color("#0000FF")  # color BLUE
    if rancor == 4:
        turtle.color("#00FF00")  # color GREEN
    if rancor == 5:
        turtle.color("#FFFF00")  # color YELLOW
    if rancor == 6:
        turtle.color("#FF7F00")  # color ORANGE
    if rancor == 7:
        turtle.color("#FF0000")  # color RED


#  set the color to light blue
turtle.color("#33cddb")
turtle.pencolor("black")  # set the color of the pen to black
turtle.shape("turtle")
for i in range(5):  # draw the inner 5 kites
    turtle.begin_fill()
    turtle.right(36)
    turtle.forward(50)
    turtle.right(72)
    turtle.forward(50)
    turtle.right(108)
    turtle.forward(50)
    turtle.right(72)
    turtle.forward(50)
    turtle.end_fill()

turtle.color("#269518")  # set the color to dark green
turtle.pencolor("black")  # set the color of the pen to black
for m in range(5):  # draw the outer 5 green kites
    turtle.begin_fill()
    turtle.right(36)
    turtle.forward(50)
    turtle.right(72)
    turtle.forward(50)
    turtle.left(144)
    turtle.forward(50)
    turtle.left(36)
    turtle.forward(50)
    turtle.left(144)
    turtle.forward(50)
    turtle.right(72)
    turtle.forward(50)
    turtle.end_fill()

for i in range(5):  # draw the surrounding kits in the color of rainbow
    turtle.right(36)
    turtle.right(72)
    turtle.forward(50)
    turtle.left(72)
    turtle.forward(50)
    turtle.right(144)
    turtle.forward(50)
    for j in range(2):
        color_rainbow()  # use the rainbow function which sets the color to a random color in rainbow
        turtle.pencolor("black")
        turtle.begin_fill()  # start the filling
        turtle.left(36)
        turtle.forward(50)
        turtle.right(72)
        turtle.forward(50)
        turtle.right(108)
        turtle.forward(50)
        turtle.right(72)
        turtle.forward(50)
        turtle.end_fill()  # finish the filling
    turtle.left(36)
    turtle.forward(50)
    turtle.right(144)
    turtle.forward(50)
    turtle.left(72)
    turtle.forward(50)

undo_maker()
turtle.write("bye", move=True, font=("Arial", 20, "normal"))  # write bye in the center of the screen

turtle.hideturtle()  # hide the shape of the drawing turtle

done()  # finish the process
