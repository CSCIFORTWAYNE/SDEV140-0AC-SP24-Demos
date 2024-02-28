from card import *

c = Card("10","Hearts")
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

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800, 600)
wn.title("Deck of Cards Simulator by @TokyoEdtech")
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
c.render(0,0,pen)
wn.mainloop()