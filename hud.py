import pygame

pygame.font.init()
font_hud   = pygame.font.SysFont("couriernew", 7, bold=True)
font_small = pygame.font.SysFont("couriernew", 6)

#desenhos
_icones_carregados = False
icone_seg   = None
icone_tiros = None
icone_vidas = None

def _carregar_icones():
    global _icones_carregados, icone_seg, icone_tiros, icone_vidas
    if _icones_carregados:
        return
    TAM = (8, 8)
    icone_seg   = pygame.transform.scale(pygame.image.load('icone_seguidores.png'), TAM)
    icone_tiros = pygame.transform.scale(pygame.image.load('icone_perfume.png'),    TAM)
    icone_vidas = pygame.transform.scale(pygame.image.load('icone_vida.png'),       TAM)
    _icones_carregados = True

def desenhar_hud(surface, player):
    _carregar_icones()  #carrega só na primeira vez que o HUD for chamado

    seguidores = getattr(player, 'follower_count', 0)
    meta       = getattr(player, 'phase_goal', 200)
    tiros      = getattr(player, 'attack_bar', 0)
    vidas      = getattr(player, 'life', 0)

    px, py = 4, 4
    pw, ph = 100, 60

    #Fundo semitransparente
    painel = pygame.Surface((pw, ph), pygame.SRCALPHA)
    painel.fill((0, 0, 0, 180))
    surface.blit(painel, (px, py))

    # bordinha branca + linha rosa
    pygame.draw.rect(surface, (255, 255, 255), (px, py, pw, ph), 1, border_radius=2)
    pygame.draw.line(surface, (255, 20, 147),
                     (px + 1, py + 3), (px + 1, py + ph - 3), 1)

    #titulo
    titulo = font_hud.render("WEGLOW", True, (255, 105, 180))
    surface.blit(titulo, (px + 5, py + 4))

    #seguidores
    surface.blit(icone_seg,  (px + 5,  py + 16))
    surface.blit(font_hud.render(f"{seguidores}", True, (255, 255, 255)), (px + 15, py + 16))

    #tiros
    surface.blit(icone_tiros, (px + 45, py + 16))
    surface.blit(font_hud.render(f"{tiros}", True, (255, 255, 255)), (px + 55, py + 16))

    #vidas
    surface.blit(icone_vidas, (px + 75, py + 16))
    surface.blit(font_hud.render(f"{vidas}", True, (255, 255, 255)), (px + 85, py + 16))

    #barra de progresso
    surface.blit(font_small.render("Meta", True, (255, 255, 255)), (px + 5, py + 44))
    barra_x, barra_y = px + 5, py + 52
    barra_w = pw - 10
    prog = min(seguidores / meta, 1.0) if meta > 0 else 0
    pygame.draw.rect(surface, (50, 50, 50),   (barra_x, barra_y, barra_w, 4))
    pygame.draw.rect(surface, (255, 20, 147), (barra_x, barra_y, int(barra_w * prog), 4))