from Deck import Deck
from Human import Human
from Computer import Computer
from Card import Card
import Utilities


def start_game():
    deck = Deck()
    player_name = Utilities.get_player_name()
    player = Human(player_name)
    computer = Computer()

    player.pick_up_card(deck.give_card())
    player.pick_up_card(deck.give_card())

    computer.pick_up_card(deck.give_card())
    computer.pick_up_card(deck.give_card())

    print("\nYour hand: ")
    for card in player.hand:
        print(card)

    print("\nComputer hand: ")
    for card in computer.hand:
        print(card)


if __name__ == "__main__":
    start_game()
