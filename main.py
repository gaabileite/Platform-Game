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
from classes.game_manager import *
from classes.platform import *
from classes.collectable import *
from classes.camera import *
from constants import *

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
surface = pygame.Surface((internal_width, internal_height))
clock = pygame.time.Clock()

camera = Camera(internal_width * scale)

player = Player(player_starter_x, player_starter_y)
game_manager = GameManager()
font = pygame.font.Font(None, 24)
enemy = Enemy(300, 100 , hater_life)
platforms = [
    Platform(0, 160, 320, 20),
    Platform(100, 120, 80, 10),
    Platform(250, 100, 60 , 10)]
shots = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                game_manager.continue_game()

    if game_manager.state == 'playing':
            player.handle_movement()

            shot = player.shoot()
            if shot:
                shots.append(shot)

            camera.follow(player)
            player.update(surface, platforms)

            game_manager.check_progress(player)
            game_manager.check_defeat(player)

            surface.fill(background_color)

            pygame.draw.rect(surface, player.color, camera.apply(player))
            pygame.draw.rect(surface, enemy_color, camera.apply(enemy))

            for platform in platforms:
                pygame.draw.rect(
                    surface,
                    platform.color,
                    camera.apply(platform)
                )

            for shot in shots[:]:
                shot.move_bullet()

                if shot.x < 0 or shot.x > internal_width or shot.y < 0 or shot.y > internal_height:
                    shots.remove(shot)

            for shot in shots:
                pygame.draw.rect(
                    surface,
                    shot.color,
                    camera.apply(shot)
                )
    player.handle_movement()
    shot = player.shoot()
    if shot:
        shots.append(shot)
    camera.follow(player)

    player.update(surface, platforms)
            
    surface.fill(background_color)
    pygame.draw.rect(surface, player.color, camera.apply(player))
    pygame.draw.rect(surface, enemy_color, camera.apply(enemy))

    for platform in platforms:
        pygame.draw.rect(surface, platform.color, camera.apply(platform))
    for shot in shots:
        pygame.draw.rect(surface, shot.color, camera.apply(shot))

    for shot in shots[:]:
        shot.move_bullet()
        if shot.x < 0 or shot.x > internal_width or shot.y < 0 or shot.y > internal_height:
            shots.remove(shot)

    scaled = pygame.transform.scale(surface, (window_width, window_height))
    screen.blit(scaled, (0, 0))
    clock.tick(60)

    pygame.display.update()
