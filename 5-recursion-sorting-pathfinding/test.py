from data import maze_helper as mh

maze = mh.sample_maze()
# mh.print_maze(maze)
for i in range(len(maze)):
    print(str(i) + ": " + str(maze[i]))

def main():
    # current_point = start_point()
    current_point = (3,7)
    print(current_point)
    adjacent_points = mh.get_adjacent_positions(maze, current_point)
    print(adjacent_points)

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

if __name__ == '__main__':
    main()
