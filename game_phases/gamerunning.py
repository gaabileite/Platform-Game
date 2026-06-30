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

backgrounds = {
    1 : pygame.transform.smoothscale(pygame.image.load('assets/backgrounds/bg-phase1.png'), (320, 180)),
    2 : pygame.transform.smoothscale(pygame.image.load('assets/backgrounds/bg-phase2.png'), (320, 180)),
    3 : pygame.transform.smoothscale(pygame.image.load('assets/backgrounds/bg-phase3.png'), (320, 180))
}

def game_running(player, enemies, death, platforms, shots, camera, surface, game_manager, flag):
    last_phase = game_manager.current_phase

    player.handle_movement()
    shot = player.shoot()
    if shot:
        shots.append(shot)
    camera.follow(player)

    player.update(platforms)
    for enemy in enemies:
        enemy.update(platforms, player)

    # --- mover os tiros e remover os que saíram da tela ---
    for shot in shots[:]:
        shot.move_bullet()
        if shot.x < 0 or shot.x > internal_width or shot.y < 0 or shot.y > internal_height:
            shots.remove(shot)

    # --- desenho ---
    surface.fill(background_color)
    surface.blit(backgrounds[game_manager.current_phase], (0,0))
    surface.blit(player.image, camera.apply(player))

    for enemy in enemies:
        surface.blit(enemy.image, camera.apply(enemy))
    for platform in platforms:
        surface.blit(platform.image, camera.apply(platform))
    surface.blit(flag.image, camera.apply(flag))
    for shot in shots:
        surface.blit(shot.image, camera.apply(shot))

    # --- colisões com inimigos (jogador toma dano + tiros acertam) ---
    enemy_dead = []
    shots_used = []
    for enemy in enemies:
        if player.check_collision(enemy):
            player.life -= 1

        for shot in shots:
            if shot.check_collision(enemy):
                enemy.life -= 1
                enemy.image = SPRITES['felca_dano']
                shots_used.append(shot)

        if enemy.life <= 0:
            enemy_dead.append(enemy)

    if player.life <= 0:
        game_manager.current_phase = 6
        return game_manager, last_phase

    # --- remover inimigos mortos e tiros já usados ---
    for enemy in enemy_dead:
        if enemy in enemies:
            enemies.remove(enemy)
    for shot in shots_used:
        if shot in shots:
            shots.remove(shot)

    # --- bandeira / progresso de fase ---
    if player.check_collision(flag) and game_manager.current_phase in [1, 2]:
        game_manager.current_phase = 4
        return game_manager, last_phase

    elif player.check_collision(flag):
        game_manager.check_progress()

    # --- morte por queda ou por zona de morte ---
    if player.check_collision(death) or player.y > internal_height:
        game_manager.current_phase = 6
        return game_manager, last_phase

    return game_manager, last_phase