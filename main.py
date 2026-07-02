import pygame
from pygame.locals import *
from sys import exit
from constants import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('assets/sounds/bg_sound.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((window_width, window_height))
surface = pygame.Surface((internal_width, internal_height))
pygame.display.set_caption("WEGLOW: A Ascensão de Virgínia")
clock = pygame.time.Clock()

from classes.gameobject import *
from classes.movable import *
from classes.player import *
from classes.enemy import *
from classes.shot import *
from game_manager import *
from classes.platform import *
from classes.collectable import *
from classes.camera import *
from level import *
from game_phases.gamerunning import *
from game_phases.gameover import *
from game_phases.gamestart import *
from game_phases.gamewon import *
from hud import desenhar_hud
from game_phases.transition import *
from sprites import *

game_manager = GameManager()
player = Player(player_starter_x, player_starter_y, ANIMATIONS_V)
death, platforms, enemies, flag, coletaveis, shots, camera = create_level(game_manager.current_phase)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if game_manager.current_phase == 0:
        player, death, platforms, enemies, flag, coletaveis, shots, camera, game_manager = gamestart(surface, player, enemies, death, platforms, shots, game_manager, flag, camera)

    elif game_manager.current_phase in [1,2,3]:
        game_manager, last_phase = game_running(player, enemies, death, platforms, shots, camera, surface, game_manager, flag[game_manager.current_phase], coletaveis)

    elif game_manager.current_phase == 4:
        player, death, platforms, enemies, flag, coletaveis, shots, camera, game_manager = phase_transition(surface, player, enemies, death, platforms, shots, game_manager, flag, last_phase, camera)

    elif game_manager.current_phase == 5:
        player, death, platforms, enemies, flag, coletaveis, shots, camera, game_manager = gameover(surface, player, enemies, death, platforms, shots, game_manager, flag, camera)
    
    elif game_manager.current_phase == 6:
        player, death, platforms, enemies, flag, coletaveis, shots, camera, game_manager = gamewon(surface, player, enemies, death, platforms, shots, game_manager, flag, camera)

    screen.blit(surface, (0, 0))
    clock.tick(40)

    pygame.display.update()
