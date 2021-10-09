
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer


from SimpleExplorer import SimpleExplorer

class Explorer(SimpleExplorer):

    def __init__(self, simple_explorer, board_size) -> None:
        self.position = simple_explorer.position
        self.arrows = simple_explorer.arrows
        self.simple_board = GameBoard(board_size)
        super().__init__(self.position, self.arrows)
    

    def getCurrentState(self):
        i = self.position[0]
        j = self.position[1]
        return self.simple_board.getCell(j, i).getState()
    
    def proveWumpus(self):
        return
    
    def provePit(self):
        return
    
    