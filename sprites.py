import pygame
from pygame.locals import *

pygame.init()

#WIP
SPRITES = {
    'SEGUIDOR' : pygame.image.load("assets/collectables/seguidor.png").convert_alpha(),
    'BASE' : pygame.image.load("assets/collectables/base-product.png").convert_alpha(),
    'PERFUME' : pygame.image.load("assets/collectables/perfume-product.png").convert_alpha(),
    'BODY SPLASH' : pygame.image.load("assets/collectables/body-splash-product.png").convert_alpha(),
    'STORY' : pygame.image.load("assets/collectables/story.png").convert_alpha(),
    'flag' : pygame.image.load("assets/flag.png").convert_alpha(),
    'plataforma' : pygame.image.load("assets/plataformas/plataforma.png").convert_alpha(),
    'chao' : pygame.image.load("assets/plataformas/chao.png").convert_alpha(),
}

def load_frames(paths, size=(40, 60)):
    return [pygame.transform.scale(pygame.image.load(p).convert_alpha(), size) for p in paths]

ANIMATIONS_V = {
    'idle': {
        'right': load_frames(["assets/virginia/idle/virginia R.png"], (66, 102)),
        'left':  load_frames(["assets/virginia/idle/virginia L.png"], (66, 102)),
    },
    'run': {
        'right': load_frames(["assets/virginia/run/run_direita#3.png"], (66, 102)),
        'left':  load_frames(["assets/virginia/run/run_esquerda#3.png"], (66, 102)),
    },
    'jump': {
        'right': load_frames(["assets/virginia/jump/jumpR-frame3.png"], (66, 102)),
        'left':  load_frames(["assets/virginia/jump/jumpL-frame3.png"], (66, 102)),
    },
    'shoot': {
        'right': load_frames(["assets/virginia/shooting/shotR-frame3.png"], (66, 102)),
        'left':  load_frames(["assets/virginia/shooting/shotL-frame3.png"], (66, 102)),
    }
}

ANIMATIONS_F = {
    'idle': {
        'right': load_frames([f"assets/inimigos/felca/cara do felca.png"], (60, 90)),
        'left': load_frames([f"assets/inimigos/felca/cara do felca.png"], (60, 90))
    }
}

ANIMATIONS_A = {
    'idle': {
        'right': load_frames([f"assets/inimigos/ana castela/acastela_idle/acastela_idleR#1.png"], (60, 90)),
        'left': load_frames([f"assets/inimigos/ana castela/acastela_idle/acastela_idleL#1.png"], (60, 90))
    },
    'chase': {
        'right': load_frames([f"assets/inimigos/ana castela/acastela_chase/acastela_chase_direita#1.png"], (60, 90)),
        'left': load_frames([f"assets/inimigos/ana castela/acastela_chase/acastela_chase_esquerda#1.png"], (60, 90))
    }
}

ANIMATIONS_T = [load_frames([f"assets/tiro/frame-3.png"], (39, 12))]
