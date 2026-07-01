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
    1 : pygame.transform.scale(pygame.image.load('assets/backgrounds/bg-transicao1.png'), (320, 180)),
    2 : pygame.transform.scale(pygame.image.load('assets/backgrounds/bg-transicao2.png'), (320, 180))
}
btn_keepgoing = pygame.transform.scale(pygame.image.load('---.png'), (87, 23))

def phase_transition(surface, player, enemies, death, platforms, collectables, shots, game_manager, flag, last_phase):
    surface.blit(bg_transition[last_phase], (0, 0))

    if pygame.key.get_pressed()[K_SPACE] and last_phase == 1:
        game_manager.current_phase = 2
        death, platforms, enemies, collectables_data, flag = create_level(2)
        collectables = make_collectables(collectables_data)
        shots = []

    if pygame.key.get_pressed()[K_SPACE] and last_phase == 2:
        game_manager.current_phase = 3
        death, platforms, enemies, collectables_data, flag = create_level(3)
        collectables = make_collectables(collectables_data)
        shots = []

    return player, enemies, death, platforms, collectables, shots, game_manager, flag