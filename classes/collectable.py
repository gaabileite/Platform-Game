from constants import *
from classes.gameobject import *

class Collectable(GameObject):
    def __init__(self, x, y, image, type):
        super().__init__(x, y, image, 42, 42)

        self.type = type
        self.y = y - self.height
        self.rect.y = self.y