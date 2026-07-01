import random
from classes.platform import Platform
from classes.enemy import Enemy
from classes.collectable import Collectable
from classes.flag import Flag
from constants import *
from sprites import *
from spawn import *
from classes.camera import Camera

REPEAT_DISTANCE = 320
def pick_collectable_type():
    tipo = random.choices(COLLECTABLE_TYPES, weights=COLLECTABLE_WEIGHTS)[0]
    if tipo == 'PRODUTO':
        return random.choice(PRODUCTS)
    return tipo

def create_level(phase):
    repeat_count = LOOPS_PER_ROUND[phase]
    level_width = REPEAT_DISTANCE * repeat_count

    death = Platform(0, 180, level_width, 20, SPRITES['chao'])
    platforms = [Platform(0, 160, level_width, 20, SPRITES['chao'])]

    enemies = []
    collectables = []

    platform_pattern = PLATFORM_PATTERNS[phase]
    enemy_pattern = ENEMY_PATTERNS[phase]
    collectable_pattern = COLLECTABLE_PATTERNS[phase]

    #Criação de loop de acordo com o LOOPS_PER_ROUND da fase, preenchendo plataformas, inimigos e coletáveis
    for i in range(repeat_count):
        for (x, y, tamanho) in platform_pattern:
            w, h = PLATFORM_TYPES[tamanho]
            platforms.append(Platform(x + i * REPEAT_DISTANCE, y, w, h, SPRITES['plataforma']))

        for (x, y, tipo) in enemy_pattern:
            animacoes = ANIMATIONS_F if tipo == 'FELCA' else ANIMATIONS_A
            enemies.append(Enemy(x + i * REPEAT_DISTANCE, y, animacoes['idle']['right'][0], tipo, animacoes))

        for (x, y) in collectable_pattern:
            tipo = pick_collectable_type()
            collectables.append(Collectable(x + i * REPEAT_DISTANCE, y, SPRITES.get(tipo, SPRITES['seguidor']), tipo))

    #Criação da bandeira no final do nível
    flag = {
        1: Flag(level_width - 40, 140, SPRITES['flag fase 1']),
        2: Flag(level_width - 40, 140, SPRITES['flag fase 2']),
        3: Flag(level_width - 40, 140, SPRITES['flag fase 3']),
    }

    return death, platforms, enemies, flag, collectables, Camera(level_width)