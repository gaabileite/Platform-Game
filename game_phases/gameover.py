import pygame
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
from game_manager import *
from game_phases.gamerunning import *

pygame.init()

bg_gameover = pygame.transform.smoothscale(pygame.image.load('assets/backgrounds/bg-gameover.png'), (320, 180))
btn_tryagain = pygame.transform.smoothscale(pygame.image.load('assets/backgrounds/btn-tentar-novamente.png'), (90, 90))

bg_gameover = pygame.transform.smoothscale(bg_gameover, (320, 180))
rect_tryagain = btn_tryagain.get_rect(center=(160, 128))

def gameover(surface, player, enemies, death, platforms, shots, game_manager, flag):

    surface.blit(bg_gameover, (0, 0))
    surface.blit(btn_tryagain, rect_tryagain)

    if pygame.key.get_pressed()[K_SPACE]:
        game_manager.current_phase = 1
        death, platforms, enemies, flag, shots = create_level(game_manager.current_phase)

    return player, enemies, death, platforms, shots, game_manager, flag
