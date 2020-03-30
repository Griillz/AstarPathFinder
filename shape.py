import pygame

#displays GUI
screen = pygame.display.set_mode((700, 400))
WHITE = (255, 255, 255)

#Gets x and y values for screen size to scaley the environment to any size
screen_size = pygame.display.get_surface().get_size()
scalex = screen_size[0] // 35
scaley = screen_size[1] // 20

#Shape class that stores all of the vertices and edge for each individual shape
class shape:
    def __init__(self, *args):
        self.vertices = []
        self.vertices += [(x * scalex, y * scaley) for x, y in args]
        self.edges = list(zip(self.vertices[:-1], self.vertices[1:])) + [(self.vertices[-1], self.vertices[0])]

    #Draws the shape to the screen
    def draw(self):
        for i in range(len(self.edges)):
            pygame.draw.line(screen, WHITE, self.edges[i][0], self.edges[i][1], 3)