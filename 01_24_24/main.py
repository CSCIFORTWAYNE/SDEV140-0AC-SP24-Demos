"""Demo for if and while"""
import random

number = random.randint(0,100)
userNum = ""
while userNum == "" or userNum < 0 or userNum > 100:
    userNum = input("Enter a number: ")
    if userNum != "":
        userNum = int(userNum)


if userNum <= number:
    print("I won!!")
else:
    print("You did ok~")

print("Thanks for playing")

if number >= 90:
    print("A")
elif number >= 80:
    print ("B")
elif number >= 70:
    print("C")
elif number >= 60:
    print("D")
else:
    print("F")

if number * 6 - 34 == 5 or userNum < 50 and userNum > 0:
    print("I'm here")
else:
    print("False")

if 0 <= userNum and userNum <= 10:
    print("UserNum is between 0 and 10")
else:
    print("UserNum is not between 0 and 10")

while number < 30:
    print("something")
    number += 1
