import pygame
import colorswatch as cs
import gameBoard
from gameBoard import BGBricks
import player
import ball
from brick import Brick
import writer
import winsound
import threading


def play_beep(freq = 1000):
    winsound.Beep(freq, 20)

pygame.init()


# This is the master game file where everything will be handled at runtime

sizeX = 800
sizeY = 700
screenSize = (sizeX, sizeY)

SURFACE = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Brick Breaker by Tokyo Trekker")
FPS = 60
clock = pygame.time.Clock()
inPlay = True


GAMEBOARD = gameBoard.GameBoard(SURFACE)
PLAYER = player.Player(SURFACE)
BALL = ball.Ball(SURFACE, 400, 350, color = cs.red["pygame"])

pen = writer.Writer(SURFACE, 10, 650, color = cs.green["pygame"], size = 14)
currentLevel = 1
current_score = 0
levelMap = ""
BrickList = []
bg = []


for x in range(0, 800, 100):
    for y in range(0, 600, 40):
        bg.append(BGBricks(SURFACE, x, y))


def get_room(room_number):
    global BrickList, levelMap, currentLevel
    posX, posY = 0, 0
    width, height = 100, 40

    levelMap = GAMEBOARD.room[room_number]
   
    for row in levelMap:
        for col in row:
            if col == "1":
                BrickList.append(Brick(SURFACE, posX, posY, cs.red["pygame"]))
            if col == "2":
                BrickList.append(Brick(SURFACE, posX, posY, cs.tangelo["pygame"]))
            if col == "3":
                BrickList.append(Brick(SURFACE, posX, posY, cs.green["pygame"]))
            if col == "4":
                BrickList.append(Brick(SURFACE, posX, posY, cs.purple_rain["pygame"]))
            if col == "5":
                BrickList.append(Brick(SURFACE, posX, posY, cs.shit["pygame"]))
            if col == "6":
                BrickList.append(Brick(SURFACE, posX, posY, cs.light_gray["pygame"]))

            posX += width

        posY += height
        posX = 0

    return BrickList



def main_game():
    global BrickList, inPlay, bg, currentLevel
   
    get_room(currentLevel)
    BALL.resetBall()





    def drawlevel():
               
        for backbrick in bg:
            backbrick.draw()
        for brick in BrickList:
            brick.draw()      
        
        PLAYER.draw()
        PLAYER.updateControls()
        BALL.draw()
        GAMEBOARD.draw()

        pen.write_string(f"SCORE: {current_score}")
        pen.write_string(f"{PLAYER.lives} LIVES", posX = 690)
        pen.write_string(f"LEVEL: {currentLevel}", posX = 350)


    def update():
        global currentLevel, lives, current_score

     

        if len(BrickList) <= 0:
            currentLevel += 1
            BALL.resetBall()

        BALL.move(BALL.currentDirection)

        # Checks ball speed
        if BALL.speed >= BALL.maxSpeed:
            BALL.speed = BALL.maxSpeed


        # Collision player vs. borders
        if PLAYER.playerRect.left <= GAMEBOARD.sideRect[0].right:
            PLAYER.playerRect.x = GAMEBOARD.sideRect[0].right
        if PLAYER.playerRect.right > GAMEBOARD.sideRect[1].left:
            PLAYER.playerRect.right = GAMEBOARD.sideRect[1].left


        # Collision ball vs. player
        if BALL.ballRect.colliderect(PLAYER.playerRect) and not PLAYER.inMotion:
            thread = threading.Thread(target=play_beep(freq = 900))
            thread.start()            
            if BALL.ballRect.bottom >= PLAYER.playerRect.top:
                BALL.currentDirection = "up"
            if BALL.ballRect.left < PLAYER.playerRect.left + 40:
                BALL.currentDirection = "up-left"
            elif BALL.ballRect.left > PLAYER.playerRect.right - 40:
                BALL.currentDirection = "up-right"
            else:
                BALL.currentDirection = "up"
                BALL.speed = 3


        # Collision ball vs. player and player is in motion
        if BALL.ballRect.colliderect(PLAYER.playerRect) and PLAYER.inMotion:
            thread = threading.Thread(target=play_beep(freq = 1000))
            thread.start()
            if BALL.ballRect.left < PLAYER.playerRect.left + 40:
                BALL.currentDirection = "up-left"
            elif BALL.ballRect.left > PLAYER.playerRect.right - 40:
                BALL.currentDirection = "up-right"

          
        
        # Collision ball vs. brick
        for brick in BrickList:
            if BALL.ballRect.colliderect(brick.brickRect):
                thread = threading.Thread(target=play_beep(freq = 2000))
                thread.start()
                brick.hitpoints -= 1
                brick.updateBrick()
                if brick.hitpoints <= 0:
                    current_score += brick.points
                    BrickList.remove(brick)
                if BALL.currentDirection == "up":
                    BALL.currentDirection = "down"
                elif BALL.currentDirection == "up-right":
                    BALL.currentDirection = "down-right"
                elif BALL.currentDirection == "up-left":
                    BALL.currentDirection = "down-left"
                elif BALL.currentDirection == "down-right":
                    BALL.currentDirection = "up-right"
                elif BALL.currentDirection == "down-left":
                    BALL.currentDirection = "up-left"
                BALL.speed += .2
                
        # Collision ball vs. top
        if BALL.ballRect.colliderect(GAMEBOARD.topRect):
            thread = threading.Thread(target=play_beep(freq = 700))
            thread.start()
            if BALL.currentDirection == "up":
                BALL.currentDirection = "down"
            elif BALL.currentDirection == "up-right":
                BALL.currentDirection = "down-right"
            elif BALL.currentDirection == "up-left":
                BALL.currentDirection = "down-left"
            BALL.speed += .5
            

        # Collision ball vs. sides
        for sides in GAMEBOARD.sideRect:
            if BALL.ballRect.colliderect(sides):
                thread = threading.Thread(target=play_beep(freq = 700))
                thread.start()
                if BALL.currentDirection == "up-right":
                    BALL.currentDirection = "up-left"
                elif BALL.currentDirection == "down-right":
                    BALL.currentDirection = "down-left"
                elif BALL.currentDirection == "up-left":
                    BALL.currentDirection = "up-right"
                elif BALL.currentDirection == "down-left":
                    BALL.currentDirection = "down-right"

        #if BALL.ballRect.y >= sizeY:
        #    BALL.resetBall()
        #    PLAYER.lives -= 1
           


    # The game loop
    while inPlay:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            inPlay = False

        if PLAYER.lives < 0:
            inPlay = False

        update()
        drawlevel()
        pygame.display.update()
        SURFACE.fill(cs.black["pygame"])

    


if __name__ == "__main__":
    main_game()