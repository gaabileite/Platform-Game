import pygame
from pygame.locals import *
from constants import *
from classes.movable import *

class Shot(Movable):
    def __init__(self, x, y, direction):
        super().__init__(x, y, shot_color, 0, shot_image, shot_speed, 0)
 
        self.direction = direction
    
    def move_bullet(self):
        self.move(self.direction)
