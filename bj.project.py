import tkinter as tk
from tkinter import PhotoImage, messagebox
import random
class Card:
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value        
        pass
    def get_numeric_value(self) -> int:
        if self.value in ['K', 'Q', 'J']:
            return 10
        elif self.value == 'A':
            return 11
        else:
            return int(self.value)
    pass
    def get_image(self):
        return f"img/{self.value}_of_{self.suit}.png"        
    pass
class Deck:
    def __init__(self, suits = [], values = []):
        self.cards = []
        for value in values:
            for suit in suits:
                self.cards.append(Card(suit,value))
        pass
    def shuffle(self):
        random.shuffle(self.cards)
        pass
    def deal(self)-> Card:
        if not self.cards:
            raise ValueError("Deck is empty")
        return self.cards.pop()
    pass
class EnglishDeck(Deck):
    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        super().__init__(suits, values)
        pass
class Hand:
    def __init__(self):
        self.cards = []
        pass
    def add_card(self, card: Card):
        self.cards.append(card)
        pass
    def value(self)->int:
        total_value = sum(card.get_numeric_value() for card in self.cards)
        num_aces = sum(1 for card in self.cards if card.value == 'A')
        while total_value > 21 and num_aces:
            total_value -= 10
            num_aces -= 1
        return total_value
    pass
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        pass
class BlackjackGame:
    def __init__(self):
        self.player = Player("Player")
        self.dealer = Player("Dealer")
        self.deck = EnglishDeck()
        self.deck.shuffle()
        pass
    def start_game(self):
        self.player.hand = Hand()
        self.dealer.hand = Hand()
        for i in range (2):
            self.player.hand.add_card(self.deck.deal())
            self.dealer.hand.add_card(self.deck.deal())
        pass
    def hit(self)-> bool:
        self.player.hand.add_card(self.deck.deal())
        return self.player.hand.value() > 21
    pass
    def dealer_hit(self) -> bool:
        if self.dealer.hand.value() >= 17:
            return False  # No más cartas si el dealer tiene 17 o más
        self.dealer.hand.add_card(self.deck.deal())
        return self.dealer.hand.value() <= 21
    def determine_winner(self):
        player_value = self.player.hand.value()
        dealer_value = self.dealer.hand.value()
        if player_value > 21:
            return "You've busted! The house wins."
        if dealer_value > 21:
            return "Dealer busts! You win."
        if player_value > dealer_value:
            return "You win!"
        elif dealer_value > player_value:
            return "Dealer wins."
        else:
            return "It's a tie!"
    pass
# The GUI code is provided, so students