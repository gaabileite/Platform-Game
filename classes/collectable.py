import pygame
from pygame.locals import *
from constants import *
from classes.gameobject import *

class Collectable(GameObject):
    def __init__(self, x, y, color, image, type):
        super().__init__(x, y, color, image)

        self.type = type

        if 'follower' in type:
            self.percentage = 50

        if 'story' in type:
            self.percentage = 20

        if 'product' in type:
            self.percentage = 10
