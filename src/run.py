from deck import Deck
from player import Player

# Start the Game
# init a deck for play
deck = Deck()
# add a player for deck
player = Player(deck,'Jing')
# shuffle the cards in deck
deck.shuffle()
# player call to get card for 53 times (get 52 cards total)
# and return cards on hand
for i in range(53):
    player.playerCallCard(deck)
player.showPlayersHand()
