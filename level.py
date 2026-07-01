import random
from classes.platform import Platform
from classes.enemy import Enemy
from classes.collectable import *
from classes.flag import *
from constants import *
from sprites import *

REPEAT_DISTANCE = 320
REPEAT_COUNT = 5
LEVEL_WIDTH = REPEAT_DISTANCE * REPEAT_COUNT

def create_level(phase=1):
    death     = Platform(0, 180, LEVEL_WIDTH, 20, SPRITES['chao'])
    platforms = [Platform(0, 160, LEVEL_WIDTH, 20, SPRITES['chao'])]

    platform_pattern = [
        (100, 100, 60, 10),
        (200, 80,  60, 10),
        (300, 60,  60, 10),
    ]

    enemy_pattern = [(300, 100)]

    enemies          = []
    collectables_data = []

    for i in range(REPEAT_COUNT):
        for (x, y, largura, altura) in platform_pattern:
            platforms.append(Platform(x + i * REPEAT_DISTANCE, y, largura, altura, SPRITES['plataforma']))

        for (x, y) in enemy_pattern:
            if random.random() < 0.5:
                e = Enemy(x + i * REPEAT_DISTANCE, y, ANIMATIONS_F['idle'][0], 'Felca', ANIMATIONS_F)
            else:
                e = Enemy(x + i * REPEAT_DISTANCE, y, ANIMATIONS_F['idle'][0], 'Ana Castela', ANIMATIONS_A)
            enemies.append(e)

        for (x, y) in COLLECTABLE_PATTERNS[phase]:
            collectables_data.append((x + i * REPEAT_DISTANCE, y, pick_type()))

    flag = {
        1 : Flag(LEVEL_WIDTH - 40, 140, SPRITES['flag fase 1']),
        2 : Flag(LEVEL_WIDTH - 40, 140, SPRITES['flag fase 2']),
        3 : Flag(LEVEL_WIDTH - 40, 140, SPRITES['flag fase 3'])
    }

    return death, platforms, enemies, collectables_data, flag
