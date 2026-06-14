import pygame
from pygame.locals import *
from constants import *
from classes.movable import *

class Enemy(Movable):
    def __init__(self, x, y, life):
        super().__init__(x, y, enemy_color, life, enemy_image, enemy_speed, enemy_boost)

    def follow_player(self, player):
        if self.x < player.x:
            self.move('right')

        if self.x > player.x:
            self.move('left')
            
    def get_shot(self, bullet):
        self.take_damage(bullet)

    def get_distance(self, player):
        return abs(self.x - player.x)
