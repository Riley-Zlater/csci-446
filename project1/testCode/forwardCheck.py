# Written by Riley Slater and Cooper Strahan
# basic backtracking/brute-force approach to solving Sudoku

import forwardCheck as fc

resets = 0

def rBackSolve(puzzle, i, j):
    """
    Fill in the missing cells by checking which values pass the validator
    :param puzzle: 2-D array representing the Sudoku board
    :param i: x coordinate of the empty cell
    :param j: y coordinate of the empty cell
    :rtype: boolean
    """
    global resets
    
    if puzzle.solved() and puzzle.validator():
        fc.displayPuzzle(puzzle)
        return True
    
    if puzzle.getVertex(i,j).getTrueValue()!= 0:
        [i, j] = puzzle.nextEmptySquare(i,j)
        if i == -1 and j == -1:
            return True
        
    target = puzzle.getVertex(i,j)
    if target.numValues()==0:
        return False
    
    valList = [x for x in target.getValueList()]
    for k in valList: #look at
        # Test different k values
        puzzle2 = puzzle.copyGraph()
        puzzle2.getVertex(i, j).setTrueValue(k)
        puzzle2.prune()
        resets += 1
        if not puzzle2.validator(): #if the puzzle is invalid
            target.removeValue(k)
            resets+=1
        elif not rBackSolve(puzzle2, i, j): #if puzzle is valid run rBacksolve on new puzzle and returns if
            target.removeValue(k)
            if puzzle2.getVertex(i,j).numValues == 0:
                return False
        else:
            puzzle=puzzle2
            return True
        if target.numValues() == 0:
            return False

        if puzzle2.solved():
            puzzle = puzzle2
            return True

    [i, j] = puzzle.nextEmptySquare(i,j) #might not be necessary
    if i == -1 and j == -1:
        return True
    else:
        rBackSolve(puzzle, 0, 0)
    return False


def displayPuzzle(puzzle):#we changed
    """
    Simple function to display the finished puzzle and the algorithms performance
    :param puzzle: 2-D array representing the Sudoku board
    :return: prints the board and performance measure, returns nothing
    """
    for row in range(9):
        for col in range(9):
            print(puzzle.getVertex(col, row).getTrueValue(), end=' ')
        print()
    print("\nThe number of backtracks required for this method is", resets)
    return
