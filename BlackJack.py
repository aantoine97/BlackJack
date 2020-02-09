from Deck import Deck
from Human import Human
from Computer import Computer
from Card import Card
import Utilities


def get_bet(player):
    '''
    Gets the player's bet
    '''

    player_bet = input("\nEnter the amount of chips you would like to bet: ")
    valid_input = True
    valid_number = True

    try:
        player_bet = int(player_bet)
        if player_bet <= 0 or player_bet > player.chips:
            valid_number = False
    except:
        valid_input = False

    while not valid_input or not valid_number:
        try:
            if not valid_input:
                player_bet = int(input("Please enter a number: "))
                valid_input = True
            else:
                player_bet = int(input(
                    "Please enter a number between 0 and your account balance which is {}: ".format(player.chips)))
            if player_bet <= 0 or player_bet > player.chips:
                valid_number = False
            else:
                break
        except:
            valid_input = False

    player.place_bet(player_bet)
    return player_bet


def ask_to_play_again():
    restart = input("\nWould you like to play again? (y/n): ")
    restart = Utilities.get_valid_response(
        restart.lower(), ["y", "n"])
    return True if restart.lower() == "y" else False


def game_set_up():
    print(("\n" * 100) + "Welcome to Austin's Black Jack! I recommend you make your console as big as possible so you can see "
                       + " most of your hand without needing to scroll.\nEnjoy!" + "\n\n")
    print_rules = input(
        "Would you like an explanation of the game and rules? (y/n) ")
    print_rules = Utilities.get_valid_response(print_rules, ["y", "n"])

    if print_rules.lower() == "y":
        print("\nYou start out with a balance of 500 chips and two cards. You can then bet as many of your chips as you want for the current game."
              + " You will then continuously draw cards until the point value of your cards gets as close to 21 as possible without going"
              + " over (you'll bust and lose if you go over automatically losing your bet!) When you're confident that you have the best"
              + " point value possible, you can choose to stay. You won't be able to draw anymore and your points won't change for the rest"
              + " of the game. At this point, the computer will continuously draw cards to try to beat your score. The same rules apply to"
              + " the computer.\n\nBelow you can see the point value  of each card\nAce:\t\t\t1 or 11 points (this is a special card and it's"
              + " point value is whatever is preferable for your current point score!)\n2 - 9:\t\t\tThese cards have a point value equal to"
              + " their number\n10, Jack, Queen, King:\tThese all have a point value of 10\n\nYou now know everything you need to to play!\n\nPress"
              + " enter when you're ready to start the game")
        input()


def play():
    play_again = True
    player = Human()
    computer = Computer()

    while play_again:
        player.empty_hand()
        computer.empty_hand()

        deck = Deck()
        player.pick_up_card(deck.give_card())
        player.pick_up_card(deck.give_card())

        computer.pick_up_card(deck.give_card())
        computer.pick_up_card(deck.give_card())

        print("\nComputer hand: ")
        computer.display_hand()

        print("\nYour hand: ")
        player.display_hand()

        player.get_points()
        print("Your current chip balance is: {}".format(player.chips))

        player_bet = get_bet(player)

        keep_drawing = True

        while keep_drawing:
            user_input = input(
                "\nHit or stay? (type h for hit or s for stay): ")
            user_input = Utilities.get_valid_response(
                user_input.lower(), ["h", "s"])

            if user_input == "s":
                keep_drawing = False
            else:
                player.pick_up_card(deck.give_card())
                player.display_hand()
                player.get_points()
                if player.bust():
                    print(
                        "\nYou went bust! Unfortunately you lost your bet and your chip balance is {}".format(player.chips))
                    play_again = ask_to_play_again()
                    break

        if not player.bust():
            print(
                "\nThe computer will now draw until it either beats your score or busts...")
            computer.collect_cards(deck, player)

            if computer.bust():
                player.collect_winnings(player_bet * 2)
                print("\nThe computer went bust so you win! Your total score was {} and the computer's was {}. Your chip balance is {}".format(
                    player.get_total_points(), computer.get_total_points(), player.chips))
                play_again = ask_to_play_again()
            elif computer.get_total_points() == player.get_total_points():
                player.collect_winnings(player_bet)
                print("\nLooks like there's been a tie! You get to keep your bet so your chip balance is {}".format(
                    player.chips))
                play_again = ask_to_play_again()
            else:
                print(
                    "\nThe computer beat your score :(... Your total score was {} and the computer's was {}. Your chip balance is {}".format(player.get_total_points(), computer.get_total_points(), player.chips))
                play_again = ask_to_play_again()


def start_game():
    '''
    Manages the flow of the game
    '''

    game_set_up()
    play()


if __name__ == "__main__":
    start_game()
