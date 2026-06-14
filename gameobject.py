import pygame
from pygame.locals import *
from constants import *

class GameObject:
    def __init__(self, x, y, color, image):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.color = color
        self.image = image

    def get_rect(self):
        return self.x, self.y, self.width, self.height
