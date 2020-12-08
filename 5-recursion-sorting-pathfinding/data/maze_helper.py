def sample_maze():
    """Return a single, sample maze that you can use for testing.

    Returns:
        list: Returns a 2D list of strings, each string is a wall("#"), start("O"), end("X"), or empty(" ")
    """
    maze = []
    # maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    # maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    # maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    # maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    # maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    # maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    # maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    # maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    # maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    maze.append(["#","O", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", " ", "#", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])
    
    return maze

def get_adjacent_positions(maze, position):
    """Return a list of all non-wall symbols surrounding the position in the maze (up/down/left/right).

    Args:
        maze (list): The 2D list of string symbols, as seen in the sample_maze() function
        position (tuple): A tuple containing the x, y position of the cell we are looking at.

    Returns:
        list: A list of tuples, each tuple representing a valid position that can be moved to.
    """
    # These poses represent up/down/left/right
    poses = [ (-1, 0), (0,1), (1, 0), (0, -1) ]
    locations = []

    # Use a loop to check each of the four possible positions
    for pose in poses:
        # Setup a new position that will represent where we need to look
        new_pose = (pose[0]+position[0], pose[1]+position[1])
        in_bounds = (-1 < new_pose[0] < len(maze[0])) and (-1 < new_pose[1] < len(maze))
        valid_spot = in_bounds and symbol_at(maze, new_pose) != "#"
        
        if in_bounds and valid_spot:
            locations.append(new_pose)

    return locations

def symbol_at(maze, position):
    """Return the string in the maze, given the position.

    Args:
        maze (list): The 2D list of string symbols, as seen in the sample_maze() function
        position (tuple): A tuple containing the x, y position of the cell we are trying to get the symbol for.

    Returns:
        str: The single character string representing the maze feature; either wall ("#"), floor(" "), start ("O") or exit ("X")
    """
    return maze[position[1]][position[0]]

def add_walk_symbol(maze, position):
    """Updates the maze data so that the cell at the given position is considered part of the valid path to the exit.

    Args:
        maze (list): The 2D list of string symbols, as seen in the sample_maze() function
        position (tuple): A tuple containing the x, y position of the cell we are trying to visualize as part of the valid path
    """
    maze[position[1]][position[0]] = "."

def print_maze(maze):
    """Prints the maze in a readable way, with some spacing between each horizontal character.

    Args:
        maze (list): The 2D list of string symbols, as seen in the sample_maze() function
    """
    for i, row in enumerate(maze):
        for j, col in enumerate(maze):
            print(symbol_at(maze, (j, i)), end="   ")
        print()  
