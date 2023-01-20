from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cards.db')
base = declarative_base()


class Card(base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    suit = Column(String)
    rank = Column(String)

base.metadata.create_all(bind=engine)


# create a new session
Session = sessionmaker(bind=engine)
session = Session()

# check if table is empty
if not session.query(Card).first():
    # create a new deck of cards
    deck = [Card(suit=s, rank=r) for s in ["Hearts", "Diamonds", "Clubs", "Spades"] for r in
            ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]
    session.add_all(deck)
    session.commit()
else:
    # table is not empty, close session
    session.close()