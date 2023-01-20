from abc import ABC, abstractmethod

from IDealer import IDealer
from IDeck import IDeck
from IPlayer import IPlayer


class IGame(ABC):
    @property
    @abstractmethod
    def player(self) -> IPlayer:
        pass

    @property
    @abstractmethod
    def dealer(self) -> IDealer:
        pass

    @property
    @abstractmethod
    def deck(self) -> IDeck:
        pass

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def check_win(self) -> bool:
        pass

    @abstractmethod
    def payout(self) -> int:
        pass