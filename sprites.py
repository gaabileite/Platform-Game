import pygame
from pygame.locals import *

pygame.init()

#WIP
SPRITES = {
    'seguidor' : pygame.image.load("assets/collectables/seguidor.png").convert_alpha(),
    'base' : pygame.image.load("assets/collectables/base-product.png").convert_alpha(),
    'perfume' : pygame.image.load("assets/collectables/perfume-product.png").convert_alpha(),
    'bodysplash' : pygame.image.load("assets/collectables/body-splash-product.png").convert_alpha(),
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
    'idle' : load_frames([f"assets/front_inimigos/felca/cara do felca.png"]),
    'dano' : load_frames([f"assets/front_inimigos/felca/felca_dano.png"])
}

ANIMATIONS_A = {

}

ANIMATIONS_T = {

}
