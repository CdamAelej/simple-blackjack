from abc import ABC, abstractmethod


# interface defines the properties and methods that the Card class should have
class ICard(ABC):
    @property
    @abstractmethod
    def suit(self) -> str:
        pass

    @property
    @abstractmethod
    def rank(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
