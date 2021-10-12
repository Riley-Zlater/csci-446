from Explorer import Explorer
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer

boardSize = 10

wumpus = GameBoard(boardSize, 0.25, 0.1, .33)

#wumpus.displayBoard(boardSize)

jerry = SimpleExplorer([0,0], 3)

explorer = Explorer(jerry, boardSize)

print(explorer.searchForGold(wumpus))

# print(explorer.getCurrentState())

five_by_five = []
# ten_by_ten = []
# fifteen_by_fifteen = []
# twenty_by_twenty = []
# twentfy_five_by_twenty_five = []

# while boardSize <= 25:
for i in range(0,10):
    wumpus = GameBoard(boardSize, 0.05, .05, .05)
    se = SimpleExplorer([0,0], 3)
    e = Explorer(se, boardSize)
    five_by_five.append(e.searchForGold(wumpus))
#     boardSize += 5

print(five_by_five)
    