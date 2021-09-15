# Written by Riley Slater and Cooper Strahan

# global var to track performance
resets = 0


def forwardCheck(puzzle, i, j) -> bool:
    """
    This function uses the forward checking version of the pruning function
    from the Graph object to solve sudoku.
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
        if i == -1 and j == -1:
            return True

    # assign var target to current vertex
    target = puzzle.getVertex(i, j)
    # if the possible values for the current vertex are 0
    if target.numValues() == 0:
        return False  # return false and backtrack

    # assign var valList to hold the possible values for the current vertex
    valList = [x for x in target.getValueList()]
    for k in valList:  # Test different k values where k is an element of the valList
        puzzle2 = puzzle.copyGraph()
        puzzle2.getVertex(i, j).setTrueValue(k)
        puzzle2.prune()  # prune domains of adjacent vertices to the current vertex

        # if the puzzle is invalid remove k from valList
        if not puzzle2.validator():
            target.removeValue(k)
            resets += 1  # track number of backtracks

        # if puzzle is valid recursively call and continue with backtracking
        elif not forwardCheck(puzzle2, i, j):
            target.removeValue(k)  # remove the tested k from the current vertex valList
            # error handling in case we prune all possible values
            if puzzle2.getVertex(i, j).numValues() == 0:
                return False
        else:
            puzzle = puzzle2  # update original object
            return True
        if target.numValues() == 0:  # error handling 
            return False

        # if the puzzle is solved update original object
        if puzzle2.solved():
            puzzle = puzzle2
            return True

    [i, j] = puzzle.nextEmptySquare(i, j)  # check for an empty cell again
    if i == -1 and j == -1:
        return True
    else:
        forwardCheck(puzzle, 0, 0)
    return False
