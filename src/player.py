from deck import Deck

class Player():
    def __init__(self, deck, name):
        self.name = name
        self.deck = deck
        self._players_hand = []

    # call a card from deck
    def playerCallCard(self, deck):
        card = deck.dealOneCard()
        if card:
            self._players_hand.append(card)
            return ('Get a Card, you have total' + str(len(self._players_hand)))
        else:
            return 'No more card on deck.'

    # for test use only
    def showPlayersHand(self):
        for card in self._players_hand:
            card.showCard()
