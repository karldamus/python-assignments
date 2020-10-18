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
def printLootbox():
    print("\nPlease select a loot box from the menu below:\n")
    i = 0
    while i < boxCount:
        print(str(i + 1) + ". " + "[" + boxRarity[i] + "]" + " (" + str('{:4.2f}'.format(boxPrices[i])) + ") " + boxNames[i])
        i += 1
    i += 1
    print(str(i) + ". Complete Purchase")
def errorWrongInput():
    print("\nError: That was not a valid selection. Please enter a number between 1-" + str(boxCount))

def receipt():
    c = 0
    total = []
    print("---------------------------------")
    while c < (len(cart)):
        print(str(cart[c + 2]) + "x " + cart[c] + " ($" + str(cart[c + 1]) + ")")
        total.append(float(cart[c + 1]))
        c += 3
    print("---------------------------------")
    print ("\nTotal Cost: $" + str(sum(total)))
    print("Thank you! Good luck, gamer!\n")

def addToCart():
    cart.append(boxNames[updatedValue])
    cart.append(str('{:4.2f}'.format(boxPrices[updatedValue])))
    cart.append(int(quantity))

# print ('{:4.2f}'.format'{:4.2f}'.format(boxPrices[0]))

# game start
gamerName = input("\nHELLO, GAMER! Welcome to the Raven Runner Loot Box Purchasing System. First, what's your player name?\n")

userFinished = False
while userFinished == False:
    printLootbox()
    selection = input("\n")
    isDigit = selection.isdigit()
    if isDigit == False: 
        errorWrongInput()
    else:
        if int(selection) >= 1 and int(selection) <= boxCount:
            
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
                        addToCart()
                        finalized = True
                    else:
                        print("\nThat is not a valid quantity. Please type a number above 0.")
                        
        elif int(selection) == 4:
            userFinished = True
            break
        else:
            errorWrongInput()

print("\nThanks, " + gamerName + "! Here is your receipt:\n")
receipt()