import random
from constants import *
from classes.gameobject import *
from sprites import *

# Tipos e frequências de spawn (documento: 50% seguidor, 30% produto, 20% story)
COLLECTABLE_TYPES   = ['seguidor', 'base', 'bodysplash', 'perfume', 'story']
COLLECTABLE_WEIGHTS = [50, 10, 10, 10, 20]

# Posições relativas por bloco — fase 1: 5×5=25, fase 2: 7×5=35, fase 3: 12×5=60
COLLECTABLE_PATTERNS = {
    1: [
        (115, 100 - collectable_size),
        (215, 80  - collectable_size),
        (315, 60  - collectable_size),
        (50,  160 - collectable_size),
        (175, 160 - collectable_size),
    ],
    2: [
        (115, 100 - collectable_size),
        (215, 80  - collectable_size),
        (315, 60  - collectable_size),
        (50,  160 - collectable_size),
        (175, 160 - collectable_size),
        (135, 100 - collectable_size),
        (250, 160 - collectable_size),
    ],
    3: [
        (115, 100 - collectable_size),
        (215, 80  - collectable_size),
        (315, 60  - collectable_size),
        (50,  160 - collectable_size),
        (175, 160 - collectable_size),
        (135, 100 - collectable_size),
        (250, 160 - collectable_size),
        (235, 80  - collectable_size),
        (10,  160 - collectable_size),
        (75,  160 - collectable_size),
        (150, 160 - collectable_size),
        (295, 160 - collectable_size),
    ],
}

class Collectable(GameObject):
    def __init__(self, x, y, image, type):
        super().__init__(x, y, image, collectable_size, collectable_size)
        self.type = type

        if type == 'seguidor':
            self.percentage = 50
        elif type == 'story':
            self.percentage = 20
        else:
            self.percentage = 10

def pick_type():
    return random.choices(COLLECTABLE_TYPES, weights=COLLECTABLE_WEIGHTS)[0]

def make_collectables(collectables_data):
    return [Collectable(x, y, SPRITES.get(t, SPRITES['seguidor']), t)
            for x, y, t in collectables_data]
