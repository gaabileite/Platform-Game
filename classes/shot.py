from constants import *
from classes.movable import *

class Shot(Movable):
    def __init__(self, x, y, direction, image, animations):
        super().__init__(x, y, image, 0, shot_speed, 0, 39, 12, animations)
 
        self.direction = direction
    
    def move_bullet(self):
        self.move(self.direction)

    def update(self):
        self.move_bullet()
