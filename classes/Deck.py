import random

from Card import Card
from ICard import ICard
from IDeck import IDeck


# class to create a deck using database
class Deck(IDeck):
    def __init__(self, session):
        self.session = session
        self.cards = session.query(Card).all()
        self.shuffle()

    # method to shuffling deck
    def shuffle(self):
        random.shuffle(self.cards)

    # method returns a card from the top of the deck
    def draw(self) -> ICard:
        if self.remaining() > 0:
            return self.cards.pop()

    # method returns the number of cards remaining in the deck
    def remaining(self) -> int:
        return len(self.cards)
