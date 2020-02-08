class Player():
    def __init__(self):
        self.account_balance = 500
        self.points = 0
        self.hand = []

    def pick_up_card(self, card):
        self.hand.append(card)
        self.points += card.point_val

    def get_points(self):
        pass

    def display_hand(self):
        pass
