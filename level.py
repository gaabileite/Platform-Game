from classes.platform import Platform
from classes.enemy import Enemy
from constants import *
from classes.flag import *

REPEAT_DISTANCE = 320
REPEAT_COUNT = 5
LEVEL_WIDTH = REPEAT_DISTANCE * REPEAT_COUNT

def create_level():
    death = Platform(0, 180, LEVEL_WIDTH, 20)

    platforms = [
        Platform(0, 160, LEVEL_WIDTH, 20),
    ]

    #Padrão de spawn de plataformas e inimigos, repetido ao longo do nível
    platform_pattern = [
        (100, 100, 60, 10),
        (200, 80, 60, 10),
        (300, 60, 60, 10),
    ]

    enemy_pattern = [
        (300, 100)
    ]

    #Criação de loop de acordo com a REPEAT_COUNT para preencher o nível com plataformas e inimigos
    enemies = []
    for i in range(REPEAT_COUNT):
        for (x, y, largura, altura) in platform_pattern:
            platforms.append(Platform(x + i * REPEAT_DISTANCE, y, largura, altura))
        for (x, y) in enemy_pattern:
            enemies.append(Enemy(x + i * REPEAT_DISTANCE, y))

    #Criação da bandeira no final do nível
    flag = Flag(LEVEL_WIDTH - 40, 140)

    return death, platforms, enemies, flag, []
