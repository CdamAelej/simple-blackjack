from ICard import ICard


class Card(ICard):
    def __init__(self, suit: str, rank: str):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self) -> str:
        return self._suit

    @property
    def rank(self) -> str:
        return self._rank

    def __str__(self) -> str:
        return f"{self._rank} of {self._suit}"
