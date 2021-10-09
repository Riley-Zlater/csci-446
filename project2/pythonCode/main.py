from Explorer import Explorer
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer

boardSize = 5

wumpus = GameBoard(boardSize)

wumpus.displayBoard(boardSize)

jerry = SimpleExplorer([3,3], 1)

jerry2 = Explorer(jerry)