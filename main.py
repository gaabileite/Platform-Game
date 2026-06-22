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

# Definições iniciais padrão do Pygame e criação da janela
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
surface = pygame.Surface((internal_width, internal_height))
pygame.display.set_caption("WEGLOW: A Ascensão de Virgínia")
clock = pygame.time.Clock()

# Instanciação do GameManager e criação dos objetos do jogo
game_manager = GameManager()
camera = Camera(LEVEL_WIDTH)
player = Player(player_starter_x, player_starter_y)
death, platforms, enemies, flag = create_level()
shots = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                game_manager.continue_game()

    # Verificação de progresso do jogador para transição entre fases
    game_manager.check_progress(player)

    # GAME START
    if game_manager.current_phase == 0:
        player, enemies, death, platforms, shots, state, flag = gamestart(surface, player, enemies, death, platforms, shots, state, flag)

    # GAME RUNNING: PHASE 1
    elif game_manager.current_phase == 1:
        state = game_running(player, enemies, death, platforms, shots, camera, surface, state, flag)

    # GAME OVER
    elif game_manager.current_phase == 4:
        player, enemies, death, platforms, shots, state, flag = gameover(surface, player, enemies, death, platforms, shots, state, flag)
    
    # GAME WON
    elif game_manager.current_phase == 6:
        player, enemies, death, platforms, shots, state, flag = gamewon(surface, player, enemies, death, platforms, shots, state, flag)

    # SCREEN UPDATE 
    scaled = pygame.transform.scale(surface, (window_width, window_height))
    screen.blit(scaled, (0, 0))
    clock.tick(60)

    pygame.display.update()
