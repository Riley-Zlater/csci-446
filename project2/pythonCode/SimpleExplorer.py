# Written by Cooper Strahan and Riley Slater
import random as rd

"""
*This Class does the funcitonality for the reactionary agent.
"""
class SimpleExplorer:
    def __init__(self, arrow) -> None:
        self.position = [0,0]
        self.arrows = arrow
        self.gold = 0
        self.wumpus_kills = 0
        self.death_by_pit = 0
        self.death_by_wumpus = 0
        self.visited_cells = []
        self.cost = 0
        self.moves = 0
        self.direction = "north"
        self.screamHeard = False
    
    def getCurrentCell(self, board):
        """
        *This method gets the cell that the agent is in.
        @param board The GameBoard object
        @return The [i, j] indecies of the agent, list
        """
        return board.getCell(self.position)
    
    def getCurrentState(self, cell):
        """
        *This method gets the states of the Cell the agent is in.
        @param cell A Cell object which is a child of the GameBoard class
        @return A dictionary with the boolean values of the possible states for a Cell
        """
        return cell.getState()

    def turn(self):
        """
        *This method randomly choose which way the agent will face north, east, west, or south.
        """
        num = rd.random()
        if(num < 0.25):
            self.direction = "north"
        elif(num < 0.5):
            self.direction = "south"
        elif(num < 0.75):
            self.direction = "east"
        elif(num > 0.75):
            self.direction = "west"
        self.cost -= 1
    
    def directedTurn(self, direction):
        """
        *This method updates the direction the agent is facing directly.
        @param direction The direction the agent will be facing, string
        """
        self.direction = direction
        self.cost -= 1
    
    
    def moveForward(self, board):
        """
        *This method moves the agent from one cell to another.
        @param board The GameBoard object
        """
        old_position = self.position

        if self.direction == "north" and self.position[0] - 1 >= 0:
            self.position = [self.position[0] - 1, self.position[1]]

        if self.direction == "south" and self.position[0] + 1 <= board.getSize()-1:
            self.position = [self.position[0] + 1, self.position[1]]

        if self.direction == "east" and self.position[1] + 1 <= board.getSize()-1:
            self.position = [self.position[0], self.position[1] + 1]

        if self.direction == "west" and self.position[1] - 1 >= 0:
            self.position = [self.position[0], self.position[1] - 1]

        cell = board.getCell(self.position)

        if cell.getState()['Obstacle'] == True:
            self.position = old_position

        self.cost -= 1
        self.moves += 1
        
    def shootArrow(self, board):
        """
        *This method shoots an arrow based on the direction the agent is facing.
        @param board The GameBoard object
        @return boolean
        """
        if self.arrows > 0:
            self.arrows -= 1
            self.cost -= 50

            arrow_pos = self.position
            

            if self.direction == "north":
                while arrow_pos[0] > 0:
                    arrow_pos = [arrow_pos[0] - 1, arrow_pos[1]]
                    self.arrow_fire(board, arrow_pos)

            if self.direction == "south":
                while arrow_pos[0] < board.getSize()-1:
                    arrow_pos = [arrow_pos[0] + 1, arrow_pos[1]]
                    self.arrow_fire(board, arrow_pos)

            if self.direction == "east":
                while arrow_pos[1] < board.getSize()-1:
                    arrow_pos = [arrow_pos[0], arrow_pos[1] + 1]
                    self.arrow_fire(board, arrow_pos)

            if self.direction == "west":
                while arrow_pos[1] > 0:
                    arrow_pos = [arrow_pos[0] -1, arrow_pos[1] - 1]
                    self.arrow_fire(board, arrow_pos)

        return False
    
    def arrow_fire(self, board, arrow_pos):
        """
        *This method tracks the arrows flight path and notifies the agent if a Wumpus is hit.
        @param board The GameBoard object
        @param arrow_pos The indecies of the arrow
        @return boolean
        """
        arrow_cell_state = self.getCurrentState(board.getCell(arrow_pos))
        if arrow_cell_state['Wumpus'] == True:
            self.screamHeard = True
            self.wumpus_kills += 1
            return True

        if arrow_cell_state['Obstacle'] == True:
            return False

    def getPosition(self):
        """
        *This method gets the current position of the agent.
        @return The [i, j] indecies of the agent, list
        """
        return self.position
    
    def determineDeath(self, cell):
        """
        *This method determines if the agent has walked into a Wumpus or pit.
        @param cell The Cell object location of the agent on the GameBoard
        @return boolean
        """
        state = self.getCurrentState(cell)     

        if state['Wumpus'] == True:
            self.death_by_wumpus += 1
            return True

        elif state['Pit'] == True:
            self.death_by_pit += 1
            return True
        
        return False

    def determineWin(self, cell):
        """
        *This method determines if the agent has found the gold.
        @param cell The Cell object location of the agent on the GameBoard
        @return boolean
        """
        state = self.getCurrentState(cell)

        if state['Gold'] == True:
            self.gold += 1
            return True
        
        return False

    def simpleSearchForGold(self, board):
        """
        *This method does a search for the gold using the simple reactive explorer agent.
        @param board The GameBoard object
        @return A dictionary containing the performance measures
        """
        while(self.moves <= board.getSize() * board.getSize()):
            
            cell = board.getCell(self.position)

            if cell not in self.visited_cells:
                self.visited_cells.append(cell)

            if self.determineDeath(cell) == True:
                self.cost -= 1000
                break
            
            if self.determineWin(cell) == True:
                self.cost += 1000
                break

            if rd.random() > 0.98:
                self.shootArrow(board)

            if (self.screamHeard == True):
                self.screamHeard = False

            self.turn()
            self.moveForward(board)
            cell = board.getCell(self.position)

        return {"Cost": self.cost, 
                "Total Moves": self.moves, 
                "Wumpuses Killed": self.wumpus_kills,
                "Death by Wumpus": self.death_by_wumpus,
                "Death by Pit": self.death_by_pit, 
                "Gold Captured": self.gold, 
                "Total Visited Cells": len(self.visited_cells)}