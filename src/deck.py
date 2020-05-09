import random
from card import Card

class Deck():
    # Global: Array of cards
    card_list = []

    def __init__(self):
        # init the card list, total 52 cards
        self.constructDeck()

    # construct deck by input cards into card_list array
    def constructDeck(self):
        for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for v in ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']:
                self.card_list.append(Card(v, s))

    # shuffle cards
    def shuffle(self):
        random.shuffle(self.card_list)

    def dealOneCard(self):
        if len(self.card_list) > 0:
            return self.card_list.pop()
        else:
            return None

    # for test use only
    def showDeck(self):
        for card in self.card_list:
            card.showCard()
