import pygame
from pygame.locals import *
from constants import *
from classes.gameobject import *
    
class Movable(GameObject):
    def __init__(self, x, y, color, life, image, speed, boost):
        super().__init__(x, y, color, image)

        self.speed = speed
        self.boost = boost
        self.life = life
        self.vy = 0
        self.on_ground = True

    def apply_gravity(self):
        if not self.on_ground:
            self.vy += gravity
            self.y += self.vy

    def check_platform_collision(self, platforms): #platforms is the list of platform objects
        self.on_ground = False

        for platform in platforms:
            if self.get_rect().colliderect(platform.get_rect()):
                if self.vy >= 0:
                    self.y = platform.y - self.height
                    self.vy = 0
                    self.on_ground = True
                    break
    
    def move(self, direction):
        if direction == 'right':
            self.x += self.speed
        
        elif direction == 'left':
            self.x -= self.speed
        
        elif direction == 'jump' and self.on_ground:
            self.vy = -self.boost
            self.on_ground = False

    def check_collision(self, other):
        return self.get_rect().colliderect(other.get_rect())
    
    def take_damage(self, other):
        if self.check_collision(other):
            self.life -= 1 
    
    def update(self, platforms):
        self.apply_gravity()
        self.check_platform_collision(platforms)
