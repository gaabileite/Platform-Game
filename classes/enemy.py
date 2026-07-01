from constants import *
from classes.movable import *
import random

class Enemy(Movable):
    def __init__(self, x, y, image, type, animations):
        super().__init__(x, y, image, enemy_life, enemy_speed, enemy_boost, enemy_size, enemy_size, animations)
        self.type = type
        self.steal_timer = 0

    def follow_player(self, player):
        distance = self.get_distance(player)

        if self.type == 'Felca':
            if distance <= 30:
                if self.x < player.x:
                    self.move('right')
                    self.facing = 'right'
                elif self.x > player.x:
                    self.move('left')
                    self.facing = 'left'

                self.steal_timer += 1
                if self.steal_timer >= 60:
                    steal = random.randint(3000, 5000)
                    player.follower_count = max(0, player.follower_count - steal)
                    self.steal_timer = 0
            else:
                self.steal_timer = 0

        else:
            if distance <= persuit_range:
                if self.x < player.x:
                    self.move('right')
                    self.facing = 'right'
                elif self.x > player.x:
                    self.move('left')
                    self.facing = 'left'
            
    def get_shot(self, bullet):
        self.take_damage(bullet)

    def get_distance(self, player):
        return abs(self.x - player.x)
    
    def update(self, platforms, player):
        self.follow_player(player)
        self.apply_gravity()
        self.check_platform_collision(platforms)
