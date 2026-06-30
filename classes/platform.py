from constants import *
from classes.gameobject import *
    
class Platform(GameObject):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, image, width, height)
