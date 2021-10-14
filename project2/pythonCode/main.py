from Explorer import Explorer
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer
from math import floor


numTests = 100

pit_p = .025
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
for boardSize in range(5, 26, 5):
    for test in range(numTests):
        wumpus = GameBoard(boardSize, pit_p, wumpus_p, obs_p)

        arrows = floor((boardSize ** 2) * wumpus_p)

        se = SimpleExplorer(arrows)
        
        se_results[inc].append(se.simpleSearchForGold(wumpus))
        
        e = Explorer(boardSize, arrows)
        e_results[inc].append(e.searchForGold(wumpus))
    inc += 1

avgCost = 0
avgMoves = 0
avgWumpusKilled = 0
avgDeathByWumpus = 0
avgDeathByPit = 0
avgGoldCap = 0
avgVisitedCells = 0

i = 5
print("Simple Explorer Results")
for result in se_results:
    print("\nboard size of", i,"with", numTests,"tests")
    for board in result:
        avgCost += board['Cost']
        avgMoves += board['Total Moves']
        avgWumpusKilled += board['Wumpuses Killed']
        avgDeathByWumpus += board['Death by Wumpus']
        avgDeathByPit += board['Death by Pit']
        avgGoldCap += board['Gold Captured']
        avgVisitedCells += board['Total Visited Cells']

    avgCost /= numTests
    avgMoves /= numTests
    avgWumpusKilled /= numTests
    avgDeathByWumpus /= numTests
    avgDeathByPit /= numTests
    avgGoldCap /= numTests
    avgVisitedCells /= numTests
    print("Average Cost:",avgCost,"\nAverage Moves:",avgMoves,"\nAverage Wumpuses Killed:",avgWumpusKilled,"\nAverage Death by Wumpus:",avgDeathByWumpus,
    "\nAverage Death by Pit:",avgDeathByPit,"\nAverage Gold Captured:",avgGoldCap,"\nAverage Visited Cells:",avgVisitedCells)
    i += 5
    avgCost = 0
    avgMoves = 0
    avgWumpusKilled = 0
    avgDeathByWumpus = 0
    avgDeathByPit = 0
    avgGoldCap = 0
    avgVisitedCells = 0

print()
print()

i = 5
print("Explorer Results")
for result in e_results:
    print("\nboard size of", i,"with", numTests,"tests")
    for board in result:
        avgCost += board['Cost']
        avgMoves += board['Total Moves']
        avgWumpusKilled += board['Wumpuses Killed']
        avgDeathByWumpus += board['Death by Wumpus']
        avgDeathByPit += board['Death by Pit']
        avgGoldCap += board['Gold Captured']
        avgVisitedCells += board['Total Visited Cells']

    avgCost /= numTests
    avgMoves /= numTests
    avgWumpusKilled /= numTests
    avgDeathByWumpus /= numTests
    avgDeathByPit /= numTests
    avgGoldCap /= numTests
    avgVisitedCells /= numTests
    print("Average Cost:",avgCost,"\nAverage Moves:",avgMoves,"\nAverage Wumpuses Killed:",avgWumpusKilled,"\nAverage Death by Wumpus:",avgDeathByWumpus,
    "\nAverage Death by Pit:",avgDeathByPit,"\nAverage Gold Captured:",avgGoldCap,"\nAverage Visited Cells:",avgVisitedCells)
    i += 5
    avgCost = 0
    avgMoves = 0
    avgWumpusKilled = 0
    avgDeathByWumpus = 0
    avgDeathByPit = 0
    avgGoldCap = 0
    avgVisitedCells = 0