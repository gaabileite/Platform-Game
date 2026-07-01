import pygame
from constants import *
from classes.gameobject import *

def build_tiled(image, width, height):
    tile = pygame.transform.scale(image, (height, height))
    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    for tx in range(0, width, height):
        surf.blit(tile, (tx, 0))
    return surf

class Platform(GameObject):
    def __init__(self, x, y, width, height, image):
        tiled = build_tiled(image, width, height)
        super().__init__(x, y, tiled, width, height)