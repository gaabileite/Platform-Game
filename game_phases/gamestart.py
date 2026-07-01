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

bg_gamestart = pygame.transform.scale(pygame.image.load('assets/backgrounds/bg_start.png'), (320, 180))
btn_play = pygame.transform.scale(pygame.image.load('assets/backgrounds/btn-jogar.png'), (87, 23))

def gamestart(surface, player, enemies, death, platforms, shots, game_manager, flag, camera):
    coletaveis = []
    surface.blit(bg_gamestart, (0, 0))
    
    escala = 1.0 + math.sin(pygame.time.get_ticks() * 0.005) * 0.08
    btn_pulsante = pygame.transform.scale(btn_play, (int(87 * escala), int(23 * escala)))
    rect_pulsante  = btn_pulsante.get_rect(center=(160, 128))
    surface.blit(btn_pulsante, rect_pulsante)

    if pygame.key.get_pressed()[K_SPACE]:
        game_manager.current_phase = 1
        death, platforms, enemies, flag, coletaveis, shots, camera = create_level(game_manager.current_phase)

    return player, death, platforms, enemies, flag, coletaveis, shots, camera, game_manager