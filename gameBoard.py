import pygame
import colorswatch as cs

class BGBricks(object):
    def __init__(self, surface, locX, locY):
        self.surface = surface
        self.locX = locX
        self.locY = locY
        self.borderColor = cs.black["pygame"]
        self.contourColor = cs.night_gray["pygame"]
        self.surfaceColor = cs.dark_gray["pygame"]
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
        self.borderRectColor = cs.deep_purple["pygame"]
        self.bg = []
        for x in range(0, 800, 100):
            for y in range(0, 600, 40):
                self.bg.append(BGBricks(self.surface, x, y))

        self.room = [["--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                     
                     ["--------",
                      "--------",
                      "--------",
                      "--------",
                      "-111111-",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],

                     ["--------",
                      "--------",
                      "--------",
                      "-111111-",
                      "--1111--",
                      "---11---",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],

                     ["--------",
                      "--------",
                      "--------",
                      "-111111-",
                      "-111111-",
                      "---22---",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--------",
                      "-111111-",
                      "-11--11-",
                      "---22---",
                      "-222222-",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--------",
                      "-11--11-",
                      "---22---",
                      "-22--22-",
                      "---22---",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--1111--",
                      "---11---",
                      "-222222-",
                      "-22--22-",
                      "---22---",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--------",
                      "---11---",
                      "-22--22-",
                      "---11---",
                      "-222222-",
                      "-33--33-",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--------",
                      "-131313-",
                      "-222222-",
                      "-22--22-",
                      "---22---",
                      "-33--22-",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--------",
                      "11111111",
                      "22222222",
                      "33322211",
                      "11111111",
                      "22112211",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--------",
                      "---11---",
                      "---33---",
                      "---22---",
                      "---44---",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--------",
                      "111--111",
                      "-223322-",
                      "42222224",
                      "-11--11-",
                      "222--222",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],

                     ["--------",
                      "--------",
                      "--------",
                      "12341234",
                      "33333333",
                      "2------2",
                      "33333333",
                      "444--444",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--------",
                      "11221122",
                      "3434--34",
                      "1111--11",
                      "22222111",
                      "33311---",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--------",
                      "1144----",
                      "-1144---",
                      "--114444",
                      "-1144---",
                      "1144----",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                          
                     ["--------",
                      "--------",
                      "--------",
                      "---1----",
                      "--2-2---",
                      "-3---3--",
                      "-432-4--",
                      "-4--14--",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"],
                         
                     ["--------",
                      "--------",
                      "--------",
                      "11111111",
                      "33333333",
                      "42342341",
                      "33221123",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------",
                      "--------"]]


    def draw(self):
        pygame.draw.rect(self.surface, self.borderRectColor, self.topRect)
        pygame.draw.rect(self.surface, self.borderRectColor, self.sideRect[0])
        pygame.draw.rect(self.surface, self.borderRectColor, self.sideRect[1])

       

