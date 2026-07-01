from constants import *
from classes.gameobject import *

class Collectable(GameObject):
    def __init__(self, x, y, image, type):
        super().__init__(x, y, image, collectable_size, collectable_size)

        self.type = type