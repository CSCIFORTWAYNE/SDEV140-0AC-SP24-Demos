import random

class Card(object):
    """A card object with a suit and rank."""

    RANKS = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    SUITS = ("Spades", "Diamonds", "Hearts", "Clubs")
    SUIT_SYMBOL = {"Diamonds":"♦", "Clubs":"♣", "Hearts":"♥", "Spades":"♠"}

    def __init__(self,rank:str,suit:str):
        """Creates a card with the given rank and suit."""
        if rank in Card.RANKS:
           self.rank = rank 
        else:    
            raise Exception("Rank must be between 0 and 12")
        if suit in Card.SUITS:
            self.suit = suit
        else:
            raise Exception("Suit must be Spades, Diamonds, Hearts, or Clubs")
    def __str__(self):
        """Returns the strign representation of a card"""
        return self.rank + Card.SUIT_SYMBOL[self.suit]

class Deck(object):
    """A deck containing 52 cards."""
    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        if len(self) == 0:
            return None
        else:
            return self.cards.pop()
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        result = ""
        for c in self.cards:
            result = result + str(c) + "\n"
        return result
        
        