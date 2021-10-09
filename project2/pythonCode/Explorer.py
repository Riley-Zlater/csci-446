
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer


from SimpleExplorer import SimpleExplorer

class Explorer(SimpleExplorer):

    def __init__(self, simple_explorer, board_size) -> None:
        self.position = simple_explorer.position
        self.arrows = simple_explorer.arrows
        self.simple_board = GameBoard(board_size)
        super().__init__(self.position, self.arrows)
    

    def getCurrentState(self, board):
        i = self.position[0]
        j = self.position[1]
        return board.getCell(j, i).getState()
    
    
    
    def setPotWumpus(self, state):
        if state['Stench'] == True:
            self.simple_board.getCell(self.position).setStatePotWumpus()
    
    def setPotPit(self, state):
        if state['Breeze'] == True:
            self.simple_board.getCell(self.position).setStatePotPit()
    
    def proveWumpus(state):
        return

    def provePit(state):
        return
    
    def moveForwardAssertState(self, board):
        if self.direction == "north":
            self.position = [self.position[0] - 1, self.position[1]]
        if self.direction == "south":
            self.position = [self.position[0] + 1, self.position[1]]
        if self.direction == "east":
            self.position = [self.position[0], self.position[1] + 1]
        if self.direction == "west":
            self.position = [self.position[0], self.position[1] - 1]
        
        state = self.getCurrentState(board)
        
        self.setPotWumpus(state)
        self.setPotPit(state)

        self.proveWumpus(state)

        self.provePit(state)

        self.cost -= 1
        print(self.position)    