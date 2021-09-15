#Written by Riley Slater and Cooper Strahan


def nextEmptySquare(puzzle):
    """
    Find the next empty cell on the puzzle, denoted by 0
    :param puzzle: 2-D array representing the Sudoku board
    :return: The (x, y) coordinate of the empty cell
    :rtype: int, 2-tuple
    """
    for x in range(0, 9):
        for y in range(0, 9):
            if puzzle[x][y] == 0:
                return x, y
    return -1, -1


def validator(puzzle, i, j, k):
    """
    Check for duplicates of k in the row, column, and 3x3 section
    of the empty cell
    :param puzzle: 2-D array representing the Sudoku board
    :param i: x coordinate of the empty cell
    :param j: y coordinate of the empty cell
    :param k: integer that is being tested in the empty cell
    :return: True or False depending on if k validates
    :rtype: boolean
    """
    # Checks row
    rowCheck = True
    for v in range(9):
        if k == puzzle[i][v]:
            rowCheck = False
    if rowCheck:
        # Checks column if row passes
        columnCheck = True
        for v in range(9):
            if k == puzzle[v][j]:
                columnCheck = False 
        if columnCheck:
            # check 3x3 sector if row and column pass
            # Top left coords of the sector containing x, y
            topX = 3 * (i // 3)
            topY = 3 * (j // 3)
            for x in range(topX, topX + 3):
                for y in range(topY, topY + 3):
                    if puzzle[x][y] == k:
                        return False
            return True
    return False



