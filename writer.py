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


    def write_string(self, string_toWrite, posX = None, posY = None, size = None, color = None):
        locals_dict = locals()

        for args in ["posX", "posY", "size", "color"]:
            if locals_dict[args] == None:
                locals_dict[args] = getattr(self, args)

        showtext = self.renderFont.render(string_toWrite, locals_dict["size"], locals_dict["color"])
        self.surface.blit(showtext, (locals_dict["posX"], locals_dict["posY"]))
