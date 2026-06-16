import pygame 
import math
from classes import enemy
from classes import player
from constants import *

pygame.init() 
fonte = pygame.font.SysFont("Arial", 40)
fonte_pequena = pygame.font.SysFont("Arial", 20)
tela = pygame.display.set_mode((window_width , window_height))
clock = pygame.time.Clock()
tam = 20
game_over = False
rodando = True
tela_inicial = True
jogador_x, jogador_y = 100, 100
inimigo_x, inimigo_y = 300, 300
espaco =fonte_pequena.render("Pressione ESPACO para continuar", True, (255, 255, 0))

alcance = 200
player_speed = 5


def reiniciar():
    return 100,100,300,300,0,40

while rodando:
   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and game_over:
                jogador_x,jogador_y,inimigo_x,inimigo_y,qtd_moedas,tamanho = reiniciar()
                game_over = False 
    
    tecla = pygame.key.get_pressed()

    if not game_over:  
        if tecla[pygame.K_LEFT]  and jogador_x > 0:          jogador_x -= player_speed
        if tecla[pygame.K_RIGHT] and jogador_x < window_width - tam:  jogador_x += player_speed
        if tecla[pygame.K_UP]    and jogador_y > 0:          jogador_y -= player_speed
        if tecla[pygame.K_DOWN]  and jogador_y < window_height - tam:  jogador_y += player_speed

    player_rect = pygame.Rect(jogador_x, jogador_y, tam, tam)
    enemy_rect = pygame.Rect(inimigo_x, inimigo_y, tam, tam)

    if player_rect.colliderect(enemy_rect):
        game_over = True
    distancia = math.sqrt((inimigo_x - jogador_x) ** 2 + (inimigo_y - jogador_y) ** 2)
    if distancia < alcance and not game_over:
        if inimigo_x < jogador_x: inimigo_x += 2
        if inimigo_x > jogador_x: inimigo_x -= 2
        if inimigo_y < jogador_y: inimigo_y += 2
        if inimigo_y > jogador_y: inimigo_y -= 2
    tela.fill((0, 0, 0))            
    if game_over:
        texto  = fonte.render("GAME OVER!!!", True, (250, 250, 0))
        tela.blit(texto,  (250, 250))
        tela.blit(espaco, (250, 320))
    else:
        pygame.draw.rect(tela, (255, 0, 127), player_rect)
        pygame.draw.rect(tela, (255, 0, 0), enemy_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
