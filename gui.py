import pygame
from shape import shape
import math
from temporary import scalex, scaley, screen, screen_size, WHITE
from astarv2 import \
intersect, a_star, heuristic

print(scalex)
print(scaley)
pygame.init()
GREEN = (0,255,0)
shapes = [
shape((29, 12), (31, 15), (31, 18), (29, 19), (25, 18), (25, 15)),
shape((5, 15), (5, 19), (17, 19), (17, 15)),
shape((7, 3), (10, 8), (8, 13), (4, 12), (3, 8)),
shape((23, 3), (23, 11), (28, 11), (28, 3)),
shape((31, 3), (34, 5), (33, 13), (29, 5)),
shape((20, 3), (22, 5), (16, 8), (16, 4)),
shape((11, 13), (13, 7), (15, 13)),
shape((18, 11), (20, 16), (23, 14))
]
vertices = []
edges = []
shape1 = shapes[0]
shape2 = shapes[1]


#print(dointersect(shape1.vertices[1], shape1.vertices[4], shape2.vertices[2], shape1.vertices[2]))
for shape in shapes:
    shape.draw()
    for vertex in shape.vertices:
        vertices.append(vertex)
    for edge in shape.edges:
        edges.append(edge)

#pygame.draw.line(screen, GREEN, (110, 570), (110, 450), 3)
#pygame.draw.line(screen, GREEN, (110, 570), (374, 570), 3)
#pygame.draw.line(screen, GREEN, (110, 570), (374, 450), 3)
#pygame.draw.line(screen, GREEN, (110, 570), (88, 360), 3)
#pygame.draw.line(screen, GREEN, (110, 570), (66, 240), 3)
running = True

start = pygame.draw.circle(screen, (0, 255, 0), (3 * scalex, 18 * scaley), screen_size[0] // 100)
end = pygame.draw.circle(screen, (255, 0, 0), (35 * scalex, 3 * scaley), screen_size[0] // 100)
vertices.append((35 * scalex, 3 * scaley))
print("hi")
path = a_star((3 * scalex , 18 * scaley), (35 * scalex , 3 * scaley), heuristic, vertices, edges, shapes)
pygame.draw.lines(screen, GREEN, False, path, 3)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # screen.blit(path)
        pygame.display.update()
#if path == False:

