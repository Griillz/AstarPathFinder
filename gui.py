import pygame
from shape import shape, screen_size, scaley, scalex, screen
from astarv2 import a_star
import time
import random

# Pygame stuff
pygame.init()
pygame.display.set_caption(("A* Shortest Pathfinder"))
icon = pygame.image.load("maze.png")
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 20)
running = True

# Constants for certain RGB colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fixed starting and ending locations
start_fixed = ((2 * scalex, 18 * scaley))
end_fixed = ((34 * scalex, 3 * scaley))

# Random starting and ending locations
startrand = random.randint(1, 19)
endrand = random.randint(1, 19)
start = (2 * scalex, startrand * scaley)
end = (34 * scalex, endrand * scaley)

# List of different shape objects
shapes = [
    shape((29, 12), (31, 15), (31, 18), (29, 19), (25, 18), (25, 15)),
    shape((5, 15), (5, 19), (17, 19), (17, 15)),
    shape((7, 3), (10, 8), (8, 13), (4, 12), (3, 8)),
    shape((23, 3), (23, 11), (28, 11), (28, 3)),
    shape((31, 3), (33, 5), (32, 13), (29, 5)),
    shape((18, 3), (19, 5), (16, 8), (16, 4)),
    shape((11, 12), (13, 6), (15, 12)),
    shape((18, 13), (20, 18), (23, 16))
]

# Cost restraint for assignment 2
restraint = int(input("Input your desired restraint value."))

# Shows restraint on gui screen, and displays different results based on if a path is found or not
score = font.render("Restraint: " + str(restraint), True, (255,255,255))
nopath = font.render("Path Not Found with restraint of: " + str(restraint), True, (255,0,0))
pathfound = font.render("Path found with restraint of: " + str(restraint), True, (0,255,0))
screen.blit(score,(10,10))

# List of all vertices and edges for all shapes
vertices, edges = [], []
shape1 = shapes[0]
shape2 = shapes[1]

# Loop through shapes and draw to screen
for shape in shapes:
    shape.draw()
    for vertex in shape.vertices:
        vertices.append(vertex)
    for edge in shape.edges:
        edges.append(edge)

# Draws start and end circles
pygame.draw.circle(screen, (0, 255, 0), start, screen_size[0] // 100)
pygame.draw.circle(screen, (255, 0, 0), end, screen_size[0] // 100)

# Adds goal location to vertices list so it can be explored
vertices.append(end)

# Runs the astar algorithm and stores the best path in a variable
path = a_star(start, end, vertices, edges, shapes, restraint)

# Draws the best path to the screen if it is found
if path:
    # Leaves best path on screen along with all other paths the algorithm tried to take for three seconds,
    # Then redraws the shapes along with only the best paths
    pygame.draw.lines(screen, GREEN, False, path, 3)
    time.sleep(3)
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 0), start, screen_size[0] // 100)
    pygame.draw.circle(screen, (255, 0, 0), end, screen_size[0] // 100)
    for shape in shapes:
        shape.draw()
    pygame.draw.lines(screen, GREEN, False, path, 3)
    screen.blit(pathfound, (10, 10))
    pygame.display.update()
else:
    # Tells the user that no path was found under the restraint
    screen.fill((0,0,0))
    screen.blit(nopath, (10, 10))
    pygame.draw.circle(screen, (0, 255, 0), start, screen_size[0] // 100)
    pygame.draw.circle(screen, (255, 0, 0), end, screen_size[0] // 100)
    for shape in shapes:
        shape.draw()
    pygame.display.update()

# Infinite pygame loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # screen.blit(path)
        pygame.display.update()
