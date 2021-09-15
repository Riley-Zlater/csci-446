# Written by Riley Slater and Cooper Strahan

# Basic backtracking/brute-force + forward checking
# approach to solving sudoku problems.

# global var to track performance
resets = 0

def forwardCheck(puzzle, i, j):

    global resets
    
    # if .solved() and .validator() return true, then puzzle is solved/displayed
    if puzzle.solved() and puzzle.validator():
        puzzle.displayGraph()
        return True

    # only get a new vertex if the value of the vurrent vertex is not 0
    if puzzle.getVertex(i, j).getTrueValue() != 0:
        [i, j] = puzzle.nextEmptySquare(i, j)
        if i == -1 and j == -1:
            return True

    # assign var target to current vertex
    target = puzzle.getVertex(i, j)
    if target.numValues() == 0: # if the possible values for the current vertex are 0
        return False  # return false and backtrack

    # assign var valList to hold the possible values for the current vertex
    valList = [x for x in target.getValueList()]
    for k in valList:  # Test different k values where k is an element of the valList
        puzzle2 = puzzle.copyGraph()
        puzzle2.getVertex(i, j).setTrueValue(k)
        puzzle2.prune()  # prune domains of adjacent vertices to the current vertex

        if not puzzle2.validator():  # if the puzzle is invalid remove k from valList
            target.removeValue(k)
            resets += 1  # track number of backtracks
            
        elif not forwardCheck(puzzle2, i, j):  # if puzzle is valid recursively call and continue with backtracking
            target.removeValue(k)  # remove the tested k from the current vertex valList
            if puzzle2.getVertex(i, j).numValues() == 0:  # error handling incase we prune all possible values
                return False
        else:
            puzzle = puzzle2  # update original object
            return True
        if target.numValues() == 0:  # error handling 
            return False

        if puzzle2.solved():  # if the puzzle is solved ubpdate original object
            puzzle = puzzle2
            return True

    [i, j] = puzzle.nextEmptySquare(i, j)  # check for an empty cell again
    if i == -1 and j == -1:
        return True
    else:
        forwardCheck(puzzle, 0, 0)
    return False

