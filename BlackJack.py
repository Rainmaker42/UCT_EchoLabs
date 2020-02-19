'''
BlackJack

List of cards 1 deck so 52 cards total

'''
import random
#Built deck (Constant)
DeckOfCards = {1:"Ace", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:'7', 8:'8', 9:'9',
               10:'10', 11:"Jack", 12:"Queen", 13:'King'}

dealerTotal = 0
playerTotal = 0

print("Welcome to BlackJack")
UserName = input("What is your name: ")
dealerTotal, playerTotal = 0, 0

while dealerTotal <=21 or playerTotal <=21:
    playerTotal += random.randint(1, 13)
    if playerTotal > 21:
        break
    dealerTotal += random.randint(1, 13)
    print("Dealer total is {}".format(dealerTotal))
    print("{} total is {}".format(UserName, playerTotal))


if playerTotal > 21:
    print("Everybody Lost")
elif dealerTotal > 21 and playerTotal <= 21:
    print("{} has won!".format(UserName))
else:
    print("Dealer has won!")
