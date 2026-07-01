class GameManager:
    def __init__(self):
            self.current_phase = 0
            self.states = {
                0: 'Game Start',
                1: 'Rezende',
                2: 'Zé Felipe',
                3: 'Vini Jr.',
                4: 'Phase Transition',
                5: 'Game Over',
                6: 'Victory'
            }

    # Verifica se o jogador atingiu os requisitos
    def check_progress(self, player):
        if (self.current_phase == 3 and player.follower_count < 1000) or player.life <= 0:
            self.current_phase = 5

        elif self.current_phase == 3 and player.life > 0 and player.follower_count >= 1000:
            self.current_phase = 6