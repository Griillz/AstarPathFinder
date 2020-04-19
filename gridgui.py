import pygame
import random
from astarv1 import simplified_anytime
from init import *

changew = 10



numobstacles = int((gridsize * gridsize) * gridblocked)


grid = [[0 for x in range(gridsize)] for y in range(gridsize)]

setofobstacles = []
for i in range(numobstacles):
    x = random.randint(0, gridsize - 1)
    y = random.randint(0, gridsize - 1)
    if (x,y) not in setofobstacles and (x,y) != START and (x,y) != END:
        setofobstacles.append((x,y))
    else:
        i -= 1

for item in setofobstacles:
    grid[item[0]][item[1]] = 1

gridcopy = grid.copy()

pygame.init()



pygame.display.set_caption(("A* Shortest Pathfinder"))

done = False


# Set the screen background
screen.fill(BLACK)

# Draw the grid
for row in range(gridsize):
    for column in range(gridsize):
        color = WHITE
        if grid[row][column] == 1:
            color = BLACK
        elif (row,column) == START:
            color = GREEN
        elif (row,column) == END:
            color = RED
        pygame.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

pygame.display.flip()

path = simplified_anytime(START, END, grid, w, changew, gridsize - 1, gridcopy)
# print("what the fuck")
# while not done:
#     for event in pygame.event.get():  # User did something
#         if event.type == pygame.QUIT:  # If user clicked close
#             done = True  # Flag that we are done so we exit this loop
#
#
#     # Go ahead and update the screen with what we've drawn.
#     pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
