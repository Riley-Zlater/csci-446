


domains = [[6, 6, {1, 3, 4, 7}], [6, 7, {1, 3, 4, 7}], [7, 6, {1, 3, 4, 7}], [8, 6, {1, 3, 4, 7}]]

def arc(puzzle, domains):
    variables = [[x[0], x[1]] for x in domains]
    domains = [[x[3]] for x in domains]

def getNeighborhood(i, j):
    arcs = {}
    emptyCell = [j, i]
    topX = (i / 3) * 3
    topY = (j / 3) * 3

    for x in range(0, 9):
        if (x != i):
            arcs[(emptyCell, [j, x])] = 1
#https://raw.githubusercontent.com/smallbasic/smallbasic.samples/master/applications/sudoku_solver.bas
