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

#imagens de fundo
fundo_gameover = pygame.transform.smoothscale(pygame.image.load('bg-gameover.png'), (320, 180))
btn_tentar     = pygame.transform.smoothscale(pygame.image.load('btn-tentar-novamente.png'), (90, 90))


# Escala o fundo para 960x540
fundo_gameover = pygame.transform.smoothscale(fundo_gameover, (320, 180))


rect_tentar = btn_tentar.get_rect(center=(160, 128))


def gameover(surface, player, enemies, death, platforms, shots, game_manager, flag):

    surface.blit(fundo_gameover, (0, 0))
    surface.blit(btn_tentar, rect_tentar)

    if pygame.key.get_pressed()[K_SPACE]:
        player = Player(player_starter_x, player_starter_y)
        enemies = [
            Enemy(300, 100)]
        death, platforms, enemies, flag = create_level()
        shots = []
        game_manager.current_phase = 1

    return player, enemies, death, platforms, shots, game_manager, flag
