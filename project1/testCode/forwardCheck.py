# Written by Riley Slater and Cooper Strahan
# basic backtracking/brute-force approach to solving Sudoku


resets = 0

def forwardCheck(puzzle, i, j):

    global resets
    
    if puzzle.solved() and puzzle.validator():
        puzzle.displayGraph()
        return True
    
    if puzzle.getVertex(i, j).getTrueValue() != 0:
        [i, j] = puzzle.nextEmptySquare(i, j)
        if i == -1 and j == -1:
            return True
        
    target = puzzle.getVertex(i, j)
    if target.numValues() == 0:
        return False
    
    valList = [x for x in target.getValueList()]
    for k in valList:  # look at
        # Test different k values
        puzzle2 = puzzle.copyGraph()
        puzzle2.getVertex(i, j).setTrueValue(k)
        puzzle2.prune()

        if not puzzle2.validator():  # if the puzzle is invalid
            target.removeValue(k)
            resets += 1
        elif not forwardCheck(puzzle2, i, j):  # if puzzle is valid run forwarCheck on new puzzle and returns if
            target.removeValue(k)
            if puzzle2.getVertex(i, j).numValues() == 0:
                return False
        else:
            puzzle = puzzle2
            return True
        if target.numValues() == 0:
            return False

        if puzzle2.solved():
            puzzle = puzzle2
            return True

    [i, j] = puzzle.nextEmptySquare(i, j)  # might not be necessary
    if i == -1 and j == -1:
        return True
    else:
        forwardCheck(puzzle, 0, 0)
    return False

