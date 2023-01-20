from abc import ABC, abstractmethod

from IBet import IBet
from IHand import IHand


# interface defines the properties and methods that the Player class should have
class IPlayer(ABC):
    @property
    @abstractmethod
    def hand(self) -> IHand:
        pass

    @property
    @abstractmethod
    def bet(self) -> IBet:
        pass

    @abstractmethod
    def is_blackjack(self) -> bool:
        pass

    @abstractmethod
    def win(self, amount: int) -> None:
        pass

    @abstractmethod
    def lose(self, amount: int) -> None:
        pass

