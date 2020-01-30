import pygame
from shape import shape
import math
from temporary import scalex, scaley, screen, screen_size

from astar import astar, heuristic



print(scalex)
print(scaley)
pygame.init()

shape1 = shape()
shape1.draw((29, 12), (31, 15),(31, 18),
               (29, 19), (25, 18),(25, 15))
shape2 = shape()
shape2.draw((5 , 15),(5 , 19),
            (17 , 19),(17 , 15))
shape3 = shape()
shape3.draw((7 , 3),(10 , 8),
            (8 , 13),(4 , 12),(3 , 8))
shape4 = shape()
shape4.draw((23 , 3),
            (23 , 11),(28 , 11),(28 , 3))
shape5 = shape()
shape5.draw((31 , 3),
            (34 , 5),(33 , 13),(29 , 5))
shape6 = shape()
shape6.draw((20 , 3),
            (22 , 5),(16 , 8),(16 , 4))
shape7 = shape()
shape7.draw((11 , 13),
            (13 , 7),(15 , 13))
shape8 = shape()
shape8.draw((18 , 11),(20 , 16),
            (23 , 14))

running = True

start = pygame.draw.circle(screen, (0, 255, 0), (3 * scalex, 18 * scaley), screen_size[0] // 100)
end = pygame.draw.circle(screen, (255, 0, 0), (35 * scalex, 3 * scaley), screen_size[0] // 100)

#path = astar((3 , 18), (35 , 3), heuristic, edges, vertices)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.blit(path)
    pygame.display.update()
