import pygame
from shape import shape
import math
from temporary import scalex, scaley, screen, screen_size

from astar import astar, heuristic

print(scalex)
print(scaley)
pygame.init()

shape1 = shape((29, 12), (31, 15), (31, 18), (29, 19), (25, 18), (25, 15))
shape1.draw()
shape2 = shape((5, 15), (5, 19), (17, 19), (17, 15))
shape2.draw()
shape3 = shape((7, 3), (10, 8), (8, 13), (4, 12), (3, 8))
shape3.draw()
shape4 = shape((23, 3), (23, 11), (28, 11), (28, 3))
shape4.draw()
shape5 = shape((31, 3), (34, 5), (33, 13), (29, 5))
shape5.draw()
shape6 = shape((20, 3), (22, 5), (16, 8), (16, 4))
shape6.draw()
shape7 = shape((11, 13), (13, 7), (15, 13))
shape7.draw()
shape8 = shape((18, 11), (20, 16), (23, 14))
shape8.draw()

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
