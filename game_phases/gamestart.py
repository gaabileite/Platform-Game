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

# ── Carrega fora da função para não recarregar a cada frame ──
fundo         = pygame.transform.scale(pygame.image.load('bg-menu.png'), (320, 180))
botao_base    = pygame.transform.scale(pygame.image.load('botao1.png'), (87, 23))

def gamestart(surface, player, enemies, death, platforms, shots, game_manager, flag):

    # Fundo escalado para 320x180
    surface.blit(fundo, (0, 0))

    # Botão pulsante — coordenadas em 320x180
    escala = 1.0 + math.sin(pygame.time.get_ticks() * 0.005) * 0.08
    botao_pulsante = pygame.transform.scale(botao_base, (int(87 * escala), int(23 * escala)))
    rect_pulsante  = botao_pulsante.get_rect(center=(160, 128))  # ← centro da surface
    surface.blit(botao_pulsante, rect_pulsante)

    if pygame.key.get_pressed()[K_SPACE]:
        death, platforms, enemies, flag = create_level()
        shots = []
        game_manager.current_phase = 1

    return player, enemies, death, platforms, shots, game_manager, flag