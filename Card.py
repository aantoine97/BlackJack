class Card():

    card_val = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6",
                7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K"}

    def __init__(self, num_val, card_type, point_value):
        self.num_val = num_val
        self.card_type = card_type
        self.point_val = point_value

    def __str__(self):
        if self.card_type == "HEARTS":
            symbol = "♥"
        elif self.card_type == "DIAMONDS":
            symbol = "♦"
        elif self.card_type == "CLUBS":
            symbol = "♣"
        else:
            symbol = "♠"

        top_bottom = " ---------"
        if self.num_val != 10:
            symbol_line1 = "| {}       |\n".format(self.card_val[self.num_val])
            symbol_line2 = "|       {} |\n".format(self.card_val[self.num_val])
        else:
            symbol_line1 = "| {}      |\n".format(self.card_val[self.num_val])
            symbol_line2 = "|      {} |\n".format(self.card_val[self.num_val])

        result = top_bottom + "\n"

        for i in range(0, 7):
            if i == 0:
                result += symbol_line1
            elif i == 6:
                result += symbol_line2
            elif i == 3:
                result += "|    {}    |\n".format(symbol)
            else:
                result += "|         |\n"

        result += top_bottom
        return result
