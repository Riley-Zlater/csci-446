


def arc(variables, domains, constraint1, constraint2):
    pass









##import forwardChecking as fc
##
##def arc(domains):
##    queue = [getArcs()]
##    variablse
##    while not queue.empty():
##        (Xi, Xj) = queue.pop()
##        if (checker(Xi, Xj):
##            if (len(domains[Xi]) == 0):
##                return False
##    for Xk in getNeighborhoodArcs():
##        queue.append((Xk, Xi))
##    return True
##
##def checker(Xi, Xj):
##    Di = 
##    
##def getNeighborhood(Xi):
##    out = []
##    for (x, y) in arcs[Xi]:
##        out.append(y)
##    return out
##
##def getNeighborhoodArcs(i, j):
##    arcs = {}
##    emptyCell = [j, i]
##    topX = (i / 3) * 3
##    topY = (j / 3) * 3
##
##    for x in range(0, 9):
##        if (x != i):
##            arcs[(emptyCell, [j, x])] = 1
##    for y in range(0, 9):
##        if (y != j):
##            arcs[(emptyCell, [y, i])] = 1
##    for x in range(topX, topX+3):
##        for y in range(topY, topY+3):
##            if (x != i or y != j):
##                arcs[(emptyCell, [y, x])] = 1
##    return arcs
##
##def getArcs():
##    out = []
##    for x in range(0, 9):
##        for y in range(0, 9):
##            out += getNeighborhoodArcs(y, x)
##    return out
#https://raw.githubusercontent.com/smallbasic/smallbasic.samples/master/applications/sudoku_solver.bas
