from constants import *
from classes.gameobject import *
    
class Platform(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, platform_color, width, height)
