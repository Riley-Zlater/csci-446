import copy
from pprint import pprint
from random import randint
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer


from SimpleExplorer import SimpleExplorer

class Explorer(SimpleExplorer):

    def __init__(self, simple_explorer, board_size) -> None:
        self.position = simple_explorer.position
        self.arrows = simple_explorer.arrows
        self.simple_board = GameBoard(board_size)
        self.visited_cells = []
        self.moves = 0
        super().__init__(self.position, self.arrows)
    

    def getCurrentCell(self, board):
        return board.getCell(self.position)
    
    def getCurrentState(self, cell):
        return cell.getState()  
    
    def setPotWumpus(self, state):
        if state['Stench'] == True:
            self.simple_board.getCell(self.position).setStatePotWumpus()
    
    def setPotPit(self, state):
        if state['Breeze'] == True:
            self.simple_board.getCell(self.position).setStatePotPit()
    
    def removePotPit(self, state):
        if state['Breeze'] == False:
            self.simple_board.getCell(self.position).removeAdjStatePotPit()

    def removePotWumpus(self, state):
        if state['Breeze'] == False:
            self.simple_board.getCell(self.position).removeAdjStatePotWumpus()

    
    def proveWumpus(self):
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
                print(copy_pot_wumpus_list)

        if len(copy_pot_wumpus_list) == 1:
            cell_index = copy_pot_wumpus_list[0]
            j, i = cell_index
            self.simple_board.getCell([i,j]).setStateWumpus()
            print("PROVED WUMPUS")

        
    def provePit(self):
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
                print(copy_pot_pit_list)

        if len(copy_pot_pit_list) == 1:
            cell_index = copy_pot_pit_list[0]
            j, i = cell_index
            self.simple_board.getCell([i,j]).setStatePit()
            print("PROVED PIT")
        
    
    def safeState(self, state):
        if state['Pit']:
            return False
        if state['Wumpus']:
            return False
        
        return True 
        
    def uncertainSafeState(self, state):
        if state['potP']:
            return True
        if state['potW']:
            return True
        
        return False
    
    def determineDirection(self, projectedCell):
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
            self.simple_board.getCell(cell.getIndex()).setStateObs()
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
            self.proveWumpus()
        
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
        # print(self.position)    

    def determineDeath(self, cell):
        state = self.getCurrentState(cell)     

        if state['Wumpus'] == True:
            print("Killed by a stinking wumpus")
            # print(cell.getIndex())
            # print(state)
            return True
        elif state['Pit'] == True:
            print("Fell into a pit")
            # print(cell.getIndex())
            # print(state)
            return True
        
        return False

    def determineWin(self, cell):
        state = self.getCurrentState(cell)

        

        if state['Gold'] == True:
            self.simple_board.getCell(cell.getIndex()).setStateGold()
            return True
        
        return False
    
    
    def searchForGold(self, board):

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
            # print(self.position)
            print("Explorer current position:",self.position)

            cell = board.getCell(self.position)
            # print(cell.getIndex())
            board.displayBoard(board.getSize())
            print()
            self.simple_board.displaySimpleBoard(board.getSize())
            print()

            v_c = [cell.getIndex() for cell in self.visited_cells]
            print("Visted Cells list:")
            print(v_c)

            if self.determineDeath(cell) == True:
                self.cost -= 1000
                print("Lost Board")
                break
            
            if self.determineWin(cell) == True:
                self.cost += 1000
                self.simple_board.displaySimpleBoard(board.getSize())
                print("Won Board")
                break

            # input("Press enter")
            self.findBestMove(board)
        
        return self.cost

            
        