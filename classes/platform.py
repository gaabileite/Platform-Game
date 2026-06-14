import pygame
from pygame.locals import *
from constants import *
from classes.gameobject import *
    
class Platform(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, platform_color, platform_image)

        self.width = width
        self.height = height
