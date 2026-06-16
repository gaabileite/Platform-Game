import pygame
from pygame.locals import *
from constants import *

class Camera:
    def __init__(self, level_width):
        self.x = 0
        self.level_width = level_width

    def follow(self, target):
        self.x = target.x - internal_width // 2
        self.x = max(0, min(self.x, self.level_width - internal_width))
    
    def apply(self, object):
        return object.x - self.x, object.y, object.width, object.height
