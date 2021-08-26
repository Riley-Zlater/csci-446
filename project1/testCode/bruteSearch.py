# https://stackoverflow.com/questions/1697334/algorithm-for-solving-sudoku


# Find the next empty square on the puzzle
def findNextEmpty(puzzle):
    # Look for an empty location in the puzzle
    for x in range(0, 9):
        for y in range(0, 9):
            if puzzle[x][y] == 0:
                return x, y
    return -1, -1


# Check and see if the empty square can be the arbitrary value k
def validator(puzzle, i, j, k):
    rowCheck = all([k != puzzle[i][x] for x in range(9)])
    if rowCheck:
        columnCheck = all([k != puzzle[x][j] for x in range(9)])
        if columnCheck:
            # Top left coords of the sector containing x, y
            topX, topY = 3 * (i // 3), 3 * (j // 3)
            for x in range(topX, topX + 3):
                for y in range(topY, topY + 3):
                    if puzzle[x][y] == k:
                        return False
            return True
    return False


# Fill in the missing squares through brute-force
def bruteSolve(puzzle, i=0, j=0):

    i, j = findNextEmpty(puzzle)
    if i == -1:
        return True

    for k in range(1, 10):
        # Test different k values
        if validator(puzzle, i, j, k):
            puzzle[i][j] = k
            if bruteSolve(puzzle, i, j):
                return True

            puzzle[i][j] = 0

    return False


def displayPuzzle(puzzle):
    for row in puzzle:
        print(row)
    return


