# Written by Riley Slater and Cooper Strahan
# basic backtracking/brute-force approach to solving Sudoku


resets = 0

def recursiveBacktrackSolve(puzzle, i, j):

    global resets

    if puzzle.solved() and puzzle.validator():
        puzzle.displayGraph()
        return True

    if puzzle.getVertex(i, j).getTrueValue() != 0:
        [i, j] = puzzle.nextEmptySquare(i, j)
        if i == -1:
            return True

    current = puzzle.getVertex(i, j)
    if current.numValues() == 0:
        return False

    for k in range(1, 10):
        puzzle2 = puzzle.copyGraph()

        puzzle2.getVertex(i, j).setTrueValue(k)

        if not puzzle2.validator():
            current.removeValue(k)
            resets += 1
        elif not recursiveBacktrackSolve(puzzle2, i, j):
            current.removeValue(k)
            if puzzle2.getVertex(i, j).numValues == 0:
                return False
        else:
            puzzle = puzzle2
            return True
        if current.numValues() == 0:
            return False

        if puzzle2.solved():
            puzzle = puzzle2
            return True

    [i, j] = puzzle.nextEmptySquare(i,j) # might not be necessary
    if i == -1 and j == -1:
        return True
    else:
        recursiveBacktrackSolve(puzzle, 0, 0)
    return False
