from typing import List

from ICard import ICard
from IDealer import IDealer
from IDeck import IDeck
from IPlayer import IPlayer


class Dealer(IDealer):
    def __init__(self, deck: IDeck):
        self._deck = deck

    # property that returns the IDeck object representing the dealer's deck
    @property
    def deck(self) -> IDeck:
        return self._deck

    # method deals two cards to each player in the list of players passed to it
    def deal(self, players: List[IPlayer]) -> None:
        for player in players:
            player.hand.add_card(self._deck.draw())
            player.hand.add_card(self._deck.draw())

    # method returns a card from the top of the deck
    def get_card(self) -> ICard:
        return self._deck.draw()
