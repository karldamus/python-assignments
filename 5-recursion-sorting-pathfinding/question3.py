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
# mh.print_maze(maze)

wall = "#"
player = "O"
end = "X"
space = " "

def main():
    current_point = start_point()
    connected_points = mh.get_adjacent_positions(maze, current_point)
    dfs(connected_points, current_point, explored=[])
    # print("The current point is: " + str(current_point) + ". The connected points are: " + str(connected_points))

def return_error(message):
    print(message)

def start_point():
    # reset current list to search in
    current_list = 0
    # go through each list inside the maze list
    for lists in maze:
        for i in range(len(lists)):
            # if "O" is the value, it is the start position!
            if lists[i] == "O":
                return_point = (current_list, i)
                return return_point
        # fall back if no point found
        return_error("ERROR 1: Start point not found")
        current_list += 1
    
# print(maze)
def dfs(connected_points, current_point, explored=[]):
    endingFound = False
    explored.append(current_point)
    # print("The current explored points are: " + str(explored))
    for new_current_point in connected_points:
        for i in new_current_point:
            isend = mh.symbol_at(maze, current_point)
        if isend == "X":
            print("Ending Found!")
            endingFound = True
            print("The current point is: " + str(current_point))
            print("The explored pathways are: " + str(explored))
            break

        if new_current_point not in explored and endingFound == False:
            explored.append(new_current_point)
            new_connected_points = mh.get_adjacent_positions(maze, new_current_point)
            dfs(new_connected_points, new_current_point, explored)
    # if endingFound == False:
    #     print("No ending was found. Maybe it's an impossible maze OoO")
        
    # print(explored)

if __name__ == '__main__':
    main()
