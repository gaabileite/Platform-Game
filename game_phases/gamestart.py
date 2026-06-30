import pygame
import math
from pygame.locals import *
from classes.gameobject import *
from classes.movable import *
from classes.player import *
from classes.enemy import *
from classes.shot import *
from classes.platform import *
from classes.collectable import *
from classes.camera import *
from constants import *
from level import *
from game_phases.gamerunning import *

pygame.init()

#imagem 
fundo         = pygame.transform.scale(pygame.image.load('bg_start.png'), (320, 180))

def gamestart(surface, player, enemies, death, platforms, shots, game_manager, flag):

    # Fundo escalado para 320x180
    surface.blit(fundo, (0, 0))

    if pygame.key.get_pressed()[K_SPACE]:
        death, platforms, enemies, flag = create_level()
        shots = []
        game_manager.current_phase = 1

    return player, enemies, death, platforms, shots, game_manager, flag