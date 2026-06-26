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
font_title = pygame.font.SysFont(None, 24)
font_subtitle = pygame.font.SysFont(None, 22)

def gamestart(surface, player, enemies, death, platforms, shots, game_manager, flag):
    surface.fill((0,0,0))

    title_text = font_title.render("WEGLOW: A Ascensão de Virgínia", True, background_color)
    surface.blit(title_text, title_text.get_rect(center=(internal_width // 2, internal_height // 2 - 15)))

    subtitle_text = font_subtitle.render("Pressione ESPAÇO para começar!", True, player_color)
    surface.blit(subtitle_text, subtitle_text.get_rect(center=(internal_width // 2, internal_height // 2 + 15)))

    if pygame.key.get_pressed()[K_SPACE]:
        death, platforms, enemies, flag = create_level()
        shots = []
        game_manager.current_phase = 1

    return player, enemies, death, platforms, shots, game_manager, flag
