# ICS3UI-02 for Ms. Harris

# Mahdi Amini

# P.Conc: drawing in pygame

# Assignment NO: 2

# Question NO: 4


# date started: 02/29/2020
# date finished: 03/1/2020

# This program creates a landscape (grass, a picnic table, shelter, trees,
# sky with sun and cloud or clouds and rain)

import pygame
from random import randrange

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (249, 252, 91)
BLUE = (141, 234, 240)
LIGHT_BLUE = (184, 242, 250)
BROWN = (137, 107, 38)
DARK_BROWN = (83, 65, 25)
NIGHT = (14, 40, 147)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My backyard")

# pi number for
pi = 3.141592653

y = 50

sun_motion = 1

moon_motion = -800

n = 0

o = 0

day_time = 0

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

    # changing the light of the sky

    # #if sun passes 500 in x axis,the light of the sky starts to change to dark blue
    # and after the full dark the program stops

    if day_time < 500:
        screen.fill(LIGHT_BLUE)
    elif sun_motion > 500:
        screen.fill((184 - (n + o), 242 - n + o, 250 - n / 2 + o / 2))
        if o >= 0:
            n += 0.5
        if n == 183:
            o += 1
            break

    day_time += 1

    # drawing the house:
    pygame.draw.rect(screen, BROWN, [50, 350, 150, 150])  # drawing the walls of the house
    pygame.draw.rect(screen, DARK_BROWN, [100, 420, 50, 80])  # drawing the door
    pygame.draw.polygon(screen, DARK_BROWN, [[0, 350], [250, 350], [125, 250]])  # drawing the roof
    pygame.draw.circle(screen, WHITE, [80, 380], 29)
    pygame.draw.circle(screen, DARK_BROWN, [80, 380], 30, 3)

    # drawing grass in random places
    for i in range(1, 700, 2):
        pygame.draw.line(screen, GREEN, [i, 500], [i, randrange(480, 490)], 4)

    # drawing the sun and sunshine
    if 50 + sun_motion < 800:
        pygame.draw.circle(screen, YELLOW, [50 + sun_motion, 50], 50)
        pygame.draw.line(screen, YELLOW, [100 + sun_motion, 50], [randrange(110, 140) + sun_motion, 50], 2)
        pygame.draw.line(screen, YELLOW, [50 + sun_motion, 100], [50 + sun_motion, randrange(120, 140)], 2)
        pygame.draw.line(screen, YELLOW, [50 + sun_motion, 50], [randrange(100, 120) + sun_motion, randrange(100, 120)],
                         2)
        pygame.draw.line(screen, YELLOW, [50 + sun_motion, 50], [randrange(0, 5) + sun_motion, randrange(0, 5)], 2)
        pygame.draw.line(screen, YELLOW, [50 + sun_motion, 50], [50 + sun_motion, randrange(10, 40)], 2)
        pygame.draw.line(screen, YELLOW, [50 + sun_motion, 50], [randrange(0, 10) + sun_motion, randrange(100, 120)], 2)
        pygame.draw.line(screen, YELLOW, [50 + sun_motion, 50], [randrange(100, 120) + sun_motion, randrange(0, 10)], 2)
        pygame.draw.line(screen, YELLOW, [50 + sun_motion, 50], [randrange(0, 10) + sun_motion, randrange(50, 60)], 2)
    else:
        # drawing the moon
        pygame.draw.circle(screen, WHITE, [moon_motion, 50], 50)
        pygame.draw.circle(screen, (14, 40, 147), [moon_motion, 50], 50, 3)

    sun_motion += 1
    moon_motion += 1

    # drawing wind by using the arc in random places
    x = randrange(100)
    if x % 7 == 0:
        pygame.draw.arc(screen, BLUE, [400, 200, 85, 50], 2 * pi, pi, 2)
        pygame.draw.arc(screen, BLUE, [315, 200, 85, 50], pi, 2 * pi, 2)
        pygame.draw.arc(screen, BLUE, [230, 200, 85, 50], 2 * pi, pi, 2)
        pygame.draw.arc(screen, BLUE, [145, 200, 85, 50], pi, 2 * pi, 2)
    elif x % 11 == 0:
        pygame.draw.arc(screen, BLUE, [600, 100, 85, 50], 2 * pi, pi, 2)
        pygame.draw.arc(screen, BLUE, [515, 100, 85, 50], pi, 2 * pi, 2)
        pygame.draw.arc(screen, BLUE, [430, 100, 85, 50], 2 * pi, pi, 2)
        pygame.draw.arc(screen, BLUE, [345, 100, 85, 50], pi, 2 * pi, 2)

    # drawing the moving cloud
    pygame.draw.ellipse(screen, WHITE, [100 + y, 50, 150, 50])
    pygame.draw.ellipse(screen, BLUE, [100 + y, 50, 150, 50], 3)
    y += 10
    if y == 680:
        y = -100

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 10 frames per second
    clock.tick(40)

# Close the window and quit.
pygame.quit()
# the pygame template is being used from
# http://programarcadegames.com/python_examples/f.php?file=pygame_base_template.py
