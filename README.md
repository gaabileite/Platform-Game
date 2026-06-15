# WeGlow: A Ascensão de Virgínia

**Disciplina:** Introdução à Programação (IP) - CIn/UFPE  

## 👥 Membros da Equipe

* **Beatriz Luna** — ([beatrizmdluna](https://github.com/beatrizmdluna))
* **Gabriel Geller** — ([gabrielgellercalou](https://github.com/gabrielgellercallou))
* **Gabriela Leite** — ([gaabileite](https://github.com/gaabileite))
* **Leonardo Kitner** — ([leonardokitner](https://github.com/leonardokitner))
* **Sâmia Freitas** — ([saamiafreitas](https://github.com/saamiafreitas))
* **Vivian Azevedo** — ([saamiafreitas](https://github.com/vivianazevedo))

---

## 🕹️ Sobre o Jogo

Desenvolvido em Python com a biblioteca Pygame, este é um jogo de plataforma 2D com mecânicas de coleta, combate e apostas, inspirado no universo da influenciadora Virginia Fonseca.

---

## 📜 História

Virgínia Fonseca tem um sonho: se tornar a maior magnata da internet. Para isso, ela precisa acumular 1 milhão de seguidores enfrentando rivais, desviando de haters e apostando seus seguidores no famoso Jogo do Tigrinho. O caminho passa por três fases — Rezende, Zé Felipe e Vini Jr — cada uma com seus próprios desafios e recompensas.

---

## 🎯 Objetivo

Controle a Vivíbora e acumule 1 milhão de seguidores para vencer. Colete seguidores, produtos WePink e Stories espalhados pelas fases, derrote Felcas e Haters no caminho e arrisque seus seguidores no Jogo do Tigrinho entre as fases — se tiver coragem.

---

## 🏗️ Arquitetura do Projeto

A estrutura do projeto separa claramente os recursos visuais da lógica do jogo:

```text
📂 Projeto
├──resources
|  ├──fonts
|  ├──spritesheets
|  |  ├──player
|  |  ├──enemy
|  |  └──collectables
|  ├──background
|  └──menu
├──classes
|  ├──gameobject.py
|  ├──movable.py
|  ├──player.py
|  ├──enemy.py
|  ├──shot.py
|  └──collectable.py
├──constants.py
└──main.py
```

---

## 📸 Galeria do Projeto

*a preencher*

---

## 🛠️ Ferramentas e Bibliotecas Utilizadas

| Ferramenta | Descrição |
|------------|-----------|
| **GitHub** | Repositório do projeto e controle de versão. |
| **Visual Studio Code** | Ambiente de desenvolvimento. |
| **Pygame** | Biblioteca para gerenciamento de gráficos, eventos e o *loop* do jogo. |
| **Piskel** | Criação dos *sprites* pixel art. |
| **Discord/WhatsApp** | Canais de comunicação interna da equipe. |
---

## 📋 Divisão de Trabalho

* **Vivian Azevedo — Front-End 1: Telas & Interface** — Menu principal, HUD (contador de seguidores, vidas e barra de ataque), interface do Jogo do Tigrinho, telas de vitória/derrota com textos personalizados e transições entre fases.

* **Sâmia Freitas — Front-End 2: Personagens & Animações** — *Sprite sheet* da protagonista (idle, run, jump, shoot), *sprites* dos inimigos Felca e Hater com animações de derrota, animações de coleta, dano e efeitos de tiro.

* **Beatriz Luna — Front-End 3: Cenários, Coletáveis & Identidade Visual** — *Backgrounds* das 3 fases (Rezende, Zé Felipe, Vini Jr), design de plataformas, *sprites* dos coletáveis (Seguidores, Produtos WePink, Stories) e guia de estilo visual (paleta e padrão pixel art).

* **Gabriela Leite — Back-End 1: Mecânicas do Jogador** — Movimentação, pulo, gravidade e colisão com plataformas; sistema de tiro e lógica da barra de ataque (efeitos por tipo de Produto WePink); gerenciamento de vidas.

* **Gabriel Geller — Back-End 2: Inimigos & Coletáveis** — IA do Felca (raio de visão, perseguição, roubo de seguidores e vida) e do Hater (perseguição direta); sistema de *spawn* com frequências (50%/30%/20%); efeitos dos coletáveis ao serem pegos e contador por fase.

* **Leonardo Kitner — Back-End 3: Fases, Tigrinho & Game Manager** — *Game loop* e controle de estados; gerenciador de fases (contadores de 25/35/60 coletáveis e transições); lógica do Jogo do Tigrinho (apostas variáveis por fase e resultado aleatório); condições de vitória (1M de seguidores) e derrota; *score* global.

---

## 📚 Conceitos da Disciplina Utilizados

* **Orientação a Objetos (POO):** Estrutura central do projeto, com hierarquia de classes (`GameObject` → `Movable` → `Player`/`Enemy`/`Shot`; `GameObject` → `Platform`/`Collectable`).
* **Herança:** `Player`, `Enemy` e `Shot` herdam de `Movable`, que herda de `GameObject`, reutilizando lógica de posição, física e colisão.
* **Listas:** Armazenam grupos de inimigos, coletáveis, plataformas e projéteis ativos por fase.
* **Estruturas Condicionais (If/Else):** Gerenciam estados do jogo (Menu, Fase, Tigrinho, Game Over, Vitória) e lógica de colisão e combate.
* **Laços de Repetição (While/For):** Mantêm o *game loop* ativo e iteram sobre grupos de objetos a cada *frame*.
* **Funções e Métodos:** Modularizam movimentação, física, renderização e detecção de colisão.
* **Aleatoriedade:** Controla o *spawn* de coletáveis com frequências definidas (50%/30%/20%) e o resultado das apostas no Jogo do Tigrinho.

---

## 💡 Desafios, Erros e Lições Aprendidas

*a preencher*

### Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?

*a preencher*

### Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?

*a preencher*

### Quais as lições aprendidas durante o projeto?

*a preencher*
