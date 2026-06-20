import pygame
from pygame.locals import *
from constants import *

class GameObject:
    def __init__(self, x, y, color, width, height):
        self.x = int(x)
        self.y = int(y)
        self.width = width
        self.height = height
        self.color = color

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
