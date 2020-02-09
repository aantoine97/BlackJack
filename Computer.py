from Player import Player
import time


class Computer(Player):

    def __init__(self):
        super().__init__()

    def should_pickup_card(self, player):
        '''
        Method that returns a boolean whether or not with current points, the computer should pick
        up another card
        '''
        if self.get_total_points() > player.get_total_points():
            return False
        else:
            return True

    def collect_cards(self, deck, player):
        '''
        Loops and continuously picks up cards until should_pickup_card is false
        '''

        while self.should_pickup_card(player):
            print("\nDrawing card...")
            time.sleep(1)
            self.pick_up_card(deck.give_card())
            self.display_hand()
            self.get_points()
            time.sleep(1)

            if self.bust():
                break

    def get_points(self):
        '''
        Shows the total points the computer has
        '''

        print("\nThe computer has {} points and {} aces.".format(
            self.points, self.aces))
