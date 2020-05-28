import random as random

class Deck:

    def __init__(self):
        self.cards = []
        self.discard = []

    def discard(self,card):
        self.discard.append(card)
    
    def draw(self):
        card = self.cards.pop()
        return card

    def init(self):
        suits = ["Spades","Hearts","Clubs","Diamonds"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for suit in suits:
            for value in values:
                card = Card(suit,value)
                self.cards.append(card)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def reset(self):
        self.card = self.discard + self.cards
        self.shuffle()

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

