# Written by Riley Slater and Cooper Strahan
from math import floor
import random as ran

"""
*This class object represents the game board as a whole.
*It has a given size and given probabilities of generating
*a Wumpus, pit or obstacle on the board.
"""
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
        """
        *This method constructs the N x N board of Cells.
        @param dim The size of the board, N, int
        @return 2D array of Cell objects
        """
        return [[Cell(i, j) for i in range(0, dim)] for j in range(0, dim)]
    
    
    def getCell(self, pos):
        """
        *This getter method returns the cell at the given position.
        @param pos The [i, j] indicies of the current cell, list
        @return Cell object at position (i, j)
        """
        i = pos[0] 
        j = pos[1]
        return self.board[i][j]
    
    def getSize(self):
        """
        *This method returns the size of the board.
        @return The board size, int
        """
        return self.size

    def setStates(self, size, pitp, wumpusp, obstp):
        """
        *This method uses random distribution to assign the states of each Cell.
        @param size The size of the board, int
        @param pitp The probability of a pit, float, given in main.py
        @param wumpusp The probability of a Wumpus, float, given in main.py
        @param obstp The probability of a obstacle, float, given in main.py
        """
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
            while self.board[i][j].state['Obstacle']:
                i = ran.randint(0, size-1)
                j = ran.randint(0, size-1)
            
            if not (self.board[i][j].state['Obstacle']):
                self.board[i][j].setStatePit()
                for cell in self.board[i][j].getAdjList():
                    cell.setStateBreeze()
                probP -= 1

        while probW > 0:
            i = ran.randint(0, size-1)
            j = ran.randint(0, size-1)
            while self.board[i][j].state['Obstacle'] or self.board[i][j].state['Pit']:
                i = ran.randint(0, size-1)
                j = ran.randint(0, size-1)
            
            if not (self.board[i][j].state['Obstacle'] and self.board[i][j].state['Pit']):
                self.board[i][j].setStateWumpus()
                adj_list = self.board[i][j].getAdjList()
                for cell in adj_list:
                    cell.setStateStench()
                probW -= 1
        
        i = ran.randint(0, size-1)
        j = ran.randint(0, size-1)

        while self.board[i][j].getState()['Obstacle'] or self.board[i][j].getState()['Pit'] or self.board[i][j].getState()['Wumpus']:
            i = ran.randint(0, size-1)
            j = ran.randint(0, size-1)
        
        self.board[i][j].setStateGold()

    def setAdjList(self, size):
        """
        *This method creates an adjacency list for each Cell in the board.
        @param size The size of the board, int
        """
        for i in range(0, size):
            for j in range(0, size):
                if i + 1 < size:
                    self.board[i][j].addAdjacent(self.board[i+1][j])
                if i - 1 >= 0:
                    self.board[i][j].addAdjacent(self.board[i-1][j])
                if j + 1 < size:
                    self.board[i][j].addAdjacent(self.board[i][j+1])
                if j - 1 >= 0:
                    self.board[i][j].addAdjacent(self.board[i][j-1])

    def displayBoard(self, dim):
        """
        *This method displays the board with characters representing the states of the Cells.
        @param dim The size of the board, int
        """
        for i in range(dim):
            for j in range(dim):
                if self.getCell([i,j]).state['Wumpus']:
                    print('W', end='      ')
                elif self.getCell([i,j]).state['Stench'] and self.getCell([i,j]).state['Breeze']:
                    print('SB', end='     ')
                elif self.getCell([i,j]).state['Pit']:
                    print('P', end='      ')
                elif self.getCell([i,j]).state['Stench']:
                    print('S', end='      ')
                elif self.getCell([i,j]).state['Breeze']:
                    print('B', end='      ')
                elif self.getCell([i,j]).state['Gold']:
                    print('G', end='      ')
                elif self.getCell([i,j]).getVisited():
                    print('V', end='      ')
                elif self.getCell([i,j]).state['Obstacle']:
                    print('O', end='      ')
                else:
                    print(self.board[i][j].getIndex(), end=' ')
            print()
        return

"""
*This class object represents each cell on the game board.
*Each Cell contains an index, a visited status as a boolean,
*and a dictionary of potential states for each Cell, initially all False.
"""
class Cell(GameBoard):
    def __init__(self, i, j):
        self.index = [i, j]
        self.adjList = []
        self.visited = False
        self.state = {'Pit': False, 'Wumpus': False, 'Obstacle': False,
                      'Breeze': False, 'Stench': False, 'potP': False,
                      'potW': False, 'Gold': False}

    def getIndex(self):
        """
        *This geter method gets the index of a Cell in the board.
        @return The index of the cell as a list, [i, j]
        """
        return self.index

    def setStatePit(self):
        """
        *This method sets the pit boolean of a Cell to True.
        """
        self.state['Pit'] = True

    def setStateObs(self):
        """
        *This method sets the obstacle boolean of a Cell to True.
        """
        self.state['Obstacle'] = True

    def setStateWumpus(self):
        """
        *This method sets the Wumpus boolean of a Cell to True.
        """
        self.state['Wumpus'] = True
    
    def setStateBreeze(self):
        """
        *This method sets the breeze boolean of a Cell to True.
        """
        self.state['Breeze'] = True

    def setStateStench(self):
        """
        *This method sets the stench boolean of a Cell to True.
        """
        self.state['Stench'] = True
    
    def setStateNoPotPit(self):
        """
        *This method sets the potential pit boolean of a Cell to False.
        """
        self.state['potP'] = False
    
    def selfStateNoPotW(self):
        """
        *This method sets the potential Wumpus boolean of a Cell to False.
        """
        self.state['potW'] = False
    
    def setStateGold(self):
        """
        *This method sets the gold boolean of a Cell to True.
        """
        self.state['Gold'] = True

    def setStatePotPit(self):
        """
        *This method sets potential pit boolean of the cells adjacent to a breeze.
        """
        for cell in self.getAdjList():
            for outerCell in cell.getAdjList():
                if not outerCell.state['Breeze']:
                    cell.state['potP'] = False
                if not cell.visited:
                    cell.state['potP'] = True
            
    def setStatePotWumpus(self):
        """
        *This method sets potential Wumpus boolean of the cells adjacent to a stench.
        """
        for cell in self.getAdjList():
            for outerCell in cell.getAdjList():
                if not outerCell.state['Stench']:
                    cell.state['potW'] = False
                if not cell.visited:
                    cell.state['potW'] = True

    def removeAdjStatePotPit(self):
        """
        *This method sets potential pit boolean of the Cells adjacent to the current Cell to False.
        """
        for cell in self.getAdjList():
            cell.state['potP'] = False
            
    def removeAdjStatePotWumpus(self):
        """
        *This method sets potential Wumpus boolean of the Cells adjacent to the current Cell to False.
        """
        for cell in self.getAdjList():
            cell.state['potW'] = False

    def getState(self):
        """
        *This method gets the state of a current Cell.
        @return A dictionary of string keys and boolean values
        """
        return self.state

    def addAdjacent(self, cell):
        """
        *This method appends Cells to a list.
        @param cell The cell that is being added to the adjacency list of the current cell
        """
        self.adjList.append(cell)

    def getAdjList(self):
        """
        *This method gets the adjacency lsit of a Cell.
        @return The adjacency list the current Cell, list
        """
        return self.adjList
    
    def getVisited(self):
        """
        *This method gets the visited status of a cell.
        @return A boolean indicating if the Cell has been traversed
        """
        return self.visited
    
    def setVisited(self):
        """
        *This method sets the visited status of the Cell to True.
        """
        self.visited = True
