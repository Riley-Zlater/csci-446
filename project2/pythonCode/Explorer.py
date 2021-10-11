import copy
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer


from SimpleExplorer import SimpleExplorer

class Explorer(SimpleExplorer):

    def __init__(self, simple_explorer, board_size) -> None:
        self.position = simple_explorer.position
        self.arrows = simple_explorer.arrows
        self.simple_board = GameBoard(board_size)
        self.visited_cells = dict()
        super().__init__(self.position, self.arrows)
    

    def getCurrentCell(self, board):
        i = self.position[0]
        j = self.position[1]
        return board.getCell(j, i)
    
    def getCurrentState(self, cell):
        return cell.getState()  
    
    def setPotWumpus(self, state):
        if state['Stench'] == True:
            self.simple_board.getCell(self.position).setStatePotWumpus()
    
    def setPotPit(self, state):
        if state['Breeze'] == True:
            self.simple_board.getCell(self.position).setStatePotPit()
    
    def proveWumpus(self):

        false_wumpus_list = dict()
        pot_wumpus_list = dict()

        for cell in self.visited_cells:
            adj_list = cell.getAdjacencyList()
            for c in adj_list:
                if c.getState()['Wumpus'] is False:
                    false_wumpus_list[c.getIndex()] = c.getState()['Wumpus']
        
        for cell in self.visited_cells:
            adj_list = cell.getAdjacencyList()
            for c in adj_list:
                pot_wumpus_list[c.getIndex()] = c.getState()['potW']

            copy_pot_wumpus_list = copy.deepcopy(pot_wumpus_list)
            
            for pot_wumpus_index in pot_wumpus_list:
                if pot_wumpus_index in false_wumpus_list.keys():
                    del copy_pot_wumpus_list[pot_wumpus_index]
            

            if len(copy_pot_wumpus_list) == 1:
                cell_index = list(copy_pot_wumpus_list.keys()[0])
                wumpus_cell = self.simple_board.getCell(cell_index) 
                wumpus_cell.setStateWumpus()
                print(wumpus_cell.getIndex())

        

    def provePit(self):
        false_pit_list = dict()
        pot_pit_list = dict()

        for cell in self.visited_cells:
            adj_list = cell.getAdjacencyList()
            for c in adj_list:
                if c.getState()['Pit'] is False:
                    false_pit_list[c.getIndex()] = c.getState()['Pit']
        
        for cell in self.visited_cells:
            if cell.getStatus()['Breeze']:
                adj_list = cell.getAdjacencyList()
                
                for c in adj_list:
                    pot_pit_list[c.getIndex()] = c.getState()['potP']
                
                copy_pot_pit_list = copy.deepcopy(pot_pit_list)
        
                for pot_pit_index in pot_pit_list:
                    if pot_pit_index in false_pit_list.keys():
                        del copy_pot_pit_list[pot_pit_index]

                if len(copy_pot_pit_list) == 1:
                    cell_index = list(copy_pot_pit_list.keys()[0])
                    pit_cell = self.simple_board.getCell(cell_index) 
                    pit_cell.setStatePit()
                    print(pit_cell.getIndex())
        
        return False
    
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

        if c_i - 1 == p_i:
            self.direction == "north"
        elif c_i + 1 == p_i: 
            self.direction == "south"
        elif c_j + 1 == p_j:
            self.direction == "east"
        elif c_j - 1 == p_j:
            self.direction == "west"
        
    def findBestMove(self, board):
        cell = board.getCurrentCell()

        adj_list = cell.getAdjacencyList()

        safe_cells = []

        for adj_cell in adj_list:
            state = adj_cell.getState()
            if self.safeState(state):
                safe_cells.append(adj_cell)
        
        if len(safe_cells) == 0:
            for adj_cell in adj_list:
                state = adj_cell.getState()
                if self.uncertainSafeState(state):
                    safe_cells.append(adj_cell)

        priority_move = safe_cells[0]

        for safe_cell in safe_cells:
            if safe_cell.getVisted() == False:
                priority_move = safe_cell
        

        self.determineDirection(priority_move)

        self.moveForwardAssertState(board)
        

    def moveForwardAssertState(self, board):
        if self.direction == "north":
            self.position = [self.position[0] - 1, self.position[1]]
        if self.direction == "south":
            self.position = [self.position[0] + 1, self.position[1]]
        if self.direction == "east":
            self.position = [self.position[0], self.position[1] + 1]
        if self.direction == "west":
            self.position = [self.position[0], self.position[1] - 1]
        
        
        cell = self.getCurrentCell(board)
        self.visited_cells[cell.index] = cell

        state = self.getCurrentState(cell)
        
        self.setPotWumpus(state)
        self.setPotPit(state)

        self.proveWumpus()
        self.provePit()

        self.cost -= 1
        print(self.position)    