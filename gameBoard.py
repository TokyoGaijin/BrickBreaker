import pygame
import colorswatch as cs

class BGBricks(object):
    def __init__(self, surface, locX, locY):
        self.surface = surface
        self.locX = locX
        self.locY = locY
        self.borderColor = cs.black["pygame"]
        self.contourColor = cs.dark_gray["pygame"]
        self.surfaceColor = cs.gray["pygame"]
        self.borderRect = pygame.Rect(locX, locY, 100, 40)
        self.contourRect = pygame.Rect(locX + 5, locY + 5, 95, 35)
        self.surfaceRect = pygame.Rect(locX + 10, locY + 10, 95, 35)


    def draw(self):
        pygame.draw.rect(self.surface, self.borderColor, self.borderRect)
        pygame.draw.rect(self.surface, self.surfaceColor, self.contourRect)
        pygame.draw.rect(self.surface, self.contourColor, self.surfaceRect)




class GameBoard(object):
    """
    Design of a gameboard that is displayed on the screen.
    Comes complete with graphical background and borders for the ball to bounce off of.
    """
    def __init__(self, surface):
        self.surface = surface
        self.bgRect = pygame.Rect(0, 0, 800, 600)
        self.topRect = pygame.Rect(0, 0, 800, 20)
        self.sideRect = [pygame.Rect(0, 0, 20, 600), pygame.Rect(780, 0, 20, 600)]
        self.borderRectColor = cs.cornflower_blue["pygame"]
        self.bg = []
        for x in range(0, 800, 100):
            for y in range(0, 600, 40):
                self.bg.append(BGBricks(self.surface, x, y))


    def draw(self):
        for i in range(0, len(self.bg)):
            self.bg[i].draw()

        pygame.draw.rect(self.surface, self.borderRectColor, self.topRect)
        pygame.draw.rect(self.surface, self.borderRectColor, self.sideRect[0])
        pygame.draw.rect(self.surface, self.borderRectColor, self.sideRect[1])
        
