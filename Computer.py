from Player import Player


class Computer(Player):

    def __init__(self):
        super().__init__()

    def collect_cards(self):
        '''
        Loops and continuously picks up cards until should_pickup_card is false
        '''
        pass

    def should_pickup_card(self):
        '''
        Method that returns a boolean whether or not with current points, the computer should pick
        up another card
        '''
        pass
