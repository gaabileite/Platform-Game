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

def game_running(player, enemies, death, platforms, shots, camera, surface, game_manager, flag):
    player.handle_movement()
    ###shot = player.shoot()
    ###if shot:
    ###    shots.append(shot)
    camera.follow(player)

    player.update(platforms)
    for enemy in enemies:
        enemy.update(platforms, player)
        ###for shot in shots:
        ###    enemy.get_shot(shot)
            
    surface.fill(background_color)
    pygame.draw.rect(surface, player.color, camera.apply(player))

    for enemy in enemies:
        pygame.draw.rect(surface, enemy_color, camera.apply(enemy))
    for platform in platforms:
        pygame.draw.rect(surface, platform.color, camera.apply(platform))
    pygame.draw.rect(surface, flag.color, camera.apply(flag))
    ###for shot in shots:
    ###    pygame.draw.rect(surface, shot.color, camera.apply(shot))

    ###for shot in shots[:]:
    ###    shot.move_bullet()
    ###    if shot.x < 0 or shot.x > internal_width or shot.y < 0 or shot.y > internal_height:
    ###        shots.remove(shot)

    enemy_dead = []
    for enemy in enemies:
        if player.check_collision(enemy):
            player.life -= 1
        if player.life <= 0:
            game_manager.current_phase = 6
            break

    if player.check_collision(flag):
        game_manager.current_phase = 7

        ###for shot in shots:
        ###    if shot.check_collision(enemy):
        ###        enemy.life -= 1
        ###if enemy.life <= 0:
        ###    enemy_dead.append(enemies.index(enemy))

    for enemy in enemy_dead:
        enemies.remove(enemy)

    if player.check_collision(death) or player.y > internal_height:
        game_manager.current_phase = 6

    return game_manager
