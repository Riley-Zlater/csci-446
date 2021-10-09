
from project2.pythonCode.GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer


from SimpleExplorer import SimpleExplorer

class Explorer(SimpleExplorer):

    def __init__(self, simple_explorer, board_size) -> None:
        self.position = simple_explorer.position
        self.arrows = simple_explorer.arrows
        self.simple_board = GameBoard(board_size)
        super().__init__(self.position, self.arrows)