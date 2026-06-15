import pygame 
import random
pygame.init() 
x , y = 800 , 600
moeda_x = random.randint(50,750)
moeda_y = random.randint(50,550)
tam = 40
tela = pygame.display.set_mode((800 , 600))
clock = pygame.time.Clock()
fonte = pygame.font.SysFont('comicsansms', 44)
fonte_moedas = pygame.font.SysFont(None, 25)
jogador_x = 100
jogador_y = 100
qtd_moedas = 0
inimigo_x  = 300
inimigo2_x  = 300
inimigo_y2 = random.randint(50,550)
inimigo_y  = random.randint(50,550)
game_over = False
vel_jogador = 7
vel_inimigo = 10
vel_inimigo2 = 20
rodando = True
tamanho = 40 
tela_inicial = True
def reiniciar():
    return 100,100,300,300,0,40

espaco = fonte_moedas.render("Pressione ESPACO para continuar", True, (255, 255, 0))
while rodando:
   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and game_over:
                jogador_x,jogador_y,inimigo_x,inimigo_y,qtd_moedas,tamanho = reiniciar()
                game_over = False 
    tecla = pygame.key.get_pressed()
    if tela_inicial :
        tela.fill((0,0,0))
        capa = fonte.render("WE GLOW! BY VIRGINIA FONSECA", True,(255,255,255))
        tela.blit(espaco,(250, 320))
        tela.blit(capa,(20,250))
        pygame.display.flip()
        if tecla[pygame.K_SPACE]:
            tela_inicial = False
    else:        
        if not game_over:  
            if tecla[pygame.K_LEFT]  and jogador_x > 0:          jogador_x -= vel_jogador
            if tecla[pygame.K_RIGHT] and jogador_x < 800 - tam:  jogador_x += vel_jogador
            if tecla[pygame.K_UP]    and jogador_y > 0:          jogador_y -= vel_jogador
            if tecla[pygame.K_DOWN]  and jogador_y < 600 - tam:  jogador_y += vel_jogador

            inimigo_x += vel_inimigo
            if inimigo_x > 800 + tamanho:
                inimigo_x = -tamanho
            inimigo2_x -= vel_inimigo2
            if inimigo2_x < 0:
                inimigo2_x = 800 + tamanho
            jogador_rect = pygame.Rect(jogador_x, jogador_y, tamanho, tamanho)
            inimigo_rect = pygame.Rect(inimigo_x, inimigo_y, 60, 60)
            coins_rect   = pygame.Rect(moeda_x, moeda_y, 20, 20)
            inimigo2_rect = pygame.Rect(inimigo2_x,inimigo_y2, 25,25)
            if jogador_rect.colliderect(inimigo_rect):
                game_over = True  
            if jogador_rect.colliderect(inimigo2_rect):
                game_over = True  

            if jogador_rect.colliderect(coins_rect):
                qtd_moedas += 1
                tamanho += 2
                moeda_x = random.randint(50, 750)
                moeda_y = random.randint(50, 550)

        tela.fill((0, 0, 0))            

        if game_over:
            texto  = fonte.render("GAME OVER!!!", True, (250, 250, 0))
            tela.blit(texto,  (250, 250))
            tela.blit(espaco, (250, 320))
            if qtd_moedas < 10 :
                humilhacao = fonte_moedas.render("caralho, tu é ruim viu porra!! menos de 10 moedas é foda",True,(255,0,255))
                tela.blit(humilhacao,(200,50))
        else:
            pygame.draw.rect(tela, (200, 0, 255), jogador_rect)
            pygame.draw.rect(tela, (255, 0, 0),   inimigo_rect)
            pygame.draw.rect(tela, (255, 0, 0),   inimigo2_rect)
            pygame.draw.rect(tela, (255, 255, 0),  coins_rect)

        texto_topo = fonte_moedas.render(f"QUANTIDADE DE MOEDAS: {qtd_moedas}", True, (255, 255, 255))
        tela.blit(texto_topo, (1, 575))
        if qtd_moedas == 20 :
            parabens = fonte_moedas.render("TU E PIKA PORRAA!!! ta na hora de aumentar a dificauldade",True,(0,255,255))
            tela.blit(parabens,(300,50))
            pygame.display.flip()
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
