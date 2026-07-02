from constants import *
from classes.movable import *
import random

class Enemy(Movable):
    def __init__(self, x, y, image, type, animations):
        super().__init__(x, y, image, enemy_life, enemy_speed, enemy_boost, 60, 90, animations)
        self.type = type
        self.steal_timer = 0
        self.flying = (type == 'FELCA')
        self.facing = 'right'

    def follow_player(self, player):
        distance = self.get_distance(player)

        if self.type == 'FELCA':
            if distance <= persuit_range:
                if self.x < player.x:
                    self.move('right')
                    self.facing = 'right'
                elif self.x > player.x:
                    self.move('left')
                    self.facing = 'left'

                if self.y < player.y:
                    self.move('down')
                elif self.y > player.y:
                    self.move('up')

                self.steal_timer += 1
                if self.steal_timer >= 60:
                    steal = random.randint(3, 5)
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
    
    def update_animation(self):
        new_state = 'chase' if self.moving else 'idle'
        if new_state not in self.animations:
            new_state = 'idle'
        self.state = new_state

        self.image = self.animations[self.state][self.facing][0]
    
    def update(self, platforms, player):
        self.follow_player(player)
        if not self.flying:
            self.apply_gravity()
        self.check_platform_collision(platforms)
        self.update_animation()
