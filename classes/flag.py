from constants import *
from classes.gameobject import *

class Flag(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, flag_color, flag_width, flag_height)
