import pygame
import math

pygame.init()

window = pygame.display.set_mode((320 *3, 180*3))
pygame.display.set_caption("STAR WEGLOW")

fundo = pygame.image.load('bg-menu.png')
botao_original = pygame.image.load('botao1.png')
botao = pygame.transform.scale(botao_original, (320, 80))

clock = pygame.time.Clock()
loop  = True



while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("iniciar jogo!")  #aqui inicia o jogo (entender como vou enxaicar isso)

    # Fundo
    window.blit(fundo, (0, 0))


   # --- SINAL DO PULSO ---
    escala = 1.0 + math.sin(pygame.time.get_ticks() * 0.005) * 0.08

    # Cria uma versão temporária da imagem esticada de acordo com o pulso (tamanho base 260x70)
    botao_pulsante = pygame.transform.scale(botao, (int(260 * escala), int(70 * escala)))
    
    # Define o centro fixo para a imagem expandir perfeita a partir do meio
    rect_pulsante = botao_pulsante.get_rect(center=(480, 385))

    # Desenha a imagem pulsando
    window.blit(botao_pulsante, rect_pulsante)

    pygame.display.update()
    clock.tick(60)

pygame.quit()