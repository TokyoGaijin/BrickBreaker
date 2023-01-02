import pygame
import colorswatch as cs

pygame.joystick.init()



class Player(object):
    def __init__(self, surface, color = cs.tangelo["pygame"]):
        self.surface = surface
        self.color = color
        self.boost = 5
        self.hasSpeedBoost = False
        self.speed = 10
        self.posX = 60
        self.posY = 520
        self.width = 100
        self.height = 20
        self.playerRect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        self.inMotion = False
        self.lives = 3


    def moveRect(self, direction):
        self.inMotion = True
        if direction == "left":
            self.playerRect.x -= self.speed
        if direction == "right":
            self.playerRect.x += self.speed


    def updateControls(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    self.speed = 10

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.speed = 20
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.moveRect("left")
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.moveRect("right")
        else:
            self.inMotion = False

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.playerRect)
