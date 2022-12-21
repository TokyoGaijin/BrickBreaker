import pygame
import colorswatch as cs
import gameBoard
import player
import ball
import brick

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
BrickList = []


def get_room(room_number):
    # Gets the level ready to go
    global BrickList
    posX, posY = 0, 0
    width, height = 100, 40

    drawlevel = GAMEBOARD.room[room_number]
    
    for row in drawlevel:
        for col in row:
            if col == 1:
                BrickList.append(brick.Brick(SURFACE, posX, posY, cs.red["pygame"]))
            if col == 2:
                BrickList.append(brick.Brick(SURFACE, posX, posY, cs.tangelo["pygame"]))
            if col == 3:
                BrickList.append(brick.Brick(SURFACE, posX, posY, cs.green["pygame"]))
            if col == 4:
                BrickList.append(brick.Brick(SURFACE, posX, posY, cs.purple_rain["pygame"]))
            if col == 5:
                BrickList.append(brick.Brick(SURFACE, posX, posY, cs.shit["pygame"]))
            if col == 6:
                BrickList.append(brick.Brick(SURFACE, posX, posY, cs.light_gray["pygame"]))

            posX += width

            posY += height
            posX = 0




get_room(2)

while inPlay:
    clock.tick(FPS)
    
    def update():
        global currentLevel
        cooldownTimer = 3300
        GAMEBOARD.draw()
        #get_room(1)
        print(len(BrickList))
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
          
        
        # Collision ball vs. brick
        #if BALL.ballRect.colliderect(BRICK.brickRect):
        #    BRICK.hitpoints -= 1
        #    BRICK.updateBrick()
        #    if BALL.currentDirection == "up":
        #        BALL.currentDirection = "down"
        #    elif BALL.currentDirection == "up-left":
        #        BALL.currentDirection = "down-left"
        #    elif BALL.currentDirection == "up-right":
        #        BALL.currentDirection = "down-right"
        #    elif BALL.currentDirection == "down-left":
        #        BALL.currentDirection = "up-left"
        #    elif BALL.currentDirection == "down-right":
        #        BALL.currentDirection = "up-right"


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