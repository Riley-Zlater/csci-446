
resets = 0

def arc(puzzle, i, j):

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
    for k in valList:
        puzzle2 = puzzle.copyGraph()
        puzzle2.getVertex(i, j).setTrueValue(k)
        puzzle2.arcPrune()

        if not puzzle2.validator():
            target.removeValue(k)
            resets += 1
        elif not arc(puzzle2, i, j):
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
        arc(puzzle, 0, 0)
    return False
