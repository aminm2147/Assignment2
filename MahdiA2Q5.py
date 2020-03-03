# ICS3UI-02 for Ms. Harris

# Mahdi Amini

# P.Conc: function in pygame

# Assignment NO: 2

# Question NO: 5


# date started: 02/29/2020
# date finished: 03/1/2020

# this program demonstrates some functions in pygame


import pygame
from random import randint


def cube_building(x_coordinate, y_coordinate):
    pygame.draw.rect(screen, GREEN, [x_coordinate, y_coordinate, 50, 50], 1)
    pygame.draw.line(screen, GREEN, [x_coordinate, y_coordinate], [x_coordinate + 20, y_coordinate - 20], 1)
    pygame.draw.line(screen, GREEN, [x_coordinate + 50, y_coordinate], [x_coordinate + 70, y_coordinate - 20], 1)
    pygame.draw.line(screen, GREEN, [x_coordinate + 20, y_coordinate - 20], [x_coordinate + 70, y_coordinate - 20], 1)
    pygame.draw.line(screen, GREEN, [x_coordinate + 50, y_coordinate + 50], [x_coordinate + 70, y_coordinate + 30], 1)
    pygame.draw.line(screen, GREEN, [x_coordinate + 70, y_coordinate + 30], [x_coordinate + 70, y_coordinate - 20], 1)


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My functions")

# pi number for circle
pi = 3.141592653


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)

    x = randint(0, 650)  # get a random number for
    y = randint(0, 450)
    cube_building(x, y)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 10 frames per second
    clock.tick(1)

# Close the window and quit.
pygame.quit()
# the pygame template is being used from
# http://programarcadegames.com/python_examples/f.php?file=pygame_base_template.py
