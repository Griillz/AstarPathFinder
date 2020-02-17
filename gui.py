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
start1 = ((2 * scalex, 18 * scaley))
end1 = ((34 * scalex, 3 * scaley))

start2 = ((3 * scalex, 15 * scaley))
end2 = ((33 * scalex, 5 * scaley))

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

shapes2 = [
    shape((5, 5), (10, 4), (15, 5), (13, 8), (10, 10), (10, 7), (5, 7)),
    shape((5, 9), (5, 13), (7, 13)),
    shape((5, 17), (15, 17), (15, 19), (5, 19)),
    shape((10, 15), (15, 10), (17, 5), (20, 10), (15, 15)),
    shape((20, 5), (21, 1), (26, 5)),
    shape((20, 19), (23, 10), (26, 7), (26, 18)),
    shape((28, 12), (30, 3), (31, 7), (33, 7), (33, 11), (31, 15), (29, 15))
]

# Cost restraint for assignment 2
initial = font.render(f'Press 1 or 2 to begin program with specified environment!', True, (255, 255, 255))
disprestraint = font.render(f'Enter restraint into the console!', True, (255, 255, 255))
screen.blit(initial, (10,10))
pygame.display.update()
#restraint = int(input("Input your desired restraint value."))

# Shows restraint on gui screen, and displays different results based on if a path is found or not


# List of all vertices and edges for all shapes
vertices, edges = [], []
# shape1 = shapes[0]
# shape2 = shapes[1]

def pathswitch(environment, newstart, newend, newshapes):
    screen.fill((0,0,0))
    screen.blit(disprestraint, (10,10))
    pygame.display.update()
    newrestraint = int(input(f"Enter a restraint value for environment {environment}: "))
    score = font.render("Restraint: " + str(newrestraint), True, (255, 255, 255))
    nopath = font.render("Path Not Found with restraint of: " + str(newrestraint), True, (255, 0, 0))
    pathfound = font.render("Path found with restraint of: " + str(newrestraint), True, (0, 255, 0))
    screen.fill((0,0,0))
    screen.blit(score, (10, 10))
    for shape in newshapes:
        shape.draw()
    pygame.draw.circle(screen, (0, 255, 0), newstart, screen_size[0] // 100)
    pygame.draw.circle(screen, (255, 0, 0), newend, screen_size[0] // 100)
    newpath = a_star(newstart, newend, vertices, edges, newshapes, newrestraint)

    if newpath:
        # Leaves best path on screen along with all other paths the algorithm tried to take for three seconds,
        # Then redraws the shapes along with only the best paths
        pygame.draw.lines(screen, GREEN, False, newpath, 3)
        time.sleep(3)
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (0, 255, 0), newstart, screen_size[0] // 100)
        pygame.draw.circle(screen, (255, 0, 0), newend, screen_size[0] // 100)
        for shape in newshapes:
            shape.draw()
        pygame.draw.lines(screen, GREEN, False, newpath, 3)
        screen.blit(pathfound, (10, 10))
        pygame.display.update()
        time.sleep(5)
        screen.fill((0,0,0))
        screen.blit(initial, (10,10))
        pygame.display.update()
    else:
        # Tells the user that no path was found under the restraint
        screen.fill((0, 0, 0))
        screen.blit(nopath, (10, 10))
        pygame.draw.circle(screen, (0, 255, 0), newstart, screen_size[0] // 100)
        pygame.draw.circle(screen, (255, 0, 0), newend, screen_size[0] // 100)
        for shape in newshapes:
            shape.draw()
        pygame.display.update()
        time.sleep(5)
        screen.fill((0, 0, 0))
        screen.blit(initial, (10, 10))
        pygame.display.update()



# Infinite pygame loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                vertices, edges = [], []
                for shape in shapes:
                    shape.draw()
                    for vertex in shape.vertices:
                        vertices.append(vertex)
                    for edge in shape.edges:
                        edges.append(edge)
                vertices.append(end1)
                pathswitch(1, start1, end1, shapes)
            if event.key == pygame.K_2:
                vertices, edges = [], []
                for shape in shapes2:
                    shape.draw()
                    for vertex in shape.vertices:
                        vertices.append(vertex)
                    for edge in shape.edges:
                        edges.append(edge)
                vertices.append(end2)
                pathswitch(2, start2, end2, shapes2)

        # screen.blit(path)
        pygame.display.update()
