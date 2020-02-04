import pygame
from shape import shape, screen_size,scaley,scalex,screen
import math
from astarv2 import intersect, a_star, heuristic
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
GREEN = (0,255,0)


pygame.display.set_caption(("A* Shortest Pathfinder"))
icon = pygame.image.load("maze.png")
pygame.display.set_icon(icon)

pygame.init()

shapes = [
shape((29, 12), (31, 15), (31, 18), (29, 19), (25, 18), (25, 15)),
shape((5, 15), (5, 19), (17, 19), (17, 15)),
shape((7, 3), (10, 8), (8, 13), (4, 12), (3, 8)),
shape((23, 3), (23, 11), (28, 11), (28, 3)),
shape((31, 3), (34, 5), (33, 13), (29, 5)),
shape((18, 3), (19, 5), (16, 8), (16, 4)),
shape((11, 12), (13, 6), (15, 12)),
shape((18, 13), (20, 18), (23, 16))
]

vertices = [ ]
edges = []
shape1 = shapes[0]
shape2 = shapes[1]

for shape in shapes:
    shape.draw()
    for vertex in shape.vertices:
        vertices.append(vertex)
    for edge in shape.edges:
        edges.append(edge)


running = True

start = pygame.draw.circle(screen, (0, 255, 0), (3 * scalex, 18 * scaley), screen_size[0] // 100)
end = pygame.draw.circle(screen, (255, 0, 0), (35 * scalex, 3 * scaley), screen_size[0] // 100)
vertices.append((35 * scalex, 3 * scaley))
print("hi")
path = a_star((3 * scalex , 18 * scaley), (35 * scalex , 3 * scaley), heuristic, vertices, edges, shapes)
pygame.draw.lines(screen, GREEN, False, path, 3)
pygame.display.update()
time.sleep(3)
screen.fill((0,0,0))
start = pygame.draw.circle(screen, (0, 255, 0), (3 * scalex, 18 * scaley), screen_size[0] // 100)
end = pygame.draw.circle(screen, (255, 0, 0), (35 * scalex, 3 * scaley), screen_size[0] // 100)
for shape in shapes:
    shape.draw()
pygame.draw.lines(screen, GREEN, False, path, 3)
pygame.display.update()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # screen.blit(path)
        pygame.display.update()

