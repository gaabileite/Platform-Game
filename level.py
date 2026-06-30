from classes.platform import Platform
from classes.enemy import Enemy
from constants import *
from classes.flag import *
from sprites import *
import random

REPEAT_DISTANCE = 320
REPEAT_COUNT = 5
LEVEL_WIDTH = REPEAT_DISTANCE * REPEAT_COUNT

def create_level():
    death = Platform(0, 180, LEVEL_WIDTH, 20, SPRITES['chao'])

    platforms = [
        Platform(0, 160, LEVEL_WIDTH, 20),
    ]

    #SPAWN PATTERN (WIP/BACK)
    platform_pattern = [
        (100, 100, 60, 10),
        (200, 80, 60, 10),
        (300, 60, 60, 10),
    ]

    enemy_pattern = [
        (300, 100)
    ]

    #Criação de loop de acordo com a REPEAT_COUNT para preencher o nível com plataformas e inimigos
    options = [
        Enemy(x + i * REPEAT_DISTANCE, y, 'Felca', ANIMATIONS_F['idle']), 
        Enemy(x + i * REPEAT_DISTANCE, y, 'Ana Castela', ANIMATIONS_A['idle'])]
    enemies = []
    for i in range(REPEAT_COUNT):
        for (x, y, largura, altura) in platform_pattern:
            platforms.append(Platform(x + i * REPEAT_DISTANCE, y, largura, altura, SPRITES['plataforma']))
        for (x, y) in enemy_pattern:
            enemies.append(random.choice(options))

    #Criação da bandeira no final do nível
    flag = {
        1 : Flag(LEVEL_WIDTH - 40, 140, SPRITES['flag fase 1']),
        2 : Flag(LEVEL_WIDTH - 40, 140, SPRITES['flag fase 2']),
        3 : Flag(LEVEL_WIDTH - 40, 140, SPRITES['flag fase 3'])
    }

    return death, platforms, enemies, flag, []
