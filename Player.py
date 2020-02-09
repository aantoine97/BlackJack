class Player():
    def __init__(self):
        self.chips = 500
        self.points = 0
        self.hand = []
        self.aces = 0

    def pick_up_card(self, card):
        '''
        Picks up a card and adds the points to the player's point balance
        '''

        self.hand.append(card)
        if not isinstance(card.point_val, tuple):
            self.points += card.point_val
        else:
            self.aces += 1

    def display_hand(self):
        '''
        Display's the player's hand
        '''

        for card in self.hand:
            print(card)

    def get_total_points(self):
        total_score = self.points

        if self.aces == 0:
            return total_score
        elif self.aces == 1 and total_score + 11 > 21:
            return total_score + 1
        elif self.aces == 1 and total_score + 11 <= 21:
            return total_score + 11
        elif self.aces > 1:
            for _ in range(0, self.aces):
                if total_score + 11 <= 21 and (self.aces - 1) + total_score + 11 <= 21:
                    total_score += 11
                else:
                    total_score += 1

        return total_score

    def bust(self):
        return self.get_total_points() > 21

    def empty_hand(self):
        self.hand.clear()
        self.points = 0
        self.aces = 0
