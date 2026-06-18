import pygame
import math
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
        self.facing = 'right' # direção padrão
        self.just_shot = False # bool se acabou de atirar

    def handle_movement(self):
        if pygame.key.get_pressed()[K_d]:
            self.move('right')
            self.facing = 'right'

        if pygame.key.get_pressed()[K_a]:
            self.move('left')
            self.facing = 'left'

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
        # se K_e for apertado e acabou de tirar (no frame anterior) ou se a quantidade de tiros disponíveis for <= 0 ou se não apertar K_e, não há tiro
        if (pygame.key.get_pressed()[K_e] and self.just_shot) or self.shot_count <= 0 or not pygame.key.get_pressed()[K_e]:
            return None
        
        # se K_e for apertado, então acabou de atirar
        self.just_shot = pygame.key.get_pressed()[K_e]

        self.shot_count -= 1

        if pygame.key.get_pressed()[K_w]:
            return Shot(self.x + self.width // 2, self.y + self.height // 2, 'up')

        return Shot(self.x + self.width // 2, self.y + self.height // 2, self.facing)
