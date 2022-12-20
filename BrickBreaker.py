import pygame
import colorswatch as cs
import gameBoard

pygame.init()

# This is the master game file where everything will be handled at runtime

sizeX = 800
sizeY = 600
screenSize = (sizeX, sizeY)

SURFACE = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Brick Breaker by Tokyo Trekker")
FPS = 60
clock = pygame.time.Clock()
inPlay = True

GAMEBOARD = gameBoard.GameBoard(SURFACE)

while inPlay:
    clock.tick(FPS)

    GAMEBOARD.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False


    pygame.display.update()
    SURFACE.fill(cs.black["pygame"])