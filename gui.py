import pygame
from shape import shape, screen_size, scaley, scalex, screen
from astarv2 import a_star, simplified_anytime
import time
import random

#Constants for certain RGB colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.display.set_caption(("A* Shortest Pathfinder"))
icon = pygame.image.load("maze.png")
pygame.display.set_icon(icon)

pygame.init()

#List of different shape objects
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

#Fixed starting and ending locations
start_fixed = ((2 * scalex, 18 * scaley))
end_fixed = ((34 * scalex, 3 * scaley))


startrand = random.randint(1,19)
endrand = random.randint(1,19)
start = (2 * scalex, startrand * scaley)
end = (34 * scalex, endrand * scaley)

#List of all vertices and edges for all shapes
vertices, edges = [], []
shape1 = shapes[0]
shape2 = shapes[1]

#Loop through shapes and draw to screen
for shape in shapes:
    shape.draw()
    for vertex in shape.vertices:
        vertices.append(vertex)
    for edge in shape.edges:
        edges.append(edge)

running = True

#Draws start and end circles
pygame.draw.circle(screen, (0, 255, 0), start_fixed, screen_size[0] // 100)
pygame.draw.circle(screen, (255, 0, 0), end_fixed, screen_size[0] // 100)

#Adds goal location to vertices list so it can be explored
vertices.append(end_fixed)

#Runs the astar algorithm and stores the best path in a variable
path = simplified_anytime(start_fixed, end_fixed, vertices, edges, shapes, 101, 10)

#Draws the best path to the screen
pygame.draw.lines(screen, GREEN, False, path, 3)
pygame.display.update()

#Leaves best path on screen along with all other paths the algorithm tried to take for three seconds,
#Then redraws the shapes along with only the best paths
time.sleep(3)
screen.fill((0, 0, 0))
pygame.draw.circle(screen, (0, 255, 0), start_fixed, screen_size[0] // 100)
pygame.draw.circle(screen, (255, 0, 0), end_fixed, screen_size[0] // 100)
for shape in shapes:
    shape.draw()
pygame.draw.lines(screen, GREEN, False, path, 3)
pygame.display.update()

#Infinite pygame loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # screen.blit(path)
        pygame.display.update()