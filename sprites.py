import pygame
from pygame.locals import *

pygame.init()

#WIP
SPRITES = {
    'SEGUIDOR' : pygame.image.load("assets/collectables/seguidor.png").convert_alpha(),
    'BASE' : pygame.image.load("assets/collectables/base-product.png").convert_alpha(),
    'PERFUME' : pygame.image.load("assets/collectables/perfume-product.png").convert_alpha(),
    'BODY SPLASH' : pygame.image.load("assets/collectables/body-splash-product.png").convert_alpha(),
    'flag fase 1' : pygame.image.load("assets/flag1.png").convert_alpha(),
    'flag fase 2' : pygame.image.load("assets/flag2.png").convert_alpha(),
    'flag fase 3' : pygame.image.load("assets/flag3.png").convert_alpha(),
    'plataforma' : pygame.image.load("assets/plataformas/plataforma.png").convert_alpha(),
    'chao' : pygame.image.load("assets/plataformas/chao.png").convert_alpha(),
}

def load_frames(paths, size=(40, 60)):
    return [pygame.transform.scale(pygame.image.load(p).convert_alpha(), size) for p in paths]

ANIMATIONS_V = {
    'idle': {
        'right': load_frames(["assets/virginia/idle/virginia R.png"]),
        'left':  load_frames(["assets/virginia/idle/virginia L.png"]),
    },
    'run': {
        'right': load_frames([f"assets/virginia/virginia_run/run_direita#{i}.png"  for i in range(1, 5)]),
        'left':  load_frames([f"assets/virginia/virginia_run/run_esquerda#{i}.png" for i in range(1, 5)]),
    },
    'jump': {
        'right': load_frames([f"assets/virginia/jump/jumpR-frame{i}.png" for i in range(1, 4)]),
        'left':  load_frames([f"assets/virginia/jump/jumpL-frame{i}.png" for i in range(1, 4)]),
    },
    'shoot': {
        'right': load_frames([f"assets/virginia/shooting/shotR-frame{i}.png" for i in range(1, 4)]),
        'left':  load_frames([f"assets/virginia/shooting/shotL-frame{i}.png" for i in range(1, 4)]),
    }
}

ANIMATIONS_F = {
    'idle': {
        'right': load_frames([f"assets/front_inimigos/felca/cara do felca.png"]),
        'left': load_frames([f"assets/front_inimigos/felca/cara do felca.png"])
    },
    'dano': {
        'right': load_frames([f"assets/front_inimigos/felca/felca_dano.png"]),
        'left': load_frames([f"assets/front_inimigos/felca/felca_dano.png"])
    },
}

ANIMATIONS_A = {
    'idle': {
        'right': load_frames([f"assets/front_inimigos/ana castela/acastela_idle/acastela_idleR#{i}.png" for i in range(1, 3)]),
        'left': load_frames([f"assets/front_inimigos/ana castela/acastela_idle/acastela_idleL#{i}.png" for i in range(1, 3)])
    },
    'chase': {
        'right': load_frames([f"assets/front_inimigos/ana castela/acastela_chase/acastela_chase_direita#{i}.png" for i in range(1, 4)]),
        'left': load_frames([f"assets/front_inimigos/ana castela/acastela_chase/acastela_chase_esquerda#{i}.png" for i in range(1, 4)])
    }
}

ANIMATIONS_T = [load_frames([f"assets/tiro/frame-{i}.png" for i in range(1, 4)])]
