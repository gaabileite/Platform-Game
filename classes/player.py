import pygame
from pygame.locals import *
from constants import *
from classes.movable import *
from classes.shot import *

class Player(Movable):
    def __init__(self, x, y, animations):
        super().__init__(x, y, animations['idle']['right'][0], player_life, player_speed, player_boost, player_size, player_size, animations)

        self.follower_count = 0
        self.shot_count = 0
        self.story_count = 0
        self.facing = 'right'
        self.just_shot = False
        self.damage_cooldown = 0

    def handle_movement(self):
        self.moving = False
                
        if pygame.key.get_pressed()[K_d]:
            self.move('right')
            self.facing = 'right'
            self.moving = True

        if pygame.key.get_pressed()[K_a]:
            self.move('left')
            self.facing = 'left'
            self.moving = True

        if pygame.key.get_pressed()[K_SPACE]:
            self.move('jump')

    def add_collectable(self, collectable):
        if self.check_collision(collectable) and collectable.type == 'story':
            self.story_count += 1

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
        if (pygame.key.get_pressed()[K_e] and self.just_shot) or self.shot_count <= 0 or not pygame.key.get_pressed()[K_e]:
            return None
        
        self.just_shot = pygame.key.get_pressed()[K_e]
        self.shot_count -= 1

        if pygame.key.get_pressed()[K_w]:
            return Shot(self.x + self.width // 2, self.y + self.height // 2, 'up')

        return Shot(self.x + self.width // 2, self.y + self.height // 2, self.facing)
    
    def take_contact_damage(self):
        if self.damage_cooldown == 0:
            self.life -= 1
            self.damage_cooldown = 90

    def update(self, platforms):
        if self.damage_cooldown > 0:
            self.damage_cooldown -= 1
        self.apply_gravity()
        self.check_platform_collision(platforms)
        self.update_animation()
