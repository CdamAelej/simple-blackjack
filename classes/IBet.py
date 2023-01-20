from abc import ABC, abstractmethod


# interface defines the properties and methods that the Bet class should have
class IBet(ABC):
    @property
    @abstractmethod
    def amount(self) -> int:
        pass

    @abstractmethod
    def increase(self, amount: int) -> None:
        pass

    @abstractmethod
    def decrease(self, amount: int) -> None:
        pass
