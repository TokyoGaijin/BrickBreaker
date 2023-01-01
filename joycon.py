import pygame
from pygame import joystick
from enum import Enum

"""
A custom library and class that maps the Nintendo Switch Joyconn Controller.
Specifically, Joy-Con L (minus) controller.

Includes inputs for all butons, *except* for the capture button.
"""

pygame.joystick.init()

class ButtonStates(Enum):
    # The key maps for the controllers
    # Enumerated to correspond to which buttons are which
    HAT_X = "X AXIS"
    HAT_Y = "Y AXIS"
    Y = 2
    X = 3
    B = 0
    A = 1
    L = 4
    R = 5
    SIGN_BUTTON = 9
    SHOULDER = 8
    TRIGGER = 6
    FUNCTION = 16


class JoyCon(object):
    def __init__(self, surface):
        self.surface = surface
        self.events = pygame.event.get()
        self.button_pressed = None
        self.axis = None

        
    def update_controller(self):
        pass
