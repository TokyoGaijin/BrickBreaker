import pygame
import colorswatch as cs

class Ball(object):
    def __init__(self, surface, startX, startY, color = cs.cornflower_blue["pygame"]):
        self.surface = surface
        self.startX = startX
        self.startY = startY
        self.posX = startX
        self.posY = startY
        self.color = color
        self.speed = 2
        self.currentDirection = "down"
        self.ballRect = pygame.Rect(self.startX, self.startY, 15, 15)
        self.isInPlay = True
       


    def move(self, direction):
        if direction == "down":
            self.ballRect.y += self.speed
        if direction == "up":
            self.ballRect.y -= self.speed
        if direction == "up-left":
            self.ballRect.y -= self.speed
            self.ballRect.x -= self.speed
        if direction == "up-right":
            self.ballRect.y -= self.speed
            self.ballRect.x += self.speed
        if direction == "down-left":
            self.ballRect.y += self.speed
            self.ballRect.x -= self.speed
        if direction == "down-right":
            self.ballRect.y += self.speed
            self.ballRect.x += self.speed



    def resetBall(self):
        self.isInPlay = True
        self.speed = 2
        self.ballRect.x = self.startX
        self.ballRect.y = self.startY
        

    def draw(self):
        if self.isInPlay:
            pygame.draw.rect(self.surface, self.color, self.ballRect)

    

    