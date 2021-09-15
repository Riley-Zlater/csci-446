# Written by Riley Slater and Cooper Strahan

# global variable to track performance
resets = 0


def recursiveBacktrackSolve(puzzle, i, j) -> bool:
    """
    This function uses the brute-force/backtracking approach to
    solve sudoku.
    :param puzzle: Graph object, 2-D array of vertex objects
    :param i: x index for the current vertex, typically the next empty vertex
    :param j: y index for the current vertex
    :return: boolean
    """
    global resets

    # if .solved() and .validator() return true, then puzzle is solved/displayed
    if puzzle.solved() and puzzle.validator():
        puzzle.displayGraph()
        return True

    # only get a new vertex if the value of the current vertex is not 0
    if puzzle.getVertex(i, j).getTrueValue() != 0:
        [i, j] = puzzle.nextEmptySquare(i, j)
        if i == -1:
            return True

    # assign var current to the current vertex
    current = puzzle.getVertex(i, j)
    # if the possible values for the current vertex are 0
    if current.numValues() == 0:
        return False  # return false and backtrack

    # test values 1-9 for every empty cell in the graph
    for k in range(1, 10):
        puzzle2 = puzzle.copyGraph()
        puzzle2.getVertex(i, j).setTrueValue(k)  # input k to the graph

        # test if that k validates, if not remove k
        if not puzzle2.validator():
            current.removeValue(k)
            resets += 1  # track the number of backtracks

        # if the possible values for the current vertex are 0
        elif not recursiveBacktrackSolve(puzzle2, i, j):
            current.removeValue(k)  # remove the tested k value
            if puzzle2.getVertex(i, j).numValues == 0:  # error handling
                return False
        else:
            puzzle = puzzle2  # update original object
            return True
        if current.numValues() == 0:  # error handling
            return False

        # if the puzzle is solved update original object
        if puzzle2.solved():
            puzzle = puzzle2
            return True

    [i, j] = puzzle.nextEmptySquare(i, j)  # check for another empty cell
    if i == -1 and j == -1:
        return True
    else:
        recursiveBacktrackSolve(puzzle, 0, 0)
    return False
