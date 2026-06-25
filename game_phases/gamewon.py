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
pygame.init()
font_title = pygame.font.SysFont(None, 24)
font_subtitle = pygame.font.SysFont(None, 22)

def gamewon(surface, player, enemies, death, platforms, shots, state, flag):
    surface.fill((0,0,0))
    title_text = font_title.render("PARABÉNS! VOCÊ VENCEU!", True, background_color)
    surface.blit(title_text, title_text.get_rect(center=(internal_width // 2, internal_height // 2 - 15)))

    subtitle_text = font_subtitle.render("Pressione ESPAÇO para reiniciar...", True, player_color)
    surface.blit(subtitle_text, subtitle_text.get_rect(center=(internal_width // 2, internal_height // 2 + 15)))

    if pygame.key.get_pressed()[K_SPACE]:
        player = Player(player_starter_x, player_starter_y)
        enemies = [
            Enemy(300, 100)]
        death, platforms, enemies, flag = create_level()
        shots = []
        state = 'game-running'

    return player, enemies, death, platforms, shots, state, flag
