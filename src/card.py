class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # for test use only
    def showCard(self):
        print(str(self.value) + " of " + str(self.suit))
