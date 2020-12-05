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

PLAYER = (10,10)
ENEMY = (5,2)