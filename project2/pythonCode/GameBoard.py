# Written by Riley Slater and Cooper Strahan
from math import ceil


class GameBoard:
    def __init__(self, size, pitp=0, wumpusp=0, obstp=0):
        self.size = size + 1
        self.pitp = pitp
        self.wumpusp = wumpusp
        self.obstp = obstp

        self.board = self.makeWorld(self.size)

        # self.setAdjList(size)

    @staticmethod
    def makeWorld(dim):
        return [[Cell(i, j) for i in range(1, dim)] for j in range(1, dim)]

    def getCell(self, i, j):
        return self.board[i][j]

    # TODO
    def setStates(self, size, pitp, wumpusp, obstp):  # use the probabilities to change the states of the cells
        numPits, numWumpus, numObstacles = 0

        numPits = ceil(size * pitp)
        numWumpus = ceil(size * wumpusp)
        numObstacles = ceil(size * obstp)

        self.setAdjList(size)

    # TODO
    def setAdjList(self, size):  # this fn will make the adjacency lists for each cell
        for col in range(size):  # if current cell is (2, 2) adjList: [(1, 2), (2, 1), (3, 2), (2, 3)]
            for row in range(size):
                for row2 in range(size):
                    for col2 in range(size):
                        pass

    def displayBoard(self, dim):  # simple display fn
        for i in range(dim):
            for j in range(dim):
                print(self.board[i][j].getIndex(), end=' ')
            print()
        return


class Cell(GameBoard):
    def __init__(self, i, j):
        self.index = (i, j)
        self.adjList = []
        self.state = {'Pit': False, 'Wumpus': False, 'Obstacle': False,
                      'Breeze': False, 'Stench': False}  # Maybe leave the dict empty when initializing

    def getIndex(self):  # returns the current index as (col, row)
        return self.index

    # TODO
    def setState(self, numPits, numWumpus, numObstacles):  # this fn will change the state of the current cell
        pitCounter, wumpusCounter, obstacleCounter = 0

    def getState(self):  # return this cells state
        return self.state

    def addAdjacent(self, cell):  # add a cell to the adjacency list of the current cell
        self.adjList.append(cell)

    def getAdjList(self):  # return the adjacency list of the current cell
        return self.adjList
