from IDealer import IDealer
from IDeck import IDeck
from IGame import IGame
from IPlayer import IPlayer


class Game(IGame):
    def __init__(self, player: IPlayer, dealer: IDealer, deck: IDeck):
        self._player = player
        self._dealer = dealer
        self._deck = deck

    @property
    def player(self) -> IPlayer:
        return self._player

    @property
    def dealer(self) -> IDealer:
        return self._dealer

    @property
    def deck(self) -> IDeck:
        return self._deck

    # Method to play the game, it contains the gameplay logic
    def play(self) -> None:
        # Shuffle the deck
        self._deck.shuffle()

        # Draw initial cards for the player and the dealer
        self._player.add_card(self._deck.draw())
        self._dealer.add_card(self._deck.draw())
        self._player.add_card(self._deck.draw())
        self._dealer.add_card(self._deck.draw())

        # Check if the player has blackjack
        if self._player.is_blackjack():
            print("Player has blackjack! Player wins!")
            self._player.increase_balance(self._player.bet.amount * 2.5)
            return

        # Check if the dealer has blackjack
        if self._dealer.is_blackjack:
            print("Dealer has blackjack! Dealer wins!")
            return

        # Player's turn
        while self._player.bet():
            self._player.add_card(self._deck.draw())
            if self._player.is_busted():
                print("Player is busted! Dealer wins!")
                return

        # Dealer's turn
        while self._dealer.hit():
            self._dealer.add_card(self._deck.draw())
            if self._dealer.is_busted():
                print("Dealer is busted! Player wins!")
                self._player.increase_balance(self._player.bet.amount * 2)
                return

        # Compare hands
        if self._player.hand_value() > self._dealer.hand_value():
            print("Player wins!")
            self._player.increase_balance(self._player.bet.amount * 2)
        elif self._player.hand_value() < self._dealer.hand_value():
            print("Dealer wins!")
        else:
            print("It's a tie!")
            self._player.increase_balance(self._player.bet.amount)



    def check_win(self) -> bool:
        """
        Method to check if the player has won or lost
        """
        pass

    def payout(self) -> float:
        """
        Method to calculate the payout for the player
        """
        pass