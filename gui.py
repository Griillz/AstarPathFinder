import pygame
from shape import shape
import math
from temporary import scalex, scaley, screen, screen_size
from astarv2 import dointersect

from astar import astar, heuristic

print(scalex)
print(scaley)
pygame.init()

shapes = [
shape((29, 12), (31, 15), (31, 18), (29, 19), (25, 18), (25, 15)),
shape((5, 15), (5, 19), (17, 19), (17, 15)),
    ]
'''
shape((7, 3), (10, 8), (8, 13), (4, 12), (3, 8)),
shape((23, 3), (23, 11), (28, 11), (28, 3)),
shape((31, 3), (34, 5), (33, 13), (29, 5)),
shape((20, 3), (22, 5), (16, 8), (16, 4)),
shape((11, 13), (13, 7), (15, 13)),
shape((18, 11), (20, 16), (23, 14))
'''

shape1 = shapes[0]
shape2 = shapes[1]

print(dointersect(shape1.vertices[3], shape1.vertices[4], shape2.vertices[2], shape1.vertices[2]))
for shape in shapes:
    shape.draw()



running = True

start = pygame.draw.circle(screen, (0, 255, 0), (3 * scalex, 18 * scaley), screen_size[0] // 100)
end = pygame.draw.circle(screen, (255, 0, 0), (35 * scalex, 3 * scaley), screen_size[0] // 100)

# path = astar((3 , 18), (35 , 3), heuristic, edges, vertices)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.blit(path)
    pygame.display.update()
