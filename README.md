# WeGlow: A Ascensão de Virgínia

**Disciplina:** Introdução à Programação (IP) - CIn/UFPE  

## 👥 Membros da Equipe

* **Beatriz Luna** — ([beatrizmdluna](https://github.com/beatrizmdluna))
* **Gabriel Geller** — ([gabrielgellercalou](https://github.com/gabrielgellercallou))
* **Gabriela Leite** — ([gaabileite](https://github.com/gaabileite))
* **Leonardo Kitner** — ([leonardokitner](https://github.com/leonardokitner))
* **Sâmia Freitas** — ([saamiafreitas](https://github.com/saamiafreitas))
* **Vivian Azevedo** — ([vivianazevedo](https://github.com/vivianazevedo))

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

* **Beatriz Luna — Front-End 2: Personagens & Animações** — *Sprite sheet* da protagonista (idle, run, jump, shoot), *sprites* dos inimigos Felca e Hater com animações de derrota, animações de coleta, dano e efeitos de tiro.

* **Sâmia Freitas — Front-End 3: Cenários, Coletáveis & Identidade Visual** — *Backgrounds* das 3 fases (Rezende, Zé Felipe, Vini Jr), design de plataformas, *sprites* dos coletáveis (Seguidores, Produtos WePink, Stories) e guia de estilo visual (paleta e padrão pixel art).

* **Gabriela Leite — Back-End 1: Mecânicas do Jogador** — Movimentação, pulo, gravidade e colisão com plataformas; sistema de tiro e lógica da barra de ataque (efeitos por tipo de Produto WePink); gerenciamento de vidas.

* **Gabriel Geller — Back-End 2: Inimigos & Coletáveis** — IA do Felca (raio de visão, perseguição, roubo de seguidores e vida) e do Hater (perseguição direta); sistema de *spawn* com frequências (50%/30%/20%); efeitos dos coletáveis ao serem pegos e contador por fase.

* **Leonardo Kitner — Back-End 3: Fases, Tigrinho & Game Manager** — *Game loop* e controle de estados; gerenciador de fases (contadores de 25/35/60 coletáveis e transições); condições de vitória (1M de seguidores) e derrota; *score* global.

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

### Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?

O maior erro foi a falta de integração e comunicação entre os integrantes da equipe. Por estarmos todos passando por um período de adaptação ao primeiro período da faculdade e conciliando diferentes responsabilidades, em alguns momentos a comunicação acabou falhando, o que dificultou o alinhamento das tarefas e o acompanhamento do andamento do projeto. Para resolver essa situação, passamos a utilizar o Discord de forma mais organizada, realizamos reuniões com maior frequência e mantivemos um contato mais constante entre os membros da equipe. Além disso, buscamos apoio dos monitores, mantendo-os informados sobre o progresso do jogo e tirando dúvidas sempre que necessário, o que contribuiu para colocar o projeto novamente no caminho certo.

### Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?

O maior desafio, sem dúvidas, foi evitar o acúmulo de tarefas e manter um ritmo constante de desenvolvimento. Nossa equipe tinha uma proposta bastante criativa, que recebeu muitos elogios da monitoria, o que aumentou ainda mais as expectativas em relação ao resultado final. No entanto, percebemos que boas ideias, por si só, não garantem um bom projeto. Foi necessário que cada integrante assumisse suas responsabilidades e entregasse suas atividades de forma gradual, evitando deixar tudo para os últimos dias. Com mais organização e divisão das tarefas, conseguimos avançar no desenvolvimento sem comprometer a qualidade do jogo.

### Quais as lições aprendidas durante o projeto?

A principal lição aprendida foi que a colaboração é indispensável em projetos de tecnologia. Um trabalho da dimensão deste projeto só se torna possível quando todos os integrantes contribuem de forma equilibrada e mantêm uma comunicação clara e constante. Além dos conhecimentos técnicos adquiridos, aprendemos a importância do planejamento, da organização e do comprometimento individual para que o trabalho em equipe funcione. Essa experiência mostrou que o sucesso de um projeto depende tanto da qualidade da ideia quanto da capacidade do grupo de trabalhar em conjunto para transformá-la em realidade. 
