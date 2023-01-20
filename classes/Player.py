from IBet import IBet
from IHand import IHand
from IPlayer import IPlayer


class Player(IPlayer):
    def __init__(self, hand: IHand, bet: IBet):
        self._hand = hand
        self._bet = bet

    # property that returns the IHand object representing the player's hand
    @property
    def hand(self) -> IHand:
        return self._hand

    # property that returns the IBet object representing the player's bet
    @property
    def bet(self) -> IBet:
        return self._bet

    def is_blackjack(self) -> bool:
        if len(self._hand) != 2:
            return False

        if (self._hand[0].rank != 'Ace' or self._hand[1].rank not in ['10', 'Jack', 'Queen', 'King']) and (
                self._hand[1].rank != 'Ace' or self._hand[0].rank not in ['10', 'Jack', 'Queen', 'King']):
            return False
        return True

    # method increases the amount of the player's bet by the given amount
    def win(self, amount: int) -> None:
        self._bet.increase(amount)

    # method decreases the amount of the player's bet by the given amount
    def lose(self, amount: int) -> None:
        self._bet.decrease(amount)
