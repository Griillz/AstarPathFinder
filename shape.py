import math
import pygame
from gui import scalex, scaley, screen, WHITE


class shape:

    def __init__(self):
        self.vertices = []
        self.edges = []
        self.count = 0

    def draw(self, *args):
        self.vertices.append([x for x in args])
        self.edges = []
        for i in range(self.vertices[self.count]):
            self.edges[self.count].append((self.vertices[i], self.vertices[i + 1]))

        pygame.draw.polygon(screen, WHITE,
                            tuple(self.vertices[self.count][0] * scalex, self.vertices[self.count][1] * scaley))
        self.count += 1
