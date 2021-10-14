# Writen by Cooper Strahan and Riley Slater
import copy
from random import randint
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer

"""
*This class extends the SimpleExplorer class and adds the inference engine functionality.
"""
class Explorer(SimpleExplorer):
    def __init__(self, board_size, arrows) -> None:
        self.position = [0,0]
        self.arrows = arrows
        self.simple_board = GameBoard(board_size)
        self.cost = 0
        super().__init__(self.arrows)
    
    def setPotWumpus(self, state):
        """
        *This method updates the Cells adjacent to a stench to be potential Wumpuses.
        @param state The state of the current Cell
        """
        if state['Stench'] == True:
            self.simple_board.getCell(self.position).setStatePotWumpus()
    
    def setPotPit(self, state):
        """
        *This method updates the Cells adjacent to a breeze to be potential pits.
        @param state The state of the current Cell
        """
        if state['Breeze'] == True:
            self.simple_board.getCell(self.position).setStatePotPit()
    
    def removePotPit(self, state):
        """
        *This method will remove a potential pit after more evaluation.
        @param state The state of the current cell
        """
        if state['Breeze'] == False:
            self.simple_board.getCell(self.position).removeAdjStatePotPit()

    def removePotWumpus(self, state):
        """
        *This method will remove a potential Wumpus after more evaluation.
        @param state The state of the current cell
        """
        if state['Breeze'] == False:
            self.simple_board.getCell(self.position).removeAdjStatePotWumpus()

    def proveWumpus(self, board):
        """
        *This method applies unification and resolution to prove the location of Wumpus.
        @param board The GameBoard object
        """
        false_wumpus_list = []
        pot_wumpus_list = []

        for cell in self.visited_cells:
            act_cell = self.simple_board.getCell(cell.getIndex())
            adj_list = act_cell.getAdjList()
            false_wumpus_list.append(cell.getIndex())

            for c in adj_list:
                if c.getState()['potW'] == False:
                    false_wumpus_list.append(c.getIndex())

        for cell in self.simple_board.getCell(self.position).getAdjList():
            pot_wumpus_list.append(cell.getIndex())

        copy_pot_wumpus_list = copy.deepcopy(pot_wumpus_list)

        for pot_wumpus_index in pot_wumpus_list:
            if pot_wumpus_index in false_wumpus_list:
                copy_pot_wumpus_list.remove(pot_wumpus_index)

        if len(copy_pot_wumpus_list) == 1:
            cell_index = copy_pot_wumpus_list[0]
            j, i = cell_index
            self.simple_board.getCell([i,j]).setStateWumpus()
            self.determineDirection(self.simple_board.getCell([i,j]))
            self.shootArrow(board)
            if(self.screamHeard == True):
                self.screamHeard = False
        
    def provePit(self):
        """
        *This method applies unification and resolution to prove the location of pit.
        """
        false_pit_list = []
        pot_pit_list = []

        for cell in self.visited_cells:
            act_cell = self.simple_board.getCell(cell.getIndex())
            adj_list = act_cell.getAdjList()
            false_pit_list.append(cell.getIndex())

            for c in adj_list:
                if c.getState()['potP'] == False:
                    false_pit_list.append(c.getIndex())

        for cell in self.simple_board.getCell(self.position).getAdjList():
            pot_pit_list.append(cell.getIndex())

        copy_pot_pit_list = copy.deepcopy(pot_pit_list)

        for pot_pit_index in pot_pit_list:
            if pot_pit_index in false_pit_list:
                copy_pot_pit_list.remove(pot_pit_index)

        if len(copy_pot_pit_list) == 1:
            cell_index = copy_pot_pit_list[0]
            j, i = cell_index
            self.simple_board.getCell([i,j]).setStatePit()
        
    def safeState(self, state):
        """
        *This method determines if a Cell is safe given its states.
        @state the States of a Cell
        @return boolean
        """
        if state['Pit']:
            return False
        if state['Wumpus']:
            return False
        
        return True 
        
    def uncertainSafeState(self, state):
        """
        *This method determines if a Cell is questionable interms of safety.
        @param state The state of the cell
        @return boolean
        """
        if state['potP']:
            return True
        if state['potW']:
            return True
        
        return False
    
    def determineDirection(self, projectedCell):
        """
        *This method decides which direction our explorer should turn towards.
        @param projectedCell The cell the agent is considering moving to
        """
        c_i,c_j = self.simple_board.getCell(self.position).getIndex()
        p_i,p_j = projectedCell.getIndex()

        if c_i == p_i and c_j - 1 == p_j:
            self.direction = "north"
        elif c_i == p_i and c_j + 1 == p_j: 
            self.direction = "south"
        elif c_j == p_j and c_i + 1 == p_i:
            self.direction = "east"
        elif c_j == p_j and c_i - 1 == p_i:
            self.direction = "west"
        
        self.cost -= 1
        
    def findBestMove(self, board):
        """
        *This method finds an optimal move given the current board.
        @param board The GameBoard object
        """
        cell = board.getCell(self.position)
        adj_list = cell.getAdjList()
        safe_cells = []

        for adj_cell in adj_list:
            state = adj_cell.getState()
            if self.safeState(state) == True and adj_cell not in self.visited_cells:
                safe_cells.append(adj_cell)
        
        if len(safe_cells) == 0:         
            for adj_cell in adj_list:
                state = adj_cell.getState()
                if self.safeState(state) == True:
                    safe_cells.append(adj_cell)

        if len(safe_cells) > 0:
            priority_move = safe_cells[randint(0,len(safe_cells)-1)]
        
        elif len(safe_cells) == 0:
            
            for adj_cell in adj_list:
                state = adj_cell.getState()
                if self.uncertainSafeState(state):
                    safe_cells.append(adj_cell)
            
        if len(safe_cells) == 0:
            priority_move = None

        if priority_move != None:
            self.determineDirection(priority_move)
            self.moveForwardAssertState(board)
        
        if priority_move == None:
            self.turn()
            self.moveForwardAssertState(board)


    def moveForwardAssertState(self, board):
        """
        *This method moves the agent in the direction it is facing.
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
        simple_cell = self.simple_board.getCell(self.position)

        if cell.getState()['Obstacle'] == True:
            self.simple_board.getCell(self.position).setStateObs()
            self.position = old_position
            cell = board.getCell(self.position)
            simple_cell = self.simple_board.getCell(self.position)

        if cell not in self.visited_cells:
            self.visited_cells.append(cell)

        state = self.getCurrentState(cell)
        self.simple_board.getCell(self.position).setVisited()
        
        if state['Stench']:
            simple_cell.setStateStench()
            self.setPotWumpus(state)
            self.proveWumpus(board)
        
        if state['Breeze']:
            simple_cell.setStateBreeze()
            self.setPotPit(state)
            self.provePit()

        if state['Breeze'] == False:
            self.removePotPit(state)
        
        if state['Stench'] == False:
            self.removePotWumpus(state)   

        self.cost -= 1
        self.moves += 1 
    
    def searchForGold(self, board):
        """
        *This method puts everything into motion and performes the search on the board using the agent's logic.
        @param board The GameBoard object
        @return A dictionary containing the performance measures
        """
        temp = self.simple_board.getCell(self.position)
        temp.setVisited()
        self.visited_cells.append(temp)
        state = self.getCurrentState(temp)

        if state['Stench'] == True:
            temp.setStateStench()
            self.setPotWumpus(state)
        
        if state['Breeze']:
            temp.setStateBreeze()
            self.setPotPit(state)
        
        if state['Breeze'] == False:
            self.removePotPit(state)
        
        if state['Stench'] == False:
            self.removePotWumpus(state)

        while(self.moves <= board.getSize() * board.getSize()):
            cell = board.getCell(self.position)
            v_c = [cell.getIndex() for cell in self.visited_cells]

            if self.determineDeath(cell) == True:
                self.cost -= 1000
                break
            
            if self.determineWin(cell) == True:
                self.cost += 1000
                break

            self.findBestMove(board)

        return {"Cost": self.cost, 
                "Total Moves": self.moves, 
                "Wumpuses Killed": self.wumpus_kills,
                "Death by Wumpus": self.death_by_wumpus,
                "Death by Pit": self.death_by_pit, 
                "Gold Captured": self.gold, 
                "Total Visited Cells": len(self.visited_cells)}

            
        