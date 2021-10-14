#  Written by Cooper Strahan and Riley Slater
from Explorer import Explorer
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer
from math import floor


numTests = 100     #  This variable is the number of times each board size is tested

pit_p = .025     #  This variable is the probability of generating a pit
wumpus_p = .025     #  This variable is the probability of generating a Wumpus
obs_p = .025     #  This variable is the probability of generating a obstacle

#  results containers for the smart explorer
e_five_by_five = []
e_ten_by_ten = []
e_fifteen_by_fifteen = []
e_twenty_by_twenty = []
e_twentfy_five_by_twenty_five = []

#  results containers for the simple explorer
se_five_by_five = []
se_ten_by_ten = []
se_fifteen_by_fifteen = []
se_twenty_by_twenty = []
se_twentfy_five_by_twenty_five = []

#  total results container for smart explorer
e_results = [e_five_by_five, e_ten_by_ten, e_fifteen_by_fifteen, e_twenty_by_twenty, e_twentfy_five_by_twenty_five]

#  total results container for the simpler explorer
se_results = [se_five_by_five, se_ten_by_ten, se_fifteen_by_fifteen, se_twenty_by_twenty, se_twentfy_five_by_twenty_five]

inc = 0     #  this variable serves as an index for the results containers
for boardSize in range(5, 26, 5):     #  boardSize: [5, 10, 15, 20, 25]
    for test in range(numTests):     #  test: 0 - numTests-1; in this case 0-99

        # TESTING
        wumpus = GameBoard(boardSize, pit_p, wumpus_p, obs_p)

        arrows = floor((boardSize ** 2) * wumpus_p)

        se = SimpleExplorer(arrows)
        
        se_results[inc].append(se.simpleSearchForGold(wumpus))
        
        e = Explorer(boardSize, arrows)
        e_results[inc].append(e.searchForGold(wumpus))
    inc += 1

#  INTERPRETTING THE RESULTS

#  integers used to track the performance measures across multiple tests
avgCost = 0
avgMoves = 0
avgWumpusKilled = 0
avgDeathByWumpus = 0
avgDeathByPit = 0
avgGoldCap = 0
avgVisitedCells = 0

size = 5     #  The board size
print("Simple Explorer Results")
for result in se_results:     #  Access the results
    print("\nboard size of", size,"with", numTests,"tests")

    for board in result:     #  Access the results for a specific board size
        #  Sum the performance measures of the simple explorer for a specific board size
        avgCost += board['Cost']
        avgMoves += board['Total Moves']
        avgWumpusKilled += board['Wumpuses Killed']
        avgDeathByWumpus += board['Death by Wumpus']
        avgDeathByPit += board['Death by Pit']
        avgGoldCap += board['Gold Captured']
        avgVisitedCells += board['Total Visited Cells']

    #  divide the summations by the number of tests to find the averages
    avgCost /= numTests
    avgMoves /= numTests
    avgWumpusKilled /= numTests
    avgDeathByWumpus /= numTests
    avgDeathByPit /= numTests
    avgGoldCap /= numTests
    avgVisitedCells /= numTests
    #  print the results
    print("Average Cost:",avgCost,"\nAverage Moves:",avgMoves,"\nAverage Wumpuses Killed:",avgWumpusKilled,"\nAverage Death by Wumpus:",avgDeathByWumpus,
    "\nAverage Death by Pit:",avgDeathByPit,"\nAverage Gold Captured:",avgGoldCap,"\nAverage Visited Cells:",avgVisitedCells)
    size += 5
    #  reset the performance tracking variables for the next board size
    avgCost = 0
    avgMoves = 0
    avgWumpusKilled = 0
    avgDeathByWumpus = 0
    avgDeathByPit = 0
    avgGoldCap = 0
    avgVisitedCells = 0

print()
print()

size = 5     #  The board size
print("Explorer Results")
for result in e_results:     #  Access the results
    print("\nboard size of", size,"with", numTests,"tests")

    for board in result:     #  Access the results for a specific board size
        #  Sum the performance measures of the smart explorer for a specific board size
        avgCost += board['Cost']
        avgMoves += board['Total Moves']
        avgWumpusKilled += board['Wumpuses Killed']
        avgDeathByWumpus += board['Death by Wumpus']
        avgDeathByPit += board['Death by Pit']
        avgGoldCap += board['Gold Captured']
        avgVisitedCells += board['Total Visited Cells']

    #  divide the summations by the number of tests to find the averages
    avgCost /= numTests
    avgMoves /= numTests
    avgWumpusKilled /= numTests
    avgDeathByWumpus /= numTests
    avgDeathByPit /= numTests
    avgGoldCap /= numTests
    avgVisitedCells /= numTests
    #  print the results
    print("Average Cost:",avgCost,"\nAverage Moves:",avgMoves,"\nAverage Wumpuses Killed:",avgWumpusKilled,"\nAverage Death by Wumpus:",avgDeathByWumpus,
    "\nAverage Death by Pit:",avgDeathByPit,"\nAverage Gold Captured:",avgGoldCap,"\nAverage Visited Cells:",avgVisitedCells)
    size += 5
    #  reset the performance tracking variables for the next board size
    avgCost = 0
    avgMoves = 0
    avgWumpusKilled = 0
    avgDeathByWumpus = 0
    avgDeathByPit = 0
    avgGoldCap = 0
    avgVisitedCells = 0