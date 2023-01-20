from abc import ABC, abstractmethod
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

# creating database connection
engine = create_engine('sqlite:///cards.db')
base = declarative_base()


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


"""
Creating class CardTable responsible for creation Card Table.
Thanks to its constructor I can create new table records.
"""
class CardTable(base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    suit = Column(String)
    rank = Column(String)


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

# class to create a deck using database
class Deck(IDeck):
    def __init__(self, session):
        self.session = session
        self.cards = session.query(Card).all()
        self.shuffle()

    # method to shuffling deck
    def shuffle(self):
        random.shuffle(self.cards)

    # method returns a card from the top of the deck
    def draw(self) -> ICard:
        if self.remaining() > 0:
            return self.cards.pop()

    # method returns the number of cards remaining in the deck
    def remaining(self) -> int:
        return len(self.cards)


# interface defines the properties and methods that the Bet class should have
class IBet(ABC):
    @property
    @abstractmethod
    def amount(self) -> float:
        pass

    @abstractmethod
    def increase(self, amount: float) -> None:
        pass

    @abstractmethod
    def decrease(self, amount: float) -> None:
        pass

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

class Hand(IHand):
    def __init__(self):
        self._cards = []

    # list of cards in player hand
    @property
    def cards(self) -> List[ICard]:
        return self._cards

    # method adds a card to the hand
    def add_card(self, card: ICard) -> None:
        self._cards.append(card)

    # method removes a card from the hand
    def remove_card(self, card: ICard) -> None:
        self._cards.remove(card)

    # method calculates the score of the hand based on the ranks of the cards it contains.
    def score(self) -> int:
        score = 0
        for card in self._cards:
            if card.rank == "Ace":
                score += 1
            elif card.rank in ["Jack", "Queen", "King"]:
                score += 10
            else:
                score += int(card.rank)
        return score


base.metadata.create_all(bind=engine)


# create a new session
Session = sessionmaker(bind=engine)
session = Session()

# checking if table is empty
if not session.query(CardTable).first():
    # create a new deck of cards
    deck = [CardTable(suit=s, rank=r) for s in ["Hearts", "Diamonds", "Clubs", "Spades"] for r in
            ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]
    session.add_all(deck)
    session.commit()
else:
    # table is not empty, closing session
    session.close()