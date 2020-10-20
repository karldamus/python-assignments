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

# print("Common: " + str(commons))
# print("Rare: " + str(rares))
# print("Epic: " + str(epics))



# user has finished their order let's print the lootboxes
print("\nThanks, Test! Here is your receipt:")
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


# loop through each item in cart
# for i in finalCart:







# print(cart)



# if common > 0:
#     print(str(common) + "x " + boxNames[0] + " ($" + str(boxPrices[0]) + ")")
#     total += (int(common) * float(boxPrices[0]))
# if rare > 0:
#     print(str(rare) + "x " + boxNames[1] + " ($" + str(boxPrices[1]) + ")")
#     total += (int(rare) * float(boxPrices[1]))
# if epic > 0:
#     print(str(epic) + "x " + boxNames[2] + " ($" + str(boxPrices[2]) + ")")
#     total += (int(epic) * float(boxPrices[2]))