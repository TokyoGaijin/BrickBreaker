import pygame
import colorswatch as cs
import gameBoard
import player
import ball

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
PLAYER = player.Player(SURFACE)
BALL = ball.Ball(SURFACE, 400, 250, color = cs.red["pygame"])

while inPlay:
    clock.tick(FPS)
    
    def update():
        cooldownTimer = 3300
        GAMEBOARD.draw()
        PLAYER.draw()
        PLAYER.updateControls()
        BALL.draw()
        
        BALL.move(BALL.currentDirection)

        # Collision player vs. borders
        if PLAYER.playerRect.left <= GAMEBOARD.sideRect[0].right:
            PLAYER.playerRect.x = GAMEBOARD.sideRect[0].right
        if PLAYER.playerRect.right > GAMEBOARD.sideRect[1].left:
            PLAYER.playerRect.right = GAMEBOARD.sideRect[1].left

        # Collision ball vs. player
        if BALL.ballRect.colliderect(PLAYER.playerRect):
            if BALL.ballRect.left < PLAYER.playerRect.left + 30:
                BALL.currentDirection = "up-left"
            elif BALL.ballRect.left > PLAYER.playerRect.right - 30:
                BALL.currentDirection = "up-right"
            else:
                BALL.currentDirection = "up"
                BALL.speed += .5

          

        # Collision ball vs. top
        if BALL.ballRect.colliderect(GAMEBOARD.topRect):
            if BALL.currentDirection == "up":
                BALL.currentDirection = "down"
            elif BALL.currentDirection == "up-right":
                BALL.currentDirection = "down-right"
            elif BALL.currentDirection == "up-left":
                BALL.currentDirection = "down-left"
            BALL.speed += .5
            

        # Collision ball vs. sides
        for i in range(0, len(GAMEBOARD.sideRect)):
            if BALL.ballRect.colliderect(GAMEBOARD.sideRect[i]):
                if BALL.currentDirection == "up-right":
                    BALL.currentDirection = "up-left"
                elif BALL.currentDirection == "down-right":
                    BALL.currentDirection = "down-left"
                elif BALL.currentDirection == "up-left":
                    BALL.currentDirection = "up-right"
                elif BALL.currentDirection == "down-left":
                    BALL.currentDirection = "down-right"
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False

    update()
    pygame.display.update()
    SURFACE.fill(cs.black["pygame"])