"""cards example"""

suits = { "SPADES":'♠',"HEARTS":'♥', "DIAMONDS":'♦', "CLUBS":'♣'}

userSuit = input("Enter a suit name: ")
#while not userSuit.upper() == 'SPADES' and not userSuit.upper() == 'HEARTS' and not userSuit.upper() == 'CLUBS' and not userSuit.upper() == 'DIAMONDS':
while not userSuit.upper() in suits:
    print("Error: Invalid suit. Valid suits are Spades, Hearts, Diamonds, Clubs.")
    userSuit = input("Enter a suit name: ")
print("The symbol for ", userSuit, " is ", suits[userSuit.upper()])

userSuit = input("Enter a the new suit name: ")
suits[userSuit.upper()] = '֍'
print("New suit created", userSuit,suits[userSuit.upper()])
print(suits)

keys = list(suits.keys())
keys.sort()
for key in keys:
    print(key, suits[key])