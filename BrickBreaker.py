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
import titlescreen
from enum import Enum
import time

class GameState(Enum):
    TITLE = 0
    IN_PLAY = 1
    GAME_OVER = 2
    BOARD_CLEAR = 3


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
    global BrickList, inPlay, bg, currentLevel, current_score

    game_state = GameState.TITLE
    dev_mode = False
 




    def drawlevel(isBlank = False):

        if isBlank:
            for backbrick in bg:
                backbrick.draw()
            GAMEBOARD.draw()

        else:            
            for backbrick in bg:
                backbrick.draw()
            for brick in BrickList:
                brick.draw()      
        
            PLAYER.draw()
            PLAYER.updateControls()
            BALL.draw()
            GAMEBOARD.draw()

            pen.write_string(f"SCORE: {current_score}")
            pen.write_string(f"REMAIN: {PLAYER.lives}", posX = 620)
            pen.write_string("BreakAway", posX = 350)

    

    def update():
        global currentLevel, lives, current_score

     

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
            if BALL.ballRect.left < PLAYER.playerRect.left + 50:
                BALL.currentDirection = "up-left"
            elif BALL.ballRect.left > PLAYER.playerRect.right - 50:
                BALL.currentDirection = "up-right"
            else:
                BALL.currentDirection = "up"
                BALL.speed = 3


        # Collision ball vs. player and player is in motion
        if BALL.ballRect.colliderect(PLAYER.playerRect) and PLAYER.inMotion:
            thread = threading.Thread(target=play_beep(freq = 1000))
            thread.start()
            if BALL.ballRect.left < PLAYER.playerRect.left + PLAYER.playerRect.width / 2:
                BALL.currentDirection = "up-left"
            elif BALL.ballRect.left > PLAYER.playerRect.right - PLAYER.playerRect.width / 2:
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
            


        if BALL.ballRect.colliderect(GAMEBOARD.sideRect[0]):
            thread = threading.Thread(target=play_beep(freq = 700))
            thread.start()
            if BALL.currentDirection == "up-left":
                BALL.currentDirection = "up-right"
            elif BALL.currentDirection == "down-left":
                BALL.currentDirection = "down-right"

        if BALL.ballRect.colliderect(GAMEBOARD.sideRect[1]):
            thread = threading.Thread(target=play_beep(freq = 700))
            thread.start()
            if BALL.currentDirection == "up-right":
                BALL.currentDirection = "up-left"
            elif BALL.currentDirection == "down-right":
                BALL.currentDirection = "down-left"
              


        if BALL.ballRect.y >= sizeY:
            BALL.resetBall()
            if not dev_mode:
                PLAYER.lives -= 1
           


    # The game loop
    while inPlay:

        # Exits the program nomatter what
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            inPlay = False

        # To enter Dev-Mode: LeftSHIFT+LeftCTRL+D
        if keys[pygame.K_LSHIFT] and keys[pygame.K_LCTRL] and keys[pygame.K_d]:
            if dev_mode:
                dev_mode = False
            else:
                dev_mode = True


        if game_state == GameState.IN_PLAY:
            clock.tick(FPS)
        
            if PLAYER.lives < 0:
                game_state = GameState.GAME_OVER

            # Advance to next level
            if len(BrickList) <= 0:
                current_score += 500
                currentLevel += 1
                if currentLevel >= len(GAMEBOARD.room):
                    currentLevel = 0

                game_state = GameState.BOARD_CLEAR

                


            update()
            drawlevel()
            pygame.display.update()
            SURFACE.fill(cs.black["pygame"])
        


        if game_state == GameState.BOARD_CLEAR:

            pen.write_string("LEVEL CLEAR!", posX = 300, posY = 300, size = 20, color = cs.white["pygame"])
            pen.write_string("BONUS POINTS AWARDED: 500!", posX = 300, posY = 330, size = 20, color = cs.white["pygame"])
            pen.write_string(f"SCORE: {current_score}", posX = 300, posY = 350, size = 20, color = cs.white["pygame"])
            pen.write_string(f"LIVES REMAINING: {PLAYER.lives}", posX = 300, posY = 400, size = 20, color = cs.white["pygame"])

            pen.write_string("Press ENTER to advance", posX =250, posY = 620, size = 20, color = cs.white["pygame"])

            if keys[pygame.K_RETURN]:
                BALL.resetBall()
                get_room(currentLevel)
                game_state = GameState.IN_PLAY


            

            pygame.display.update()
            SURFACE.fill(cs.black["pygame"])



        if game_state == GameState.GAME_OVER:
            drawlevel(isBlank = True)

            pen.write_string("GAME OVER", posX = (sizeX / 2) - 50, posY = sizeY / 2, size = 500)
            pen.write_string(f"YOUR SCORE: {current_score}", posX = 300, posY = 550)
            pen.write_string("Press ENTER to start again", posX = 250, posY = 620, size = 20, color = cs.white["pygame"])

            pygame.display.update()
            SURFACE.fill(cs.black["pygame"])

            if keys[pygame.K_RETURN]:
                BALL.resetBall()
                BrickList = []
                PLAYER.lives = 3
                current_score = 0
                currentLevel = 1
                game_state = GameState.TITLE




        if game_state == GameState.TITLE:
            drawlevel(isBlank = True)
            titlescreen.draw_title(SURFACE)

            pen.write_string("A 'Breakout' Clone game by Mike Yamazaki", posX = 140, posY = 500, size = 20)
            pen.write_string("Press SPACE BAR to begin", posX = 250, posY = 620, size = 20, color = cs.white["pygame"])

            if keys[pygame.K_SPACE]:
                BrickList = []
                get_room(1)
                BALL.resetBall()
                game_state = GameState.IN_PLAY

            pygame.display.update()
            SURFACE.fill(cs.black["pygame"])
        

            
    


if __name__ == "__main__":
    main_game()
