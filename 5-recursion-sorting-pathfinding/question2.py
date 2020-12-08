# Recursion, Sorting, & Pathfinding
# Question 2: Cocktail Sort, and Nearest Enemies
# 
# ©2020 Karl Damus, All Rights Reserved
#

import math

# variables used for demonstration as there was no example data given except in the assignment specification pdf
PLAYER = (10,10)
ENEMIES = [(10,20), (55,10), (23,-5), (0,200)]

def main():
    distanceList = distanceCalc(PLAYER, ENEMIES)
    print(cocktailSort(distanceList))

def distanceCalc(hero_position, enemy_positions):
    unsortedDistances = []

    # player position is constant, no need to set it each time in a for loop. << for loop is for list of enemies and is located below
    playerX = hero_position[0]
    playerY = hero_position[1]

    # iterate through list of enemies
    for i in range(len(enemy_positions)):
        # set X and Y coordinates for current enemy
        enemyX = enemy_positions[i][0]
        enemyY = enemy_positions[i][1]
        
        # calculate distance between player and current enemy
        distance = math.sqrt((( enemyX - playerX ) ** 2 ) + (( enemyY - playerY ) ** 2 ))
        
        # push rounded distance to list
        unsortedDistances.append(round(distance,2))
    
    return(unsortedDistances)
    

def cocktailSort(unsortedList):
    sortedList = []
    swapped = True
    length = len(unsortedList)
    start = 0
    end = length - 1

    while swapped == True:
        swapped = False

        # first run will start at index 0 and end at the last index
        for i in range(start, end):
            if unsortedList[i] > unsortedList[i + 1]:
                # swap values
                tempItem = unsortedList[i]
                unsortedList[i] = unsortedList[i + 1]
                unsortedList[i + 1] = tempItem
                swapped = True
        
        if swapped == False:
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if unsortedList[i] > unsortedList[i + 1]:
                # swap values
                tempItem = unsortedList[i]
                unsortedList[i] = unsortedList[i + 1]
                unsortedList[i + 1] = tempItem
                swapped = True
        start = start + 1
    
    # name changed for clarification. once this point of the algorithm has been reached, the list is definitely sorted
    sortedList = unsortedList

    return(sortedList)

if __name__ == '__main__':
    main()