import pygame
import colorswatch as cs

class Brick(object):
    def __init__(self, surface, posX, posY, color):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.color = color

        # 5 color categories in order to determine point value and hit points
        # TODO: make sure the colors change with each hit point

        if self.color == cs.red["pygame"]:
            self.points = 25
            self.hitpoints = 1
        elif self.color == cs.tangelo["pygame"]:
            self.points = 50
            self.hitpoints = 2
        elif self.color == cs.green["pygame"]:
            self.points = 75
            self.hitpoints = 3
        elif self.color == cs.purple_rain["pygame"]:
            self.points = 100
            self.hitpoints = 4
        elif self.color == cs.shit["pygame"]:
            self.points = 500
            self.hitpoints = 8
        elif self.color == cs.light_gray["pygame"]:
            self.points = 1000
            self.hitpoints = 10

        self.brickRect = pygame.Rect(self.posX, self.posY, 100, 40)
        self.brickColorRect = pygame.Rect(self.posX + 5, self.posY + 5, 95, 35)
        self.isVisible = True



    def updateBrick(self):
        if self.isVisible:
            if self.hitpoints == 1:
                self.color = cs.red["pygame"]
            elif self.hitpoints == 2:
                self.color = cs.tangelo["pygame"]
            elif self.hitpoints == 3:
                self.color = cs.green["pygame"]
            elif self.hitpoints == 4:
                self.color = cs.blue["pygame"]
            elif self.hitpoints > 4 and self.hitpoints < 10:
                self.color = cs.purple_rain["pygame"]
            elif self.hitpoints >= 10:
                self.color = cs.light_gray["pygame"]

            if self.hitpoints <= 0:
                self.isVisible = False
                # Remove brick from list manager


    def draw(self):
        if self.isVisible:
            pygame.draw.rect(self.surface, cs.black["pygame"], self.brickRect) # border that takes collisions
            pygame.draw.rect(self.surface, self.color, self.brickColorRect) # substance