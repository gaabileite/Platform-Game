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
from w.level import *
from game_phases.w.gamerunning import *

pygame.init()

bg_gamewon = pygame.transform.scale(pygame.image.load('bg-vitoria.png'), (320, 180))
btn_playagain = pygame.transform.scale(pygame.image.load('btn-tentar-novamente.png'), (87, 23))

def gamewon(surface, player, enemies, death, platforms, shots, game_manager, flag):

    surface.blit(bg_gamewon, (0, 0))
    
    escala = 1.0 + math.sin(pygame.time.get_ticks() * 0.005) * 0.08
    btn_pulsante = pygame.transform.scale(btn_playagain, (int(87 * escala), int(23 * escala)))
    rect_pulsante  = btn_pulsante.get_rect(center=(160, 128))
    surface.blit(btn_pulsante, rect_pulsante)

    if pygame.key.get_pressed()[K_SPACE]:
        game_manager.current_phase = 1
        death, platforms, enemies, flag, shots = create_level()

    return player, enemies, death, platforms, shots, game_manager, flag