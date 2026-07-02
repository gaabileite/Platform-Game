import pygame
from pygame.locals import *
from constants import *
from classes.movable import *
from classes.shot import *
from sprites import *
from sounds import tocar

class Player(Movable):
    def __init__(self, x, y, animations):
        super().__init__(x, y, animations['idle']['right'][0], player_life, player_speed, player_boost, 66, 102, animations)

        self.follower_count = 0
        self.shot_count = 0
        self.story_count = 0
        self.facing = 'right'
        self.just_shot = False
        self.damage_cooldown = 0
        self.newlife = 0
        self.shoot_timer = 0

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
        if self.check_collision(collectable) and collectable.type == 'STORY':
            self.story_count += 1

            if self.story_count == 5:
                if self.life < 5:
                    self.life += 1
                    self.story_count = 0
                    self.newlife = 60
                else:
                    self.follower_count += 50

        elif self.check_collision(collectable) and collectable.type == 'SEGUIDOR':
            self.follower_count += 10
            tocar('follower')

        elif self.check_collision(collectable) and collectable.type == 'BASE':
            self.shot_count -= 1

        elif self.check_collision(collectable) and collectable.type == 'BODY SPLASH':
            self.shot_count += 1

        elif self.check_collision(collectable) and collectable.type == 'PERFUME':
            self.shot_count += 3

    def shoot(self):
        if (pygame.key.get_pressed()[K_e] and self.just_shot) or self.shot_count <= 0 or not pygame.key.get_pressed()[K_e]:
            return None
        
        self.just_shot = pygame.key.get_pressed()[K_e]
        self.shot_count -= 1
        tocar('shot')
        self.shoot_timer = 12

        if pygame.key.get_pressed()[K_w]:
            return Shot(self.x + self.width // 2, self.y + self.height // 2, 'up', ANIMATIONS_T[0][0], ANIMATIONS_T)

        return Shot(self.x + self.width // 2, self.y + self.height // 2, self.facing, ANIMATIONS_T[0][0], ANIMATIONS_T)
    
    def reset(self):
        self.x = player_starter_x
        self.y = player_starter_y
        self.vy = 0
        self.on_ground = True
        self.life = player_life
        self.follower_count = 0
        self.shot_count = 0
        self.story_count = 0
        self.facing = 'right'
        self.just_shot = False
        self.damage_cooldown = 0

    def take_contact_damage(self):
        if self.damage_cooldown == 0:
            self.life -= 1
            self.damage_cooldown = 90

    def update_animation(self):
        if self.shoot_timer > 0:
            self.state = 'shoot'
        elif not self.on_ground:
            self.state = 'jump'
        elif self.moving:
            self.state = 'run'
        else:
            self.state = 'idle'

        self.image = self.animations[self.state][self.facing][0]

    def update(self, platforms):
        if self.damage_cooldown > 0:
            self.damage_cooldown -= 1
        self.apply_gravity()
        self.check_platform_collision(platforms)
        self.update_animation()
