# Recursion, Sorting, & Pathfinding
# Question 2: Searching for an Exit
# 
# ©2020 Karl Damus, All Rights Reserved
#

'''
In a file named ​question3.py​, include a function called ​
dfs(list(list(string)), tuple(int, int), list(tuple(int, int)) = []),​ 
or as a more simple example of what it might look like in code: dfs(maze, position, explored=[])​.
You will need to make use of the functions provided to you to take in some maze and print the maze, 
with a valid path from the start to end. It does not need to be the shortest path. 
​Be careful​ to review the functions that have already been written for you so you do not do unnecessary work.
'''

from data import maze_helper as mh

maze = mh.sample_maze()
mh.print_maze(maze)

wall = "#"
player = "O"
end = "X"
space = " "



