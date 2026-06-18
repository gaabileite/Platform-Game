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
screen = pygame.display.set_mode((window_width, window_height))
surface = pygame.Surface((internal_width, internal_height))
clock = pygame.time.Clock()

camera = Camera(internal_width * scale)
game_over = GameOver(False)

player = Player(player_starter_x, player_starter_y)
enemies = [
    Enemy(300, 100 , hater_life)]
death = Platforms(0, 180, 320, 20)
platforms = [
    death,
    Platform(0, 160, 320, 20),
    Platform(100, 120, 80, 10),
    Platform(250, 100, 60 , 10)]
shots = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if not game_over.state:
        player.handle_movement()
        shot = player.shoot()
        if shot:
            shots.append(shot)
        camera.follow(player)
    
        player.update(surface, platforms)
                
        surface.fill(background_color)
        pygame.draw.rect(surface, player.color, camera.apply(player))
        
        for enemy in enemies:
            pygame.draw.rect(surface, enemy_color, camera.apply(enemy))
        for platform in platforms:
            pygame.draw.rect(surface, platform.color, camera.apply(platform))
        for shot in shots:
            pygame.draw.rect(surface, shot.color, camera.apply(shot))
    
        for shot in shots[:]:
            shot.move_bullet()
            if shot.x < 0 or shot.x > internal_width or shot.y < 0 or shot.y > internal_height:
                shots.remove(shot)

        enemy_dead = 0
        for enemy in enemies:
            if player.check_collision(enemy):
                player.life -= 1
            if player.life == 0:
                game_over.state = True
                break

            if shot:
                if shot.check_collision(enemy):
                    enemy.life -= 1
                if enemy.life == 0:
                    enemy_dead += 1

        for i in range(enemy_dead):
            _ = enemies.pop(i)

    else:
        player, enemies, death, platforms, shots = game_over.update(surface, player, enemies, death, platforms, shots)
    
    scaled = pygame.transform.scale(surface, (window_width, window_height))
    screen.blit(scaled, (0, 0))
    clock.tick(60)

    pygame.display.update()
