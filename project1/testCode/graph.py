class Graph:
    def __init__(self, puzzle):
        self.nextSquare = (0, 0)
        self.sections = [[0, 3, 0, 3],
                         [3, 6, 0, 3],
                         [6, 9, 0, 3],
                         [0, 3, 3, 6],
                         [3, 6, 3, 6],
                         [6, 9, 3, 6],
                         [0, 3, 6, 9],
                         [3, 6, 6, 9],
                         [6, 9, 6, 9]]

        self.puzzle = [[Vertex(puzzle[i][j], (i, j)) for i in range(9)] for j in range(9)]
        for row in self.puzzle:
            for cell in row:
                if cell.getValueList() == [0]:
                    cell.setValueList([1, 2, 3, 4, 5, 6, 7, 8, 9])
        for v in range(9):
            for rows in range(self.sections[v][0], self.sections[v][1]):
                for cols in range(self.sections[v][2], self.sections[v][3]):
                    for rows2 in range(self.sections[v][0], self.sections[v][1]):
                        for cols2 in range(self.sections[v][2], self.sections[v][3]):
                            if rows2 != rows or cols2 != cols:
                                self.puzzle[rows][cols].addAdjacent(self.puzzle[rows2][cols2])

        for row in range(9):
            for col in range(9):
                for col2 in range(9):
                    if col != col2:
                        self.puzzle[row][col].addAdjacent(self.puzzle[row][col2])

        for col in range(9):
            for row in range(9):
                for row2 in range(9):
                    if row != row2:
                        self.puzzle[row][col].addAdjacent(self.puzzle[row2][col])

    def arcPrune(self):
        pruned = False
        for row in self.puzzle:
            for cell in row:
                if cell.getTrueValue() != 0:
                    for adj1 in cell.getAdjacent():
                        if adj1.removeValue(cell.getTrueValue()):
                            pruned = True

        if pruned:
            self.arcPrune()

    def prune(self):
        pruned = False
        for row in self.puzzle:
            for cell in row:
                if cell.getTrueValue() != 0:
                    for adj in cell.getAdjacent():
                        if adj.removeValue(cell.getTrueValue()):
                            pruned = True

    def getVertex(self, i, j):
        return self.puzzle[i][j]

    def validator(self):
        for row in self.puzzle:
            for cell in row:
                if cell.getTrueValue() != 0:
                    for adj in cell.getAdjacent():
                        if adj.getTrueValue() == cell.getTrueValue():
                            return False
        return True

    def solved(self):
        for row in self.puzzle:
            for cell in row:
                if cell.getTrueValue() == 0:
                    return False
        return self.validator()

    def nextEmptySquare(self, i, j):
        """
        Find the next empty cell on the puzzle, denoted by 0
        :return: The (x, y) coordinate of the empty cell
        :rtype: int, 2-tuple
        """
        for x in range(i, 9):
            for y in range(0, 9):
                if x != i or y > j:
                    if self.puzzle[x][y].getTrueValue() == 0:
                        return x, y
        for x in range(0, i):
            for y in range(0, 9):
                if x < i or y <= j:
                    if self.puzzle[x][y].getTrueValue() == 0:
                        return x, y
        return -1, -1

    def copyGraph(self):
        puzzle2 = Graph([[1 for i in range(9)] for j in range(9)])

        for row in range(9):
            for col in range(9):
                puzzle2.getVertex(row, col).setValueList([x for x in self.puzzle[row][col].getValueList()])
                puzzle2.getVertex(row, col).setTrueValue(self.puzzle[row][col].getTrueValue())
                puzzle2.getVertex(row, col).setCoor((row, col))
        return puzzle2

    def displayGraph(self):
        for row in range(9):
            for col in range(9):
                print(self.puzzle[col][row].getTrueValue(), end=' ')
            print()
        return


class Vertex(Graph):
    def __init__(self, values, coordinates):
        self.pValues = [values]
        self.coor = coordinates
        self.adjList = []
        self.tvalue = values

    def setValueList(self, values):
        self.pValues = values

    def setTrueValue(self, value):
        self.tvalue = value
        for adj in self.adjList:
            adj.removeValue(value)

    def setCoor(self, coordinates):
        self.coor = coordinates

    def getValueList(self):
        return self.pValues

    def getTrueValue(self):
        return self.tvalue

    def getCoordinates(self):
        return self.coor

    def numValues(self):
        return len(self.pValues)

    def removeValue(self, k):
        removed = False
        for vals in self.pValues:
            if vals == k:
                self.pValues.remove(k)
                removed = True
        if self.tvalue == 0 and len(self.pValues) == 1:
            self.tvalue = self.pValues[0]
        return removed

    def addAdjacent(self, vertex):
        self.adjList.append(vertex)

    def getAdjacent(self):
        return self.adjList
