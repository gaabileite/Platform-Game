import random
LOOPS_PER_ROUND = {0 : 0, 1 : 5, 2 : 7, 3 : 12}

COLLECTABLE_TYPES   = ['SEGUIDOR', 'PRODUTO', 'STORY']
COLLECTABLE_WEIGHTS = [0.50, 0.30, 0.20]
PRODUCTS = ['BASE', 'BODY SPLASH', 'PERFUME']

COLLECTABLE_PATTERNS = {
    0 : [],
    1: [
        (115, 100),
        (215, 80),
        (315, 60),
        (50,  160),
        (175, 160)
    ],
    2: [
        (115, 100),
        (215, 80),
        (315, 60),
        (50,  160),
        (175, 160),
        (135, 100),
        (250, 160)
    ],
    3: [
        (115, 100),
        (215, 80),
        (315, 60),
        (50,  160),
        (175, 160),
        (135, 100),
        (250, 160),
        (235, 80),
        (10,  160),
        (75,  160),
        (150, 160),
        (295, 160)
    ]
}

ENEMY_TYPES = ['FELCA', 'ANA CASTELA']
ENEMY_PATTERNS = {
    0: [],
    1: [
        (150, 40,  'FELCA'),
        (120, 50,  'ANA CASTELA'),
        (320, 20,  'ANA CASTELA'),
    ],
    2: [
        (250, 30,  'FELCA'),
        (185, 100, 'ANA CASTELA'),
        (320, 20,  'ANA CASTELA'),
    ],
    3: [
        (150, 20,  'FELCA'),
        (280, 40,  'FELCA'),
        (75,  100, 'ANA CASTELA'),
        (265, 100, 'ANA CASTELA'),
    ],
}

PLATFORM_TYPES = {'BIG': (80,10), 'MEDIUM': (50,10), 'SMALL': (30,10), 'BLOCK': (20,15)}
PLATFORM_PATTERNS = {
    0: [],
    1: [
        (100, 100, 'SMALL'),
        (200, 80,  'MEDIUM'),
        (300, 60,  'BIG'),
    ],
    2: [
        (105, 100, 'BIG'),
        (205, 80,  'MEDIUM'),
        (305, 60,  'MEDIUM'),
        (170, 130, 'SMALL'),
    ],
    3: [
        (105, 100, 'BIG'),
        (205, 80,  'MEDIUM'),
        (305, 60,  'BLOCK'),
        (60,  130, 'SMALL'),
        (250, 130, 'SMALL'),
    ],
}