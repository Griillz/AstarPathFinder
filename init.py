import pygame
WINDOW_X = 700
WINDOW_Y = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128,0,128)
START = (1, 3)
END = (19, 17)
w = 1
gridsize = int(input("Enter the size of the grid, 50, 100, 200, or 300"))
gridblocked = float(input("Enter the obstacle percentage, 0 , .1, .2, or .3"))
HEIGHT = WINDOW_Y / gridsize - 1
WIDTH = WINDOW_X / gridsize - 1
MARGIN = 1
WINDOW_SIZE = [WINDOW_X, WINDOW_Y]
screen = pygame.display.set_mode(WINDOW_SIZE, flags=pygame.HWACCEL)
