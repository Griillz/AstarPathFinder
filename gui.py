import pygame

screen = pygame.display.set_mode((800,600))
BLACK = (0,0,0)
WHITE = (255,255,255)
screen_size = pygame.display.get_surface().get_size()
pygame.display.set_caption(("A* Shortest Pathfinder"))
icon = pygame.image.load("maze.png")
pygame.display.set_icon(icon)

scalex = screen_size[0] // 35
scaley = screen_size[1] // 20


print(scalex)
print(scaley)
pygame.init()

running = True

def draw_env():
    pygame.draw.polygon(screen, WHITE,
                        ((29 * scalex, 12 * scaley), (31 * scalex, 15 * scaley), (31 * scalex, 18 * scaley)
                         , (29 * scalex, 19 * scaley), (25 * scalex, 18 * scaley), (25 * scalex, 15 * scaley)), 3)
    pygame.draw.polygon(screen, WHITE, ((5 * scalex, 15 * scaley), (5 * scalex, 19 * scaley), (17 * scalex, 19 * scaley)
                                        , (17 * scalex, 15 * scaley)), 3)
    pygame.draw.polygon(screen, WHITE, ((7 * scalex, 3 * scaley), (10 * scalex, 8 * scaley), (8 * scalex, 13 * scaley)
                                        , (4 * scalex, 12 * scaley), (3 * scalex, 8 * scaley)), 3)
    pygame.draw.polygon(screen, WHITE, ((23 * scalex, 3 * scaley), (23 * scalex, 11 * scaley), (28 * scalex, 11 * scaley)
                                        , (28 * scalex, 3 * scaley)), 3)
    pygame.draw.polygon(screen, WHITE,
                        ((31 * scalex, 3 * scaley), (34 * scalex, 5 * scaley), (33 * scalex, 13 * scaley)
                         , (29 * scalex, 5 * scaley)), 3)
    pygame.draw.polygon(screen, WHITE,
                        ((20 * scalex, 3 * scaley), (22 * scalex, 5 * scaley), (16 * scalex, 8 * scaley)
                         , (16 * scalex, 4 * scaley)), 3)
    pygame.draw.polygon(screen, WHITE,
                        ((11 * scalex, 13 * scaley), (13 * scalex, 7 * scaley), (15 * scalex, 13 * scaley))
                         , 3)
    pygame.draw.polygon(screen, WHITE,
                        ((18 * scalex, 11 * scaley), (20 * scalex, 16 * scaley), (23 * scalex, 14 * scaley))
                        , 3)

    #pygame.draw.polygon(screen, WHITE, ((2*scalex,2*scaley), (4*scalex, 4*scaley), (6*scalex, 6*scaley)), 5)
    pygame.draw.circle(screen, (0,255,0), (3 * scalex, 18 * scaley), 10)
    pygame.draw.circle(screen, (255, 0, 0), (35 * scalex, 3 * scaley), 10)


draw_env()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
