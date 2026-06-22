class GameManager:
    def __init__(self):
            self.state = 'playing'
            self.current_phase = 1
            self.max_life = 3
            self.score = 0

            self.phase_names = {
                1: 'Rezende',
                2: 'Zé Felipe',
                3: 'Vini Jr.'
            }

    def get_phase_name(self):
        return self.phase_names[self.current_phase]

    def check_progress(self, player):
        if self.current_phase == 1 and player.follower_count >= 200:
            self.current_phase = 2
            self.max_life = 4
            player.life = 4
            self.state = 'phase_transition'

        elif self.current_phase == 2 and player.follower_count >= 450:
            self.current_phase = 3
            self.max_life = 5
            player.life = 5
            self.state = 'phase_transition'

        elif self.current_phase == 3 and player.follower_count >= 700:
            self.state = 'victory'

    def check_defeat(self, player):
        if player.life <= 0:
            self.state = 'game_over'

    def continue_game(self):
        if self.state == 'phase_transition':
            self.state = 'playing'

    def add_score(self, amount):
        self.score += amount