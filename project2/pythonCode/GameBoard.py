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
            self.setStates(size, pitp, wumpusp, obstp)

    @staticmethod
    def makeWorld(dim):
        return [[Cell(i, j) for i in range(0, dim)] for j in range(0, dim)]
    
    def getCell(self, pos):
        i = pos[0] 
        j = pos[1]
        return self.board[i][j]

    def setStates(self, size, pitp, wumpusp, obstp):  # use the probabilities to change the states of the cells
        probP = floor((size ** 2) * pitp)
        probW = floor((size ** 2) * wumpusp)
        probO = floor((size ** 2) * obstp)

        while probO > 0:
            i = ran.randint(0, size-1)
            j = ran.randint(0, size-1)
            self.board[i][j].setStateObs()
            probO -= 1

        while probP > 0:
            i = ran.randint(0, size-1)
            j = ran.randint(0, size-1)
            while self.board[i][j].getState()['Obstacle'] == True:
                i = ran.randint(0, size-1)
                j = ran.randint(0, size-1)
            
            if (self.board[i][j].getState()['Obstacle'] == False):
                self.board[i][j].setStatePit()
                for cell in self.board[i][j].getAdjList():
                    self.board[i][j].setStateBreeze()
                probP -= 1

        while probW > 0:
            i = ran.randint(0, size-1)
            j = ran.randint(0, size-1)
            while self.board[i][j].getState()['Obstacle'] == True or self.board[i][j].getState()['Pit'] == True:
                i = ran.randint(0, size-1)
                j = ran.randint(0, size-1)
            
            if self.board[i][j].getState()['Obstacle'] == False and self.board[i][j].getState()['Pit'] == False:
                self.board[i][j].setStateWumpus()
                for cell in self.board[i][j].getAdjList():
                    self.board[i][j].setStateStench()
                probW -= 1

    def setAdjList(self, size):  # this fn will make the adjacency lists for each cell
        for i in range(0, size):  # if current cell is (2, 2) adjList: [(1, 2), (2, 1), (3, 2), (2, 3)]
            for j in range(0, size):
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
                if self.getCell([i,j]).getState()['Wumpus']:
                    print('W', end='      ')
                elif self.getCell([i,j]).getState()['Pit']:
                    print('P', end='     ')
                elif self.getCell([i,j]).getState()['Gold']:
                    print('G', end='     ')
                else:
                    print(self.board[i][j].getIndex(), end=' ')
            print()
        return


class Cell(GameBoard):
    def __init__(self, i, j):
        self.index = [i, j]
        self.adjList = []
        self.visited = False
        self.state = {'Pit': False, 'Wumpus': False, 'Obstacle': False,
                      'Breeze': False, 'Stench': False, 'potP': False,
                      'potW': False, 'Gold': False}

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
    
    def setStateNoPotPit(self):
        self.state['potP'] = False
    
    def selfStateNoPotW(self):
        self.state['potW'] = False

    def setStatePotPit(self):
        for cell in self.getAdjList():
            if cell.visted == False:
                cell.state['potP'] = True
            
    def setStatePotWumpus(self):
        for cell in self.getAdjList():
            if cell.visited == False:
                cell.state['potW'] = True
    
    def removeAdjStatePotPit(self):
        for cell in self.getAdjList():
            cell.state['potP'] = False
            
    def removeAdjStatePotWumpus(self):
        for cell in self.getAdjList():
            cell.state['potW'] = False

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
