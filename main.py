import pygame
from pygame.locals import *
from sys import exit
import random
from classes.gameobject import *
from classes.movable import *
from classes.player import *
from classes.enemy import *
from classes.shot import *
from classes.platform import *
from classes.collectable import *
from constants import *

pygame.init()
screen = pygame.display.set_mode((internal_width, internal_height))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()