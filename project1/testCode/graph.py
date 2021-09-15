# Written by Riley Slater and Cooper Strahan

class Graph:
    def __init__(self, puzzle):
        """
        Constructor for the Graph object.
        :param puzzle: 2-D array of integers/numpy.int32
        """
        self.nextSquare = (0, 0)  # potential starting index
        self.sections = [[0, 3, 0, 3],  # indices of all the 3x3 sections
                         [3, 6, 0, 3],
                         [6, 9, 0, 3],
                         [0, 3, 3, 6],
                         [3, 6, 3, 6],
                         [6, 9, 3, 6],
                         [0, 3, 6, 9],
                         [3, 6, 6, 9],
                         [6, 9, 6, 9]]

        # construct the Graph object as a 2-D array of Vertex objects
        self.puzzle = [[Vertex(puzzle[i][j], (i, j)) for i in range(9)] for j in range(9)]

        # assign [1-9] as the domain of empty cells
        for row in self.puzzle:
            for cell in row:
                if cell.getValueList() == [0]:
                    cell.setValueList([1, 2, 3, 4, 5, 6, 7, 8, 9])

        # make the adjacency list for the 3x3 sections
        for v in range(9):
            for rows in range(self.sections[v][0], self.sections[v][1]):
                for cols in range(self.sections[v][2], self.sections[v][3]):
                    for rows2 in range(self.sections[v][0], self.sections[v][1]):
                        for cols2 in range(self.sections[v][2], self.sections[v][3]):
                            if rows2 != rows or cols2 != cols:
                                self.puzzle[rows][cols].addAdjacent(self.puzzle[rows2][cols2])

        # include the row in the adjacency list
        for row in range(9):
            for col in range(9):
                for col2 in range(9):
                    if col != col2:
                        self.puzzle[row][col].addAdjacent(self.puzzle[row][col2])

        # include the column in the adjacency list
        for col in range(9):
            for row in range(9):
                for row2 in range(9):
                    if row != row2:
                        self.puzzle[row][col].addAdjacent(self.puzzle[row2][col])

    def arcPrune(self):
        """
        This function recursively prunes every Vertex in the Graph
        based on adjacency.
        """
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
        """
        This function only prunes the Vertices adjacent to the current
        Vertex in the Graph.
        """
        pruned = False
        for row in self.puzzle:
            for cell in row:
                if cell.getTrueValue() != 0:
                    for adj in cell.getAdjacent():
                        if adj.removeValue(cell.getTrueValue()):
                            pruned = True

    def getVertex(self, i, j) -> object:
        """
        A getter function for the current Vertex.
        :param i: x index of the current Vertex
        :param j: y index of the current Vertex
        :return: Vertex at position (i, j)
        :rtype: object
        """
        return self.puzzle[i][j]

    def validator(self) -> bool:
        """
        This function tests to see if the current puzzle valid.
        :return: if the puzzle is valid according to the sudoku constraints
        :rtype: boolean
        """
        for row in self.puzzle:
            for cell in row:
                if cell.getTrueValue() != 0:
                    for adj in cell.getAdjacent():
                        if adj.getTrueValue() == cell.getTrueValue():
                            return False
        return True

    def solved(self) -> bool:
        """
        This function tests to see if the whole puzzle is solved.
        :return: if not false, test with the validator
        :rtype: boolean
        """
        for row in self.puzzle:
            for cell in row:
                if cell.getTrueValue() == 0:
                    return False
        return self.validator()

    def nextEmptySquare(self, i, j):
        """
        Find the next empty cell on the puzzle, denoted by 0.
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

    def copyGraph(self) -> object:
        """
        This function copies the current Graph object
        :return: A copy of the current Graph
        :rtype: object
        """
        puzzle2 = Graph([[1 for i in range(9)] for j in range(9)])

        for row in range(9):
            for col in range(9):
                puzzle2.getVertex(row, col).setValueList([x for x in self.puzzle[row][col].getValueList()])
                puzzle2.getVertex(row, col).setTrueValue(self.puzzle[row][col].getTrueValue())
                puzzle2.getVertex(row, col).setCoor((row, col))
        return puzzle2

    def displayGraph(self):
        """
        Simple function to display the current Graph.
        """
        for row in range(9):
            for col in range(9):
                print(self.puzzle[col][row].getTrueValue(), end=' ')
            print()
        return


# Vertex, child class of Graph
class Vertex(Graph):
    def __init__(self, values, coordinates):
        """
        this is the constructor for the Vertex, child object of Graph.
        :param values: potential values the current Vertex could have
        :param coordinates: index of the current Vertex
        """
        self.pValues = [values]
        self.coor = coordinates
        self.adjList = []
        self.tvalue = values

    def setValueList(self, values):
        """
        Setter function for the potential values of the current Vertex.
        :param values: list of integers
        """
        self.pValues = values

    def setTrueValue(self, value):
        """
        Setter function for the true value of the current Vertex.
        :param value: the value that's being tested/the final value for a Vertex
        """
        self.tvalue = value
        for adj in self.adjList:
            adj.removeValue(value)

    def setCoor(self, coordinates):
        """
        A setter function for setting the coordinates of a Vertex.
        :param coordinates: (x, y) coordinates, 2-tuple
        """
        self.coor = coordinates

    def getValueList(self) -> list:
        """
        A getter function for getting the potential values of a Vertex.
        :return: the potential values for the Vertex
        :rtype: list
        """
        return self.pValues

    def getTrueValue(self) -> int:
        """
        Getter function the gets the true value of the current Vertex.
        :return: the true value of the Vertex
        :rtype: int
        """
        return self.tvalue

    def getCoordinates(self) -> tuple:
        """
        Getter function for getting the coordinates of the Vertex.
        :return: (x, y) coordinate of the Vertex
        :rtype: tuple
        """
        return self.coor

    def numValues(self) -> int:
        """
        Getter function for getting the number of potential values of the Vertex.
        :return: the length of the potential values list
        :rtype: int
        """
        return len(self.pValues)

    def removeValue(self, k) -> bool:
        """
        Remove the value k from the potential values of the Vertex.
        :param k: tested value
        :return: after removing the values
        :rtype: boolean
        """
        removed = False
        for vals in self.pValues:
            if vals == k:
                self.pValues.remove(k)
                removed = True
        if self.tvalue == 0 and len(self.pValues) == 1:
            self.tvalue = self.pValues[0]
        return removed

    def addAdjacent(self, vertex):
        """
        This function adds Vertices to the adjacency list.
        :param vertex: Vertex object to append to the adjacency list
        """
        self.adjList.append(vertex)

    def getAdjacent(self) -> list:
        """
        This function gets the adjacency list for the current Vertex.
        :return: the adjacency list of the Vertex
        :rtype: list
        """
        return self.adjList
