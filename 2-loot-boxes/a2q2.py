# Raven Runner | ©2020 Karl Damus, All Rights Reserved
# Created on October 12, 2020
# a2q2.py

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

# game start
gamerName = input("\nHELLO, GAMER! Welcome to the Raven Runner Loot Box Purchasing System. First, what's your player name?\n")

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
            updatedValue = int(int(userBox) - 1) # update the value to associate with list value
            itemDisplayText = str(boxNames[updatedValue])
            # ensure no false inputs for the quantity
            falseQuantity = True
            while falseQuantity == True:
                print("How many of " + itemDisplayText + " (" + str(boxPrices[updatedValue]) + ") "  "would you like to purchase?")
                quantity = input()
                if quantity.isdigit():
                    if(int(quantity) > 0):
                        # do calc and push to array then set falseQuantity to False
                        quantitativePush = 0
                        while quantitativePush < int(quantity):
                            cart.append(updatedValue)
                            quantitativePush += 1
                        falseQuantity = False
                else:
                    print("\nThat is not a valid quantity. Please enter any number above 0")
        else:
            print("\nThat is not a listed box. Please enter a number between 1 and 3")
    else:
        print("\nThat is not a valid number. Please enter a number between 1 and 3")

# calculations of boxes
finalCart = sorted(cart)
commons = 0
rares = 0
epics = 0

for i in finalCart:
    if i == int(0):
        commons += 1
    if i == int(1):
        rares += 1
    if i == int(2):
        epics += 1

totalCost = ((commons * boxPrices[0]) + (rares * boxPrices[1]) + (epics * boxPrices[2]))

# give a receipt if the user actually bought anything
if (commons != 0) or (rares != 0) or (epics != 0):

    # user has finished their order let's print the lootboxes
    print("\nThanks, " + str(gamerName) + " Here is your receipt:")
    print("---------------------------------")
    if commons > 0:
        print(str(commons) + "x" + "\t" + boxNames[0] + " (" + str(boxPrices[0]) + ")")
    if rares > 0:
        print(str(rares) + "x" + "\t" + boxNames[1] + " (" + str(boxPrices[1]) + ")")
    if epics > 0:
        print(str(epics) + "x" + "\t" + boxNames[2] + " (" + str(boxPrices[2]) + ")")
    print("---------------------------------")
    print ("\nTotal Cost: $" + str('{:4.2f}'.format(totalCost)))
    print("Thank you! Good luck, gamer!\n")

    print("\nThanks for shopping with us " + str(gamerName) + "! Come back anytime.\n\n")    

# user did not buy anything 
else:
    print("\nThanks for looking! Come back if you change your mind.\n\n")