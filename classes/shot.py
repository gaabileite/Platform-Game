from constants import *
from classes.movable import *

class Shot(Movable):
    def __init__(self, x, y, direction):
        super().__init__(x, y, shot_color, 0, shot_speed, 0, shot_size, shot_size)
 
        self.direction = direction
    
    def move_bullet(self):
        self.move(self.direction)

    def update(self):
        self.move_bullet()
