import random
from constants import *

class Card:
    def __init__(self, id, image):
        self.id = id
        self.image = image

    def __eq__(self, other): 
        return isinstance(other, Card) and self.id == other.id

class BetOption:
    def __init__(self, label, percentage):
        self.label = label
        self.percentage = percentage 

class TigrinhoGame:
    def __init__(self, phase_number):
        self.phase_number = phase_number
        self.deck = []
        for i in range(deck_size):
            self.deck.append(i)
        self.drawn_cards = []
        self.player_card = None
        self.bet_option = None
        self.bet_amount = 0
        self.state = 'betting'

    def get_bet_options(self):
        options = {
            1: [BetOption("Não apostar", 0.0),
                BetOption("Aposta Segura (30%)", 0.30),
                BetOption("Arriscar (80%)", 0.80)],

            2: [BetOption("Não apostar", 0.0),
                BetOption("Aposta Segura (50%)", 0.50),
                BetOption("Arriscar (80%)", 0.80)],

            3: [BetOption("Não apostar", 0.0),
                BetOption("Aposta Segura (70%)", 0.70),
                BetOption("Tudo ou Nada (100%)", 1.0)],
        }
        return options[self.phase_number]

    def place_bet(self, bet_option):
        self.bet_option = bet_option
        self.bet_amount = int(self.player.follower_count * bet_option.percentage)

        if bet_option.percentage == 0:
            self.state = 'result'

        else:
            self.state = 'choosing_card'

    def choose_card(self, card):
        self.player_card = card
        self.state = 'drawing'

    def draw_cards(self):
        self.drawn_cards = random.sample(self.deck, drawn_amount)
        self.state = 'result'

    def resolve(self):
        if self.bet_option.percentage == 0 and self.phase_number == 3:
            if self.player.follower_count < 1_000_000:
                return 'game_over'
            return 'skip'

        if self.bet_option.percentage == 0:
            return 'skip'

        if self.player_card in self.drawn_cards:
            self.player.follower_count += self.bet_amount
            return 'win'
        else:
            self.player.follower_count -= self.bet_amount
            if self.player.follower_count <= 0:
                return 'game_over'
            return 'lose'