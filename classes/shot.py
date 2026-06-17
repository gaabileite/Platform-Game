import pygame
from pygame.locals import *
from constants import *
from classes.movable import *

class Shot(Movable):
    def __init__(self, x, y, vx, vy):
        super().__init__(x, y, shot_color, 0, shot_image, shot_speed, 0)
 
        self.vx = vx
        self.vy = vy
    
    def move_bullet(self):
        self.x += self.vx
        self.y += self.vy
