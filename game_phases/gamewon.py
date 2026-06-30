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
from game_phases.gamerunning import *

pygame.init()

#imagens de fundo e botão
fundo_vitoria  = pygame.transform.scale(pygame.image.load('bg_gamewin.png'), (320, 180))
btn_jogar      = pygame.transform.scale(pygame.image.load('btn-tentar-novamente.png'), (90, 90))


fundo_vitoria = pygame.transform.scale(fundo_vitoria, (960, 540))

#botao
rect_jogar = btn_jogar.get_rect(center=(480, 340))


def gamewon(surface, player, enemies, death, platforms, shots, game_manager, flag):
    surface.blit(fundo_vitoria, (0, 0))
    surface.blit(btn_jogar, rect_jogar)
    

    if pygame.key.get_pressed()[K_SPACE]:
        player = Player(player_starter_x, player_starter_y)
        enemies = [
            Enemy(300, 100)]
        death, platforms, enemies, flag = create_level()
        shots = []
        game_manager.current_phase = 2

    return player, enemies, death, platforms, shots, game_manager, flag
