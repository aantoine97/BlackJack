from random import shuffle
from Card import Card


class Deck():
    card_types = {1: "HEARTS", 2: "DIAMONDS", 3: "CLUBS", 4: "SPADES"}

    def __init__(self):
        self.cards = []

        for i in range(1, 14):
            for index in range(1, 5):
                num = i
                card_type = self.card_types[index]

                if i == 1:
                    point_val = (1, 11)
                elif i >= 11:
                    point_val = 10
                else:
                    point_val = i

                card = Card(num, card_type, point_val)
                self.cards.append(card)

        shuffle(self.cards)

    def shuffe_deck(self):
        shuffle(self.cards)

    def give_card(self):
        return self.cards.pop()
