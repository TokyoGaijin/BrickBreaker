import pygame
import colorswatch as cs

class Ball(object):
    def __init__(self, surface, posX, posY, color = cs.cornflower_blue["pygame"]):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.color = color
        self.speed = 5
        self.direction =  ("left", None) # Value [0] = "left" or "right; Value [1] = "up" or "down"
        self.lastDir = self.direction # Only accepts a tuple to keep trrack of the balls previous trajectory
        self.ballRec = pygame.Rect(self.posX, self.posY, 5, 5)


    def move(self, dir):
        # moving ball in cardinal directions only        
        if dir == ("left", None):
            self.ballRec.x -= self.speed
        if dir == ("right", None):
            self.ballRec.x += self.speed
        if dir == (None, "up"):
            self.ballRec.y -= self.speed
        if dir == (None, "down"):
            self.ballRec.y += self.speed

        # moving ball in diagonal directions
        if dir == ("left", "up"):
            self.ballRec.x -= self.speed
            self.ballRec.y -= self.speed
        if dir == ("left", "down"):
            self.ballRec.x -= self.speed
            self.ballRec.y += self.speed
        if dir == ("right", "up"):
            self.ballRec.x += self.speed
            self.ballRec.y -= self.speed
        if dir == ("right", "down"):
            self.ballRec.x += self.speed
            self.ballRec.y += self.speed

        self.lastDir = dir


    def draw(self):
        pygame.draw.rect(self.surfrace, self.color, self.ballRect)


"""
    def resetBall(self, lastDir):
        if self.lastDir[0] == "left":
            self.move(("right", None))
        if self.lastDir[0] == "right":
            self.move(("left", None))
"""     

    