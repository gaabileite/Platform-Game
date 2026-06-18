import pygame
from pygame.locals import *
from sys import exit
import random
import math
from classes.gameobject import *
from classes.movable import *
from classes.player import *
from classes.enemy import *
from classes.shot import *
from classes.platform import *
from classes.collectable import *
from classes.camera import *
from constants import *

pygame.init()

font_title = pygame.font.Font(None, 28)
font_subtitle = pygame.font.Font(None, 24)

class GameOver:
    def __init__(self, state):
        self.state = state

    def update(self):
        surface.fill(game_over_bg)

        title_text = font_title.render("GAME OVER", True, background_color)
        surface.blit(title_text, title_text.get_rect(center=(internal_width // 2, internal_height // 2 - 15)))

        subtitle_text = font_subtitle.render("Press SPACE to reset", True, player_color)
        surface.blit(subtitle_text, subtitle_text.get_rect(center=(internal_width // 2, internal_height // 2 + 15)))

        if pygame.keys.get_pressed()[K_SPACE]:
            player = Player(player_starter_x, player_starter_y)
            enemies = [
                Enemy(300, 100 , hater_life)]
            death = Platform(0, 180, 320, 20)
            platforms = [
                death,
                Platform(0, 160, 320, 20),
                Platform(100, 120, 80, 10),
                Platform(250, 100, 60 , 10)]
            shots = []
            self.state = False
            return player, enemies, death, platforms, shots
