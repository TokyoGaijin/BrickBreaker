import pygame.freetype
import os
import colorswatch as cs

# A text display module for pygame

pygame.font.init()

class Writer(object):
    def __init__(self, surface, posX, posY, color = cs.cornflower_blue["pygame"], size = 12, font = "arcade_font.ttf"):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.color = color
        self.size = size
        self.font = font
        self.renderFont = pygame.font.Font(os.path.join("fonts", self.font), self.size)


    def write_string(self, string_toWrite):
        showtext = self.renderFont.render(string_toWrite, self.size, self.color)
        self.surface.blit(showtext, (self.posX, self.posY))
