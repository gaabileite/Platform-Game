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

    # Verifica se o jogador atingiu os requisitos para avançar para a próxima fase
    def check_progress(self, player):
        if self.current_phase == 1 and player.follower_count >= 200:
            self.current_phase = 1.5
            player.life += 1

        elif self.current_phase == 2 and player.follower_count >= 450:
            self.current_phase = 2.5
            player.life += 5

        elif self.current_phase == 3 and player.follower_count >= 700:
            self.current_phase = 5

        if player.life <= 0 or (player.follower_count < 0 and self.current_phase >= 1):
            self.current_phase = 6
