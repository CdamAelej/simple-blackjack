import classes
from database.database import session

#Create a new deck of cards
deck = classes.Deck.Deck(session)

#Create a new dealer
dealer = classes.Dealer.Dealer(deck)

# Create a new hand for the player
hand = classes.Hand.Hand()

# Create a new bet for the player
bet = classes.Bet.Bet(10.0)

# Create a new player
player = classes.Player.Player(hand, bet)
