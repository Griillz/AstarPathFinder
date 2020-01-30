import pygame

WHITE = (255, 255, 255)
screen = pygame.display.set_mode((800, 600))
BLACK = (0, 0, 0)

screen_size = pygame.display.get_surface().get_size()
pygame.display.set_caption(("A* Shortest Pathfinder"))
icon = pygame.image.load("maze.png")
pygame.display.set_icon(icon)

scalex = screen_size[0] // 35
scaley = screen_size[1] // 20