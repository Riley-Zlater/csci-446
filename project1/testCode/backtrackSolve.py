# Written by Riley Slater and Cooper Strahan
# basic backtracking/brute-force approach to solving Sudoku

from toolsLib import nextEmptySquare, validator

resets = 0

def recursiveBacktrackSolve(puzzle, i=0, j=0):
    """
    Fill in the missing cells by checking which values pass the validator
    :param puzzle: 2-D array representing the Sudoku board
    :param i: x coordinate of the empty cell
    :param j: y coordinate of the empty cell
    :rtype: boolean
    """
    global resets

    i, j = nextEmptySquare(puzzle)
    if i == -1 and j == -1:
        return True

    for k in range(1, 10):
        # Test different k values
        if validator(puzzle, i, j, k):
            puzzle[i, j] = k

            
            if recursiveBacktrackSolve(puzzle, i, j):
                return True

            # track the number of backtracks
            resets += 1
            # if we get to here it means we had to backtrack
            puzzle[i, j] = 0

    return False



def displayPuzzle(puzzle):
    """
    Simple function to display the finished puzzle and the algorithms performance
    :param puzzle: 2-D array representing the Sudoku board
    :return: prints the board and performance measure, returns nothing
    """
    for row in puzzle:
        print(row)
    print("\nThe number of backtracks required for this method is", resets)
    return
