import random
LOOPS_PER_ROUND = {0 : 0, 1 : 5, 2 : 7, 3 : 12}

COLLECTABLE_TYPES   = ['SEGUIDOR', 'PRODUTO', 'STORY']
COLLECTABLE_WEIGHTS = [0.50, 0.30, 0.20]
PRODUCTS = ['BASE', 'BODY SPLASH', 'PERFUME']

COLLECTABLE_PATTERNS = {
    0 : [],
    1: [
        (345, 300),
        (645, 240),
        (945, 180),
        (150, 480),
        (525, 480)
    ],
    2: [
        (345, 300),
        (645, 240),
        (945, 180),
        (150, 480),
        (525, 480),
        (405, 300),
        (750, 480)
    ],
    3: [
        (345, 300),
        (645, 240),
        (945, 180),
        (150, 480),
        (525, 480),
        (405, 300),
        (750, 480),
        (705, 240),
        (30,  480),
        (225, 480),
        (450, 480),
        (885, 480)
    ]
}

ENEMY_TYPES = ['FELCA', 'ANA CASTELA']
ENEMY_PATTERNS = {
    0: [],
    1: [
        (450, 120, 'FELCA'),
        (360, 150, 'ANA CASTELA'),
        (960, 60,  'ANA CASTELA'),
    ],
    2: [
        (750, 90,  'FELCA'),
        (555, 300, 'ANA CASTELA'),
        (960, 60,  'ANA CASTELA'),
    ],
    3: [
        (450, 60,  'FELCA'),
        (840, 120, 'FELCA'),
        (225, 300, 'ANA CASTELA'),
        (795, 300, 'ANA CASTELA'),
    ],
}

PLATFORM_TYPES = {'BIG': (240,30), 'MEDIUM': (150,30), 'SMALL': (90,30), 'BLOCK': (60,45)}
PLATFORM_PATTERNS = {
    0: [],
    1: [
        (300, 300, 'SMALL'),
        (600, 240, 'MEDIUM'),
        (900, 180, 'BIG'),
    ],
    2: [
        (315, 300, 'BIG'),
        (615, 240, 'MEDIUM'),
        (915, 180, 'MEDIUM'),
        (510, 390, 'SMALL'),
    ],
    3: [
        (315, 300, 'BIG'),
        (615, 240, 'MEDIUM'),
        (915, 180, 'BLOCK'),
        (180, 390, 'SMALL'),
        (750, 390, 'SMALL'),
    ],
}