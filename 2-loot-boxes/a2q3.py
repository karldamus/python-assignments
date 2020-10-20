# Raven Runner | ©2020 Karl Damus, All Rights Reserved
# Created on October 18, 2020
# a2q3.py

import math
import random

# game variables
gamerName = ""
boxNames = ["The GeeGee", "The Raven", "The Three-Eyed Raven"]
boxRarity = ["Common", "Rare", "Epic"]
boxPrices = [1.50, 3.00, 7.99]
boxCount = len(boxNames)
common = 0
rare = 0
epic = 0
cart = []

# game functions
def printLootbox():
    print("\nPlease select a loot box from the menu below:\n")
    i = 0
    while i < boxCount:
        print(str(i + 1) + ". " + "[" + boxRarity[i] + "]" + " (" + str('{:4.2f}'.format(boxPrices[i])) + ") " + boxNames[i])
        i += 1
    i += 1
    print(str(i) + ". Complete Purchase")

# def requestLootbox():


# game start
# gamerName = input("\nHELLO, GAMER! Welcome to the Raven Runner Loot Box Purchasing System. First, what's your player name?\n")

# user has not finished their order yet so set orderComplete to False
orderComplete = False
while orderComplete == False:
    # lootbox function
    printLootbox()
    userBox = input()

    # catch any non digit answers
    if userBox.isdigit():
        # user types 4 to complete their order so set orderComplete to True
        if(int(userBox) == int(4)):
            orderComplete = True
        elif((int(userBox) >= 1) and (int(userBox) <= 3)):
            cart.append(userBox)
        else:
            print("\nThat is not a listed box. Please enter a number between 1 and 3")
    else:
        print("\nThat is not a valid number. Please enter a number between 1 and 3")

print(sorted(cart))