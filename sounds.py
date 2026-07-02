import pygame

pygame.mixer.init()

SONS = {
    'follower': pygame.mixer.Sound('assets/sounds/follower.ogg'),
    'shot':     pygame.mixer.Sound('assets/sounds/shot.ogg'),
}
SONS['follower'].set_volume(0.6)
SONS['shot'].set_volume(0.5)

def tocar(nome):
    SONS[nome].play()