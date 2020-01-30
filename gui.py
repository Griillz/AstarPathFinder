import pygame
import math
WHITE = (255, 255, 255)
from shape import shape
from astar import astar, heuristic

screen = pygame.display.set_mode((800, 600))
BLACK = (0, 0, 0)

screen_size = pygame.display.get_surface().get_size()
pygame.display.set_caption(("A* Shortest Pathfinder"))
icon = pygame.image.load("maze.png")
pygame.display.set_icon(icon)

scalex = screen_size[0] // 35
scaley = screen_size[1] // 20

print(scalex)
print(scaley)
pygame.init()

shapetest = shape()
shapetest.draw((29 * scalex, 12 * scaley), (31 * scalex, 15 * scaley),(31 * scalex, 18 * scaley),(29 * scalex, 19 * scaley))

running = True
"""
vertices = [(29 * scalex, 12 * scaley), (31 * scalex, 15 * scaley),(31 * scalex, 18 * scaley),(29 * scalex, 19 * scaley),
            (25 * scalex, 18 * scaley),(25 * scalex, 15 * scaley),(5 * scalex, 15 * scaley),(5 * scalex, 19 * scaley),
            (17 * scalex, 19 * scaley),(17 * scalex, 15 * scaley),(7 * scalex, 3 * scaley),(10 * scalex, 8 * scaley),
            (8 * scalex, 13 * scaley),(4 * scalex, 12 * scaley),(3 * scalex, 8 * scaley),(23 * scalex, 3 * scaley),
            (23 * scalex, 11 * scaley),(28 * scalex, 11 * scaley),(28 * scalex, 3 * scaley),(31 * scalex, 3 * scaley),
            (34 * scalex, 5 * scaley),(33 * scalex, 13 * scaley),(29 * scalex, 5 * scaley),(20 * scalex, 3 * scaley),
            (22 * scalex, 5 * scaley),(16 * scalex, 8 * scaley),(16 * scalex, 4 * scaley),(11 * scalex, 13 * scaley),
            (13 * scalex, 7 * scaley),(15 * scalex, 13 * scaley),(18 * scalex, 11 * scaley),(20 * scalex, 16 * scaley),
            (23 * scalex, 14 * scaley)]


edges = [(vertices[0],vertices[1]),(vertices[1],vertices[2]),(vertices[3],vertices[4]),(vertices[4],vertices[5]),
         (vertices[5],vertices[0]),(vertices[6],vertices[7]),(vertices[7],vertices[8]),(vertices[8],vertices[9]),
         (vertices[9],vertices[6]),(vertices[10],vertices[11]),(vertices[11],vertices[12]),(vertices[12],vertices[13]),
         (vertices[13],vertices[14]),(vertices[14],vertices[10]),(vertices[15],vertices[16]),(vertices[16],vertices[17]),
         (vertices[17],vertices[18]),(vertices[18],vertices[15]),(vertices[19],vertices[20]),(vertices[20],vertices[21]),
         (vertices[21],vertices[22]),(vertices[22],vertices[19]),(vertices[23],vertices[24]),(vertices[24],vertices[25]),
         (vertices[25],vertices[26]),(vertices[26],vertices[23]),(vertices[27],vertices[28]),(vertices[28],vertices[29]),
         (vertices[29],vertices[27]),(vertices[30],vertices[31]),(vertices[31],vertices[32]),(vertices[32],vertices[30]),]

one = pygame.draw.polygon(screen, WHITE,
                          (vertices[0],vertices[1],vertices[2],vertices[3],vertices[4],vertices[5]), 3)
two = pygame.draw.polygon(screen, WHITE,
                          (vertices[6],vertices[7],vertices[8],vertices[9]), 3)
three = pygame.draw.polygon(screen, WHITE,
                            (vertices[10],vertices[11],vertices[12],vertices[13],vertices[14]), 3)
four = pygame.draw.polygon(screen, WHITE,
                           (vertices[15],vertices[16],vertices[17],vertices[18]), 3)
five = pygame.draw.polygon(screen, WHITE,
                           (vertices[19],vertices[20],vertices[21],vertices[22]), 3)
six = pygame.draw.polygon(screen, WHITE,
                          (vertices[23],vertices[24],vertices[25],vertices[26]), 3)
seven = pygame.draw.polygon(screen, WHITE,
                            (vertices[27],vertices[28],vertices[29])
                            , 3)
eight = pygame.draw.polygon(screen, WHITE,
                            (vertices[30],vertices[31],vertices[32])
                            , 3)
start = pygame.draw.circle(screen, (0, 255, 0), (3 * scalex, 18 * scaley), screen_size[0] // 100)
end = pygame.draw.circle(screen, (255, 0, 0), (35 * scalex, 3 * scaley), screen_size[0] // 100)

path = astar((3 * scalex, 18 * scaley), (35 * scalex, 3 * scaley), heuristic, edges, vertices)
"""
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.blit(path)
    pygame.display.update()
