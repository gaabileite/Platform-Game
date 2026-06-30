from constants import *
from classes.movable import *

class Enemy(Movable):
    def __init__(self, x, y, image, type, screen):
        super().__init__(x, y, image, enemy_life, enemy_speed, enemy_boost, enemy_size, enemy_size, screen)
        self.type = type

    def follow_player(self, player):
        if self.x < player.x:
            self.move('right')

        if self.x > player.x:
            self.move('left')
            
    def get_shot(self, bullet):
        self.take_damage(bullet)

    def get_distance(self, player):
        return abs(self.x - player.x)
    
    def update(self, platforms, player):
        self.follow_player(player)
        self.apply_gravity()
        self.check_platform_collision(platforms)
