from abc import ABC, abstractmethod
from typing import List

from ICard import ICard
from IDeck import IDeck
from IPlayer import IPlayer


# interface defines the properties and methods that the Card class should have
class IDealer(ABC):
    @property
    @abstractmethod
    def deck(self) -> IDeck:
        pass

    @abstractmethod
    def is_blackjack(self) -> bool:
        pass

    @abstractmethod
    def deal(self, players: List[IPlayer]) -> None:
        pass

    @abstractmethod
    def get_card(self) -> ICard:
        pass
