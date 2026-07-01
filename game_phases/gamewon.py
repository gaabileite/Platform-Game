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

bg_gamewon = pygame.transform.scale(pygame.image.load('assets/backgrounds/bg_gamewin.png'), (960, 540))
btn_playagain = pygame.transform.scale(pygame.image.load('assets/backgrounds/btn-tentar-novamente.png'), (261, 69))

def gamewon(surface, player, enemies, death, platforms, shots, game_manager, flag, camera):
    coletaveis = []
    surface.blit(bg_gamewon, (0, 0))
    
    escala = 1.0 + math.sin(pygame.time.get_ticks() * 0.005) * 0.08
    btn_pulsante = pygame.transform.scale(btn_playagain, (int(261 * escala), int(69 * escala)))
    rect_pulsante  = btn_pulsante.get_rect(center=(160, 128))
    surface.blit(btn_pulsante, rect_pulsante)

    if pygame.key.get_pressed()[K_SPACE]:
        game_manager.current_phase = 1
        player.reset()
        death, platforms, enemies, flag, coletaveis, shots, camera = create_level(game_manager.current_phase)

    return player, death, platforms, enemies, flag, coletaveis, shots, camera, game_manager