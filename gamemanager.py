from enum import Enum
from classes.player import *
from classes.tigrinho import *
from constants import *

class GameState(Enum):
    MENU = 0
    PHASE_1 = 1
    TIGRINHO_1 = 2
    PHASE_2 = 3
    TIGRINHO_2 = 4
    PHASE_3 = 5
    TIGRINHO_3 = 6
    WIN = 7
    LOSE = 8

class GameManager:
    COLLECTABLE_LIMITS = {1 : 25, 2 : 35, 3 : 60}
    COLLECTABLE_GOAL = 100

    def __init__(self):
        self.state = GameState.MENU
        self.phase_number = 1
        self.tigrinho = None
        self.tigrinho_number = None
        self.player = Player(player_starter_x, player_starter_y)
        self.platforms = []
        self.enemies = []
        self.collectables = []
        self.collectable_count = 0

    def change_state(self, new_state):
        self.state = new_state
        self.enter_phase()

    def check_phase_end(self):
        limit = self.COLLECTABLE_LIMITS[self.phase_number]
        if self.collectable_count >= limit:
            next_tigrinho = [GameState.TIGRINHO_1,
                             GameState.TIGRINHO_2,
                             GameState.TIGRINHO_3]
            self.change_state(next_tigrinho[self.phase_number - 1])

    def check_game_over(self):
        if self.player.life <= 0 or self.player.follower_count <= 0:
            self.change_state(GameState.LOSE)

    def check_win(self):
        if self.collectable_count >= self.COLLECTABLE_GOAL:
            self.change_state(GameState.WIN)

    def enter_phase(self):
        if self.state in (GameState.PHASE_1, GameState.PHASE_2, GameState.PHASE_3):
            self.setup_phase()
        elif self.state in (GameState.TIGRINHO_1, GameState.TIGRINHO_2, GameState.TIGRINHO_3):
            self.setup_tigrinho()

    def setup_phase(self):
        self.collectable_count = 0
        self.enemies      = []
        self.collectables = []
        self.platforms    = []

    def setup_tigrinho(self):
        self.tigrinho = TigrinhoGame(self.phase_number, self.player)

    def update(self):
        if self.state in (GameState.PHASE_1, GameState.PHASE_2, GameState.PHASE_3):
            self.player.update(self.platforms)
            self.player.handle_movement()

            for enemy in self.enemies:
                enemy.update(self.platforms)
                enemy.follow_player(self.player)

            self.check_phase_end()
            self.check_game_over()
            self.check_win()

        elif self.state in (GameState.TIGRINHO_1, GameState.TIGRINHO_2, GameState.TIGRINHO_3):
            if self.tigrinho.state == 'result':
                resultado = self.tigrinho.resolve()

                if resultado == 'win':
                    self.check_win()         # aposta pode ter levado a 1M
                    if self.state != GameState.WIN:
                        self.advance_phase()

                elif resultado == 'skip':
                    self.advance_phase()

                elif resultado == 'game_over':
                    self.change_state(GameState.LOSE)