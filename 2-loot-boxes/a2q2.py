# Raven Runner | ©2020 Karl Damus, All Rights Reserved
# Created on October 8, 2020
# a2q1.py


# In this problem, you will modify your previous solution so that we can purchase multiple loot boxes at once.
# 1. Our menu will now need a “Complete Purchase” option to stop purchasing (you can rename this, as long as it is clear)
# 2. Our menu will continue prompting for additional purchases until the selects the Complete Purchase option
# 3. We will need to track how many of ​each type of loot box​ we are purchasing - one variable per type
# 4. If the user selects the same box a second or third time, it should be ​added to the previous amount
# 5. The receipt should contain a list of each box they have purchased; if they did not purchase a type of box, it should not appear on the receipt

import math
import random

# variables
gamerName = ""
boxNames = ["The GeeGee", "The Raven", "The Three-Eyed Raven"]
boxRarity = ["Common", "Rare", "Epic"]
boxPrices = [1.50, 3.00, 7.99]
boxCount = len(boxNames)

cart = []

# functions
# lootbox output
def printLootbox():
    print("\nPlease select a loot box from the menu below:\n")
    i = 0
    while i < boxCount:
        print(str(i + 1) + ". " + "[" + boxRarity[i] + "]" + " (" + str('{:4.2f}'.format(boxPrices[i])) + ") " + boxNames[i])
        i += 1

def errorWrongInput():
    print("\nError: That was not a valid selection. Please enter a number between 1-" + str(boxCount))

def receipt():
    total = float((int(quantity) * float('{:4.2f}'.format(boxPrices[updatedValue]))))
    print("---------------------------------")
    print(str(quantity) + "x " + boxNames[updatedValue] + " ($" + str('{:4.2f}'.format(boxPrices[updatedValue])) + ")")
    print("---------------------------------")
    print ("\nTotal Cost: $" + str(total))
    print("Thank you! Good luck, gamer!\n")

# print ('{:4.2f}'.format'{:4.2f}'.format(boxPrices[0]))

# game start
gamerName = input("\nHELLO, GAMER! Welcome to the Raven Runner Loot Box Purchasing System. First, what's your player name?\n")

selectionMade = False
while selectionMade == False:
    printLootbox()
    selection = input("\n")
    isDigit = selection.isdigit()
    if isDigit == False: 
        errorWrongInput()
    else:
        if int(selection) >= 1 and int(selection) <= boxCount:
            selectionMade = True
            # break
        else:
            errorWrongInput()

# subtract one from selection in order to get corresponding list value [0-2]
updatedValue = int(selection) +- 1
finalized = False
while finalized == False:
    quantity = input("\nHow many of " + boxNames[updatedValue] + "s (" + str('{:4.2f}'.format(boxPrices[updatedValue])) + ") would you like to purchase? ")
    isDigit = quantity.isdigit()
    if isDigit == False:
        print("\nThat is not a quantity. Please type a number of items you wish to purchase.")
    else:
        if int(quantity) > 0:
            finalized = True
        else:
            print("\nThat is not a valid quantity. Please type a number above 0.")

print("\nThanks, " + gamerName + "! Here is your receipt:")
receipt()