from constants import *
from classes.gameobject import *

class Flag(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, image, flag_width, flag_height)
