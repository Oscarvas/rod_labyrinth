def exit_reached (labyrinth : list[list[str]], x : int, y : int, horizontal: bool) -> bool:
    """
    This function returns True if the exit of the labyrinth has been reached by the rod 
    by any of its ends, False otherwise.

    x, y are the coordinates of the center of the rod.

    horizontal is True if the rod is horizontal, False if vertical.
    """
    return x + 1 == len(labyrinth[0]) if horizontal else y + 1 == len(labyrinth)

def is_valid_move (labyrinth : list[list[str]], x : int, y : int, horizontal: bool) -> bool:
    """
    This function returns True if the rod can move to the given position, False otherwise.

    x, y are the coordinates of the center of the rod.

    horizontal is True if the rod is horizontal, False if vertical.
    """

    n = len(labyrinth[0])
    m = len(labyrinth)

    if horizontal:
       # checks that the rod is not out of bounds and that the cells are empty
       return 0 <= x < n and 0 < y < m - 1 and not \
            any(labyrinth[x][y + i] == '#' for i in range(-1, 2)) # checks that the rod is not blocked by a wall in any of its positions using the any function
    else:
        # not out of bounds
        return 0 < x < n -1 and 0 <= y < m - 1 and not\
            any(labyrinth[x + i][y] == '#' for i in range(-1, 2)) # no walls

def labyrinth_len (labyrinth : list[list[str]], horizontal: bool) -> int:
    """
    This function checks the length of the labyrinth in the given direction.
    """
    return len(labyrinth[0]) if horizontal else len(labyrinth)


def can_rotate (labyrinth : list[list[str]], x : int, y : int) -> bool:
    """
    This function returns True if the rod can rotate in the given position, False otherwise.

    x, y are the coordinates of the center of the rod.
    """
    n = len(labyrinth[0])
    m = len(labyrinth)

    for i in range(-1, 2):
        for j in range(-1, 2):
            # checks bounds and if the cell is empty
            if not (0 <= x + i < n and 0 <= y + j < m and labyrinth[x + i][y + j] == '.'):
                return False
    return True

def solution (labyrinth : list[list[str]]) -> int:
    """
    This function returns the minimum number of steps to reach the exit of the labyrinth.

    Implementation posibilities:
    - A* search
    - Depth-first search (backtracking)

    A* search is a more efficient algorithm, but it is more difficult to implement.
    Must add a heuristic function to the algorithm considering the capabilities of the rod.

    Depth-first search is easier to figure oute, but it is less efficient.
    """
    return 11


# if __name__ == '__main__':
labyrinth = [
    [".",".","."],
    [".",".","."],
    [".",".","."]
]

#     print(solution(labyrinth))  # Output: 2
print(is_valid_move(labyrinth, 2, 1, True))