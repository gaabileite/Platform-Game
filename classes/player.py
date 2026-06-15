import pygame
from pygame.locals import *
from constants import *
from classes.movable import *
from classes.shot import *

class Player(Movable):
    def __init__(self, x, y):
        super().__init__(x, y, player_color, player_life, player_image, player_speed, player_boost)

        self.follower_count = 0
        self.shot_count = 0
        self.story_count = 0
    
    def handle_movement(self):
        if pygame.key.get_pressed()[K_d]:
            self.move('right')

        if pygame.key.get_pressed()[K_a]:
            self.move('left')

        if pygame.key.get_pressed()[K_SPACE]:
            self.move('jump')

    def add_collectable(self, collectable):
        if self.check_collision(collectable) and collectable.type == 'story':
            self.story_count +=1

            if self.story_count == 5:
                if self.life < 5:
                    self.life += 1
                    self.story_count = 0
                else:
                    self.follower_count += 50

        elif self.check_collision(collectable) and collectable.type == 'follower':
            self.follower_count += 10

        elif self.check_collision(collectable) and collectable.type == 'bad product':
            self.shot_count -= 1

        elif self.check_collision(collectable) and collectable.type == 'neutral product':
            self.shot_count += 1

        elif self.check_collision(collectable) and collectable.type == 'good product':
            self.shot_count += 3
    
    def shoot(self):
        if pygame.key.get_pressed()[K_RIGHT] and self.shot_count > 0:
            self.shot_count -= 1
            return Shot(self.x, self.y, 'right')

        elif pygame.key.get_pressed()[K_LEFT] and self.shot_count > 0:
            self.shot_count -= 1
            return Shot(self.x, self.y, 'left')

    def update_player_choices(self):
        self.handle_movement()
        self.shoot()
