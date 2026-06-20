from constants import *
from classes.gameobject import *
    
class Movable(GameObject):
    def __init__(self, x, y, color, life, speed, boost, width, height):
        super().__init__(x, y, color, width, height)

        self.speed = speed
        self.boost = boost
        self.life = life
        self.vy = 0
        self.on_ground = True

    def apply_gravity(self):
        if not self.on_ground:
            self.vy += gravity
            self.y += self.vy

    def check_platform_collision(self, platforms):
        self.on_ground = False

        for platform in platforms:
            if self.check_collision(platform):
                if self.vy >= 0:
                    self.y = platform.y - self.height
                    self.vy = 0
                    self.on_ground = True
                    break
    
    def move(self, direction):
        if direction == 'right':
            self.x += self.speed
        
        elif direction == 'left':
            self.x = max(0, self.x - self.speed)

        elif direction == 'up':
            self.y -= self.speed
        
        elif direction == 'jump' and self.on_ground:
            self.vy = -self.boost
            self.on_ground = False

    def check_collision(self, other):
        return self.get_rect().colliderect(other.get_rect())
    
    def take_damage(self, other):
        if self.check_collision(other):
            self.life -= 1 
