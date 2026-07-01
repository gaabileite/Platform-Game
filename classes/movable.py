from constants import *
from classes.gameobject import *
    
class Movable(GameObject):
    def __init__(self, x, y, image, life, speed, boost, width, height, animations):
        super().__init__(x, y, image, width, height)

        self.state = 'idle'
        self.frame_index = 0
        self.anim_counter = 0
        self.anim_speed = 6
        self.moving = False

        self.facing = 'right'
        self.speed = speed
        self.animations = animations
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

    def update_animation(self):
        if not self.on_ground:
            new_state = 'jump'
        elif self.moving:
            new_state = 'run'
        else:
            new_state = 'idle'

        if new_state != self.state:
            self.state = new_state
            self.frame_index = 0
            self.anim_counter = 0

        frames = self.animations[self.state][self.facing]

        self.anim_counter += 1
        if self.anim_counter >= self.anim_speed:
            self.anim_counter = 0
            self.frame_index = (self.frame_index + 1) % len(frames)

        self.image = frames[self.frame_index]
