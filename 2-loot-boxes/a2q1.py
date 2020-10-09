# Raven Runner | ©2020 Karl Damus, All Rights Reserved
# Created on October 8, 2020
# a2q1.py

# You will build the menu that allows the user to buy one or many of a single type of loot box.

# 1. The program starts by asking for the player’s username
# 2. The program shows a menu to the user to purchase one of three loot boxes.
    # Display: The menu must display the number for the option, the rarity, the cost, and the name of the box.
# 3. The user enters a number that corresponds with the loot box they would like to purchase
    # Invalid Inputs: The user is allowed to type incorrect inputs. If they do not type a valid number, 
    # it should print an error message and show the menu again. You can use a while loop to help with this.
# 4. The user is then asked how many of those loot boxes they would like to purchase
# 5. The user is given a personal message, thanking them for their business (using their name), and a receipt is shown for their order.
    # Receipt Info: The receipt should show the loot box name, the number of boxes they purchased, and the total cost of the purchase.

import math
import random

# variables
gamerName = ""
boxNames = ["The GeeGee", "The Raven", "The Three-Eyed Raven"]
boxRarity = ["Common", "Rare", "Epic"]
boxPrices = [1.50, 3.00, 7.99]
boxCount = len(boxNames)

# functions
# lootbox output
def printLootbox():
    print("\nPlease select a loot box from the menu below:\n")
    i = 0
    while i < boxCount:
        print(str(i + 1) + ". " + "[" + boxRarity[i] + "]" + " (" + str(boxPrices[i]) + ") " + boxNames[i])
        i += 1

def errorWrongInput():
    print("\nError: That was not a valid selection. Please enter a number between 1-" + str(boxCount))

# game start
# gamerName = input("\nHELLO, GAMER! Welcome to the Raven Runner Loot Box Purchasing System. First, what's your player name?\n")

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
quantity = input("\nHow many of " + boxNames[updatedValue] + "s (" + str(boxPrices[updatedValue]) + ") would you like to purchase? ")

