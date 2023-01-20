from abc import ABC, abstractmethod

from ICard import ICard


# interface defines the properties and methods that the Deck class should have
class IDeck(ABC):
    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def draw(self) -> ICard:
        pass

    @abstractmethod
    def remaining(self) -> int:
        pass