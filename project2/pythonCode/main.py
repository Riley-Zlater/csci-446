from Explorer import Explorer
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer
from math import floor

boardSize = 5

pit_p = 0.025
wumpus_p = .025
obs_p = .025

e_five_by_five = []
e_ten_by_ten = []
e_fifteen_by_fifteen = []
e_twenty_by_twenty = []
e_twentfy_five_by_twenty_five = []

se_five_by_five = []
se_ten_by_ten = []
se_fifteen_by_fifteen = []
se_twenty_by_twenty = []
se_twentfy_five_by_twenty_five = []

e_results = [e_five_by_five, e_ten_by_ten, e_fifteen_by_fifteen, e_twenty_by_twenty, e_twentfy_five_by_twenty_five]
se_results = [se_five_by_five, se_ten_by_ten, se_fifteen_by_fifteen, se_twenty_by_twenty, se_twentfy_five_by_twenty_five]



inc = 0
while boardSize <= 10:
    for i in range(0,10):
        wumpus = GameBoard(boardSize, pit_p, wumpus_p, obs_p)

        arrows = floor((boardSize ** 2) * wumpus_p)

        se = SimpleExplorer(arrows)
        
        se_results[inc].append(se.simpleSearchForGold(wumpus))
        
        e = Explorer(boardSize, arrows)
        e_results[inc].append(e.simpleSearchForGold(wumpus))




    boardSize += 5
    inc += 1
    

for result in se_results:
    print(result)

for result in e_results:
    print(result)