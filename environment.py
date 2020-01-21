import pygame
import random

#6x6 grids, pad 1.5 between each
screen = pygame.display.set_mode((603,603))

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (135,206,235)
WIDTH = 12
HEIGHT = 12
MARGIN = 3
running = True
grid = []

for row in range(80):
    grid.append([])
    for column in range(80):
        grid[row].append(0)

def draw_grid(cols, rows):
    for row in range(rows):
        for column in range(cols):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,
                                             (MARGIN + HEIGHT) * row + MARGIN,
                                             WIDTH,
                                             HEIGHT])


pygame.init()
screen.fill(BLUE)
draw_grid(40, 40)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_SPACE:
            grid[random.randint(0,40)][random.randint(0,40)] = 1
            draw_grid(40,40)


    pygame.display.update()

