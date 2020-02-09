from Player import Player


class Human(Player):

    def __init__(self):
        super().__init__()

    def place_bet(self, amount):
        '''
        Subtracts the players chips by how much they bet
        '''

        self.chips -= amount
        return amount

    def get_points(self):
        '''
        Shows the points and aces the player has
        '''

        print("\nYou have {} points and {} aces.".format(self.points, self.aces))

    def collect_winnings(self, amount):
        self.chips += amount
