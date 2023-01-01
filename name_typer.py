import pygame
import writer
import colorswatch as cs

class Name_Typer(object):
    def __init__(self, surface):
        self.surface = surface
        self.writer = writer.Writer(self.surface)
        self.initial_string = None
        self.letter_block = None
        self.posX = 0
        self.posY = 0
        self.gap = 24
        self.keys = pygame.key.get_pressed()
        self.cursor = None
        self.letterRect = []
        self.row1 = ["A-B-C-D-E-F-G"]
        self.row2 = ["H-I-J-K-L-M-N"]
        self.row3 = ["O-P-Q-R-S-T-U"]
        self.row4 = ["V-W-X-Y-Z-.-←"]
        self.row5 = ["END"]
        self.keyboard = [self.row1, self.row2, self.row3, self.row4, self.row5]


    def display_alpha(self, posX, posY):
        self.posX = posX
        self.posY = posY
        letterRectX = posX
        letterRectY = posY
        self.cursor = pygame.Rect(posX, posY, 12, 12)

        pygame.draw.rect(self.surface, cs.red["pygame"], self.cursor)


        for row in self.keyboard:
            for col in row:
                self.letterRect.append(pygame.Rect(letterRectX, letterRectY, 12, 12))
              
            letterRectX += self.gap
              

            letterRectY += self.gap
            letterRectX = posX

        for backBlocks in self.letterRect:
            pygame.draw.rect(self.surface, cs.blue["pygame"], backBlocks)


        self.writer.write_string(self.row1, posX, posY, color = cs.white["pygame"])
        self.writer.write_string(self.row2, posX, posY + self.gap, color = cs.white["pygame"])
        self.writer.write_string(self.row3, posX, posY + self.gap * 2, color = cs.white["pygame"])
        self.writer.write_string(self.row4, posX, posY + self.gap * 3, color = cs.white["pygame"])
        self.writer.write_string(self.row5, posX, posY + self.gap * 4, color = cs.white["pygame"])

        


    def moveCursor(self, direction):
        pass


    def keyCommands(self):
        pass


    