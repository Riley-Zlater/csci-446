# Written by Riley Slater and Cooper Strahan
from math import floor
import random as ran


class GameBoard:
    def __init__(self, size, pitp=0, wumpusp=0, obstp=0):
        self.size = size
        self.pitp = pitp
        self.wumpusp = wumpusp
        self.obstp = obstp

        self.board = self.makeWorld(self.size)
        self.setAdjList(self.size)

        if pitp != 0 and wumpusp != 0 and obstp != 0:
            self.setStates(size+1, pitp, wumpusp, obstp)

    @staticmethod
    def makeWorld(dim):
        out = [[]]
        for i in range(1, dim+1):
            print(i)
            for j in range(1, dim+1):
                print(j)
                out[i][j] = Cell(i, j)
        return out #[[Cell(i, j) for i in range(1, dim+1)] for j in range(1, dim+1)]

    def getCell(self, i, j):
        return self.board[i][j]
    
    def getCell(self, pos):
        i = pos[0] 
        j = pos[1]
        return self.board[i][j]

    def setStates(self, size, pitp, wumpusp, obstp):  # use the probabilities to change the states of the cells
        probP = floor((size ** 2) * pitp)
        probW = floor((size ** 2) * wumpusp)
        probO = floor((size ** 2) * obstp)

        while probO > 0:
            i = ran.randint(1, size)
            j = ran.randint(1, size)
            self.board[i][j].setStateObs()
            probO -= 1

        while probP > 0:
            i = ran.randint(1, size)
            j = ran.randint(1, size)
            while self.board[i][j].getState()['Obstacle'] == True:
                i = ran.randint(1, size)
                j = ran.randint(1, size)
            
            if (self.board[i][j].getState()['Obstacle'] == False):
                self.board[i][j].setStatePit()
                for cell in self.board[i][j].getAdjList():
                    self.board[i][j].setStateBreeze()
                probP -= 1

        while probW > 0:
            i = ran.randint(1, size)
            j = ran.randint(1, size)
            while self.board[i][j].getState()['Obstacle'] == True or self.board[i][j].getState()['Pit'] == True:
                i = ran.randint(1, size)
                j = ran.randint(1, size)
            
            if self.board[i][j].getState()['Obstacle'] == False and self.board[i][j].getState()['Pit'] == False:
                self.board[i][j].setStateWumpus()
                for cell in self.board[i][j].getAdjList():
                    self.board[i][j].setStateStench()
                probW -= 1

    def setAdjList(self, size):  # this fn will make the adjacency lists for each cell
        for i in range(1, size+1):  # if current cell is (2, 2) adjList: [(1, 2), (2, 1), (3, 2), (2, 3)]
            for j in range(1, size+1):
                if i + 1 < size:
                    self.board[i][j].addAdjacent(self.board[i+1][j])
                if i - 1 > 0:
                    self.board[i][j].addAdjacent(self.board[i-1][j])
                if j + 1 < size:
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
                      'Breeze': False, 'Stench': False, 'potP': False,
                      'potW': False}  # Maybe leave the dict empty when initializing

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

    def setStatePotPit(self):
        for cell in self.getAdjList():
            if cell.visted == False:
                cell.state['potP'] = True
            
    def setStatePotWumpus(self):
        for cell in self.getAdjList():
            if cell.visited == False:
                cell.state['potW'] = True

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
