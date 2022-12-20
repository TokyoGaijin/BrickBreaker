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
        if BALL.ballRect.bottom >= PLAYER.playerRect.top:
            if BALL.ballRect.left >= PLAYER.playerRect.x + 30 and BALL.ballRect.right <= PLAYER.playerRect.width - 30:
                BALL.currentDirection = "up"
                BALL.speed += 1
            if BALL.ballRect.left >= PLAYER.playerRect.x and BALL.ballRect.left <= PLAYER.playerRect.x + 30:
                BALL.currentDirection = ("up", "left")
                BALL.speed += 1
            if BALL.ballRect.left <= PLAYER.playerRect.width and BALL.ballRect.right >= PLAYER.playerRect.width - 30:
                BALL.currentDirection = ("up", "right")
                BALL.speed += 1



        # Collision ball vs. border
        if BALL.ballRect.top <= GAMEBOARD.topRect.bottom:
            BALL.currentDirection = "down"
            BALL.speed += 1
        

        


            

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False

    update()
    pygame.display.update()
    SURFACE.fill(cs.black["pygame"])