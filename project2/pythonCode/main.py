from Explorer import Explorer
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer

boardSize = 5

wumpus = GameBoard(boardSize, 0.1, 0.05, 0.1)

wumpus.displayBoard(boardSize)

jerry = SimpleExplorer([0,0], 3)

explorer = Explorer(jerry, boardSize)

explorer.searchForGold(wumpus)

# print(explorer.getCurrentState())