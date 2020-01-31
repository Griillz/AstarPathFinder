import math
import pygame
from temporary import screen, scalex, scaley, WHITE


class shape:
    def __init__(self, *args):
        self.vertices = []
        self.vertices += [(x * scalex, y * scaley) for x, y in args]
        self.edges = list(zip(self.vertices[:-1], self.vertices[1:])) + [(self.vertices[-1], self.vertices[0])]


    def draw(self):
        for i in range(len(self.edges)):
                pygame.draw.line(screen, WHITE, self.edges[i][0], self.edges[i][1], 3)