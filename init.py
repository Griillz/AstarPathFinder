import pygame
WINDOW_X = 700
WINDOW_Y = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128,0,128)
w = 51
gridsize = int(input("Enter the size of the grid, 50, 100, 200, or 300"))
END = (gridsize - 3, gridsize - 3)
START = (2, 2)
gridblocked = float(input("Enter the obstacle percentage, 0 , .1, .2, or .3"))
HEIGHT = WINDOW_Y / gridsize - 1
WIDTH = WINDOW_X / gridsize - 1
MARGIN = 1
WINDOW_SIZE = [WINDOW_X, WINDOW_Y]
screen = pygame.display.set_mode(WINDOW_SIZE)
