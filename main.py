import pygame
from pygame.locals import *
from sys import exit
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
from phases.game_running import *
from phases.game_over import *
from phases.game_start import *
from phases.game_won import *

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
surface = pygame.Surface((internal_width, internal_height))
pygame.display.set_caption("WEGLOW: A Ascensão de Virgínia")
clock = pygame.time.Clock()

camera = Camera(LEVEL_WIDTH)
player = Player(player_starter_x, player_starter_y)
enemies = [
    Enemy(300, 100)]
death, platforms, enemies, flag = create_level()
shots = []

state = 'game-start'

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if state == 'game-running':
        state = game_running(player, enemies, death, platforms, shots, camera, surface, state, flag)

    elif state == 'game-over':
        player, enemies, death, platforms, shots, state, flag = gameover(surface, player, enemies, death, platforms, shots, state, flag)
    
    elif state == 'game-start':
        player, enemies, death, platforms, shots, state, flag = gamestart(surface, player, enemies, death, platforms, shots, state, flag)

    elif state == 'game-won':
        player, enemies, death, platforms, shots, state, flag = gamewon(surface, player, enemies, death, platforms, shots, state, flag)

    # SCREEN UPDATE 
    scaled = pygame.transform.scale(surface, (window_width, window_height))
    screen.blit(scaled, (0, 0))
    clock.tick(60)

    pygame.display.update()
