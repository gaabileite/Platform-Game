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

#WIP(FRONT)
bg_transition = {
    1 : pygame.transform.scale(pygame.image.load('assets/backgrounds/bg_transicao1.png'), (320, 180)),
    2 : pygame.transform.scale(pygame.image.load('assets/backgrounds/bg_transicao2.png'), (320, 180))
}
btn_keepgoing = pygame.transform.scale(pygame.image.load('assets/backgrounds/btn-jogar.png'), (87, 23))

def phase_transition(surface, player, enemies, death, platforms, shots, game_manager, flag, last_phase, camera):
    surface.blit(bg_transition[last_phase], (0, 0))

    if pygame.key.get_pressed()[K_SPACE] and last_phase == 1:
        game_manager.current_phase = 2
        death, platforms, enemies, flag, shots, camera = create_level(game_manager.current_phase)

    if pygame.key.get_pressed()[K_SPACE] and last_phase == 2:
        game_manager.current_phase = 3
        death, platforms, enemies, flag, shots, camera = create_level(game_manager.current_phase)

    return player, enemies, death, platforms, shots, game_manager, flag, camera