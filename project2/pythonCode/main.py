from Explorer import Explorer
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer

boardSize = 5

wumpus = GameBoard(boardSize, 0.03, 0.2, 0.5)

wumpus.displayBoard(boardSize)

jerry = SimpleExplorer([0,0], 3)

explorer = Explorer(jerry, boardSize)

explorer.searchForGold(wumpus)
# print(explorer.getCurrentState())