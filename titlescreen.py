from turtle import width
import pygame
import colorswatch as cs

"""
Draws and displays title graphics on the screen.
For the title screen art.

"""

room = ["----------------",
        "BB-RR-EEE-A-K--K",
        "B-BR-RE--A-AK-K-",
        "BB-RR-EE-AAAKK--",
        "B-BR-RE--A-AK-K-",
        "BB-R-REEEA-AK--K",
        "--A-W-W-W-A-Y--Y",
        "-A-AW-W-WA-A-Y-Y",
        "-AAAW-W-WAAA--Y-",
        "-A-AW-W-WA-A-Y--",
        "-A-A-W-W-A-A-Y--",
        "----------------",
        "----------------",
        "----------------",
        "----------------"]

red = cs.red["pygame"]
yellow = cs.yellow["pygame"]
blue = cs.blue["pygame"]
black = cs.black["pygame"]
green = cs.green["pygame"]



def draw_title(surface):
    pixel_list = []
    x, y = 0, 0
    w, h = 50, 40
    for row in room:
        for col in row:
            if col == "B":
                pixel_list.append(pygame.draw.rect(surface, yellow, pygame.Rect(x, y, w, h)))
            if col == "R":
                pixel_list.append(pygame.draw.rect(surface, red, pygame.Rect(x, y, w, h)))
            if col == "E":
                pixel_list.append(pygame.draw.rect(surface, blue, pygame.Rect(x, y, w, h)))
            if col == "A":
                pixel_list.append(pygame.draw.rect(surface, green, pygame.Rect(x, y, w, h)))
            if col == "K":
                pixel_list.append(pygame.draw.rect(surface, blue, pygame.Rect(x, y, w, h)))
            if col == "W":
                pixel_list.append(pygame.draw.rect(surface, red, pygame.Rect(x, y, w, h)))
            if col == "Y":
                pixel_list.append(pygame.draw.rect(surface, yellow, pygame.Rect(x, y, w, h)))
         
            x += w
        y += h
        x = 0









