from card import *

c = Card("A","Hearts")
print(c)
try:
    d = Card("10","Hearts")
except Exception:
    try:
        d = Card("J","Blob")
    except Exception:
        d = Card("J", "Spades")
print(d)

d = Deck()
print(d)
d.shuffle()
print(d)