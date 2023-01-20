from abc import ABC, abstractmethod
from typing import List

from ICard import ICard


# interface defines the properties and methods that the Hand class should have
class IHand(ABC):
    @property
    @abstractmethod
    def cards(self) -> List[ICard]:
        pass

    @abstractmethod
    def add_card(self, card: ICard) -> None:
        pass

    @abstractmethod
    def remove_card(self, card: ICard) -> None:
        pass

    @abstractmethod
    def score(self) -> int:
        pass
