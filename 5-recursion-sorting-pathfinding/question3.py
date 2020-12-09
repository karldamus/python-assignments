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

'''
add 'final route' calculation by implementing the current_point and doing a check once more
use an array throughout to keep track of currentexploration?
it looks like explored is getting reset before the data is output

line is going through #? Why is this
'''

from data import maze_helper as mh

maze = mh.sample_maze()

def main():
    current_point = start_point()
    connected_points = mh.get_adjacent_positions(maze, current_point)
    dfs(connected_points, current_point, explored=[])
    mh.print_maze(maze)

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
                return_point = (i, current_list)
                return return_point
        # fall back if no point found
    return_error("ERROR 1: Start point not found")
    current_list += 1

# this is a 'depth first search' function
def dfs(connected_points, current_point, explored=[]):

    explored.append(current_point)

    for test_point in connected_points:
        for stringValue in test_point:
            isend = mh.symbol_at(maze, current_point)
            if isend == "X":
                print("End of Maze Found!")
                endingFound = True
                remove_wrong_paths(explored)
                break
        endingFound = False
        
        if test_point not in explored and endingFound != True:
            new_point = test_point # renamed for clarity
            new_connected_points = mh.get_adjacent_positions(maze, new_point)
            dfs(new_connected_points, new_point, explored)

def remove_wrong_paths(explored):
    # we found the ending! now lets clean up the paths that we took using recursion
    for i in range(0, len(explored)):
        try:
            test_point_1 = explored[i]
            test_point_2 = explored[i + 1]
        except:
           break
        
        # here we are getting the list of adjacent positions 
        # of two points that are next to eachother in the 'explored list'
        test_adjacent_1 = mh.get_adjacent_positions(maze,test_point_1)
        test_adjacent_2 = mh.get_adjacent_positions(maze,test_point_2)

        # these positions may NOT be adjacent on the actual map
        # we test that here
        for v in test_adjacent_2:
            if v == test_point_1:
                remove = False
                break
            else:
                remove = True
        if remove == True:
            del explored[i]
            # RECURSION
            remove_wrong_paths(explored)
    
    draw_route(explored)

def draw_route(explored):
    finalMaze = maze
    for route_point in range(len(explored)):
        x = explored[route_point][0]
        y = explored[route_point][1]
        if route_point != 0:
            maze[y][x] = "."

if __name__ == '__main__':
    main()