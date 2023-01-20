from IBet import IBet


class Bet(IBet):
    def __init__(self, amount: float):
        self._amount = amount

    @property
    def amount(self) -> float:
        return self._amount

    # method increases the amount of the bet
    def increase(self, amount: int) -> None:
        self._amount += amount

    # method decreases the amount of the bet
    def decrease(self, amount: int) -> None:
        if self._amount - amount < 0:
            raise ValueError("Bet amount cannot be negative")
        self._amount -= amount
