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
        return

    def setAdjList(self, size):  # this fn will make the adjacency lists for each cell
        for i in range(size):  # if current cell is (2, 2) adjList: [(1, 2), (2, 1), (3, 2), (2, 3)]
            for j in range(size):
                if i + 1 <= size:
                    self.board[i][j].addAdjacent(self.board[i+1][j])
                if i - 1 > 0:
                    self.board[i][j].addAdjacent(self.board[i-1][j])
                if j + 1 <= size:
                    self.board[i][j].addAdjacent(self.board[i][j+1])
                if j - 1 > 0:
                    self.board[i][j].addAdjacent(self.board[i][j-1])

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
        self.visited = False
        self.state = {'Pit': False, 'Wumpus': False, 'Obstacle': False,
                      'Breeze': False, 'Stench': False}  # Maybe leave the dict empty when initializing

    def getIndex(self):  # returns the current index as (col, row)
        return self.index

    def setStatePit(self):
        self.state['Pit'] = True

    def setStateObs(self):
        self.state['Obstacle'] = True

    def setStateWumpus(self):
        self.state['Wumpus'] = True
    
    def setStateBreeze(self):
        self.state['Breeze'] = True

    def setStateStench(self):
        self.state['Stench'] = True

    def getState(self):  # return this cells state
        return self.state

    def addAdjacent(self, cell):  # add a cell to the adjacency list of the current cell
        self.adjList.append(cell)

    def getAdjList(self):  # return the adjacency list of the current cell
        return self.adjList
    
    def getVisited(self):
        return self.visited
    
    def setVisited(self):
        self.visited = True
