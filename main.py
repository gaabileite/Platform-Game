import pygame
from pygame.locals import *
from sys import exit
from classes.gameobject import *
from classes.movable import *
from classes.player import *
from classes.enemy import *
from classes.shot import *
from game_manager import *
from classes.platform import *
from classes.collectable import *
from classes.camera import *
from constants import *
from level import *
from game_phases.gamerunning import *
from game_phases.gameover import *
from game_phases.gamestart import *
from game_phases.gamewon import *
from hud import desenhar_hud
from game_phases.transition import *
from sprites import *

#Definições iniciais padrão do Pygame e criação da janela
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
surface = pygame.Surface((internal_width, internal_height))
pygame.display.set_caption("WEGLOW: A Ascensão de Virgínia")
clock = pygame.time.Clock()

#Instanciação do GameManager e criação dos objetos do jogo
game_manager = GameManager()
camera = Camera(LEVEL_WIDTH)
player = Player(player_starter_x, player_starter_y, ANIMATIONS_V)
death, platforms, enemies, flag = create_level()
shots = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #GAME START (OK)
    if game_manager.current_phase == 0:
        player, enemies, death, platforms, shots, game_manager, flag, shots = gamestart(surface, player, enemies, death, platforms, shots, game_manager, flag)

    #GAME RUNNING: PHASE 1, 2, 3 (WIP/BACK)
    elif game_manager.current_phase in [1,2,3]:
        game_manager, last_phase = game_running(player, enemies, death, platforms, shots, camera, surface, game_manager, flag)

    #PHASE TRANSITION (WIP/FRONT)
    elif game_manager.current_phase == 4:
        player, enemies, death, platforms, shots, game_manager, flag, shots = phase_transition(surface, player, enemies, death, platforms, shots, game_manager, flag, last_phase)

    #GAME OVER (OK)
    elif game_manager.current_phase == 5:
        player, enemies, death, platforms, shots, game_manager, flag, shots = gameover(surface, player, enemies, death, platforms, shots, game_manager, flag)
    
    #GAME WON (OK)
    elif game_manager.current_phase == 6:
        player, enemies, death, platforms, shots, game_manager, flag = gamewon(surface, player, enemies, death, platforms, shots, game_manager, flag)

    #SCREEN UPDATE 
    scaled = pygame.transform.scale(surface, (window_width, window_height))
    screen.blit(scaled, (0, 0))
    clock.tick(60)

    pygame.display.update()
