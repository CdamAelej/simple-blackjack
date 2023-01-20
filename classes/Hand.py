from typing import List

from ICard import ICard
from IHand import IHand


class Hand(IHand):
    def __init__(self):
        self._cards = []

    # list of cards in player hand
    @property
    def cards(self) -> List[ICard]:
        return self._cards

    # method adds a card to the hand
    def add_card(self, card: ICard) -> None:
        self._cards.append(card)

    # method removes a card from the hand
    def remove_card(self, card: ICard) -> None:
        self._cards.remove(card)

    # method calculates the score of the hand based on the ranks of the cards it contains.
    def score(self) -> int:
        score = 0
        for card in self._cards:
            if card.rank == "Ace":
                score += 1
            elif card.rank in ["Jack", "Queen", "King"]:
                score += 10
            else:
                score += int(card.rank)
        return score
