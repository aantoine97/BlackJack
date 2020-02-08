from Player import Player


class Human(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def place_bet(self, amount):
        self.account_balance -= amount
        return amount
