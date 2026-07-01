import pygame
from pygame.locals import *
from constants import *

pygame.init()

class GameObject:
    def __init__(self, x, y, image, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(image, (width, height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
