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
# mh.print_maze(maze)

wall = "#"
player = "O"
end = "X"
space = " "

def main():
    current_point = start_point()
    connected_points = mh.get_adjacent_positions(maze, current_point)
    print(dfs(connected_points, current_point, explored=[]))
    mh.print_maze(maze)
    # for i in maze:
    #     print(i)
    # print(route)
    # draw_path(route)

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

def dfs(connected_points, current_point, explored=[]):

    explored.append(current_point)

    for test_point in connected_points:
        # print(test_point)
        for stringValue in test_point:
            isend = mh.symbol_at(maze, current_point)
            if isend == "X":
                print("End of Maze Found!")
                endingFound = True
                draw_route(explored)
                break
        endingFound = False
        if test_point not in explored and endingFound != True:
            new_point = test_point # rename for clarity
            # explored.append(new_point)
            new_connected_points = mh.get_adjacent_positions(maze, new_point)
            print(new_connected_points)
            dfs(new_connected_points, new_point, explored)
    
    # try:
    #     if endingFound == True:
    #         for route_point in explored:
    #             x = route_point[1]
    #             y = route_point[0]
    #             maze[y][x] = "."
    # except:
    #     pass

def draw_route(explored):
    print(explored)
    for route_point in explored:
        x = route_point[1]
        y = route_point[0]
        maze[y][x] = "."

    
    # try:
    #     print(explorationOutput)
    #     return explorationOutput
    # except:
    #     pass
    # if endingFound == False:
    #     print("No ending was found. Maybe it's an impossible maze OoO")
        
    # print(explored)

def draw_path(finalized_exploration):
    # for v in range(len(finalized_exploration)):
    #     print("test")
    #     print(point)
    #     print(point_to_draw)
    pass


if __name__ == '__main__':
    main()
