# Recursion, Sorting, & Pathfinding
# Question 2: Cocktail Sort, and Nearest Enemies
# 
# ©2020 Karl Damus, All Rights Reserved
#
'''
Write a function, ​closest_enemies(tuple(int,int), list(tuple(int,int)))​. 
This signature is a bit complex, 
but really, it could look as simple as 
​def closest_enemies(hero_position, enemy_positions):

As parameters, the function accepts:
    ● A tuple, containing two integers, 
    representing the x, y coordinate of our player character
        ○ Ex. (50, 10), (20, 35)
    ● A list of tuples, each tuple containing two integers, 
    representing enemy positions
        ○ Ex. [ (10, 20), (55, 10), (23, -5), (0, 200) ]
'''

import math
import random

PLAYER = (10,10)
ENEMIES = [(10,20), (55,10), (23,-5), (0,200)]
ENEMY = (23,-5)
testList = []

for i in range(20):
    testList.append(random.randint(0,30))

def main():
    # print(cocktailSort(testList))
    distanceList = distanceCalc(PLAYER, ENEMY)
    print(cocktailSort(distanceList))

def distanceCalc(hero_position, enemy_positions):
    unsortedDistances = []

    playerX = PLAYER[0]
    playerY = PLAYER[1]

    # iterate through list of enemies
    for i in range(len(ENEMIES)):
        # set X and Y coordinates for current enemy
        enemyX = ENEMIES[i][0]
        enemyY = ENEMIES[i][1]
        
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
                tempItem = unsortedList[i]
                unsortedList[i] = unsortedList[i + 1]
                unsortedList[i + 1] = tempItem
                swapped = True
        start = start + 1
    
    sortedList = unsortedList

    return(unsortedList)

if __name__ == '__main__':
    main()