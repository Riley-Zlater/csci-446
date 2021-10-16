#  Written by Cooper Strahan and Riley Slater
from Explorer import Explorer
from GameBoard import GameBoard
from SimpleExplorer import SimpleExplorer
from math import floor
import numpy as np
from scipy import stats
import decimal

numTests = 100     #  This variable is the number of times each board size is tested

pit_p = .05     #  This variable is the probability of generating a pit
wumpus_p = .05     #  This variable is the probability of generating a Wumpus
obs_p = .05     #  This variable is the probability of generating a obstacle

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
avgCost = []
avgMoves = []
avgWumpusKilled = []
avgDeathByWumpus = []
avgDeathByPit = []
avgGoldCap = []
avgVisitedCells = []

size = 5     #  The board size
print("Simple Explorer Results")
for result in se_results:     #  Access the results
    print("\nboard size of", size,"with", numTests,"tests")

    for board in result:     #  Access the results for a specific board size
        #  Sum the performance measures of the simple explorer for a specific board size
        avgCost.append(board['Cost'])
        avgMoves.append(board['Total Moves'])
        avgVisitedCells.append(board['Total Visited Cells'])
        avgWumpusKilled.append(board['Wumpuses Killed'])
        avgDeathByWumpus.append(board['Death by Wumpus'])
        avgDeathByPit.append(board['Death by Pit'])
        avgGoldCap.append(board['Gold Captured'])
        

    #  divide the summations by the number of tests to find the averages
    avgCost = np.array(avgCost)
    avgMoves = np.array(avgMoves)
    avgVisitedCells = np.array(avgVisitedCells)
    avgWumpusKilled = np.array(avgWumpusKilled)
    avgDeathByWumpus = np.array(avgDeathByWumpus)
    avgDeathByPit = np.array(avgDeathByPit)
    avgGoldCap = np.array(avgGoldCap)

    stdvavgCost = stats.tstd(avgCost)
    stdvavgMoves = stats.tstd(avgMoves)
    stdvavgVisitedCells = stats.tstd(avgVisitedCells)
    stdvavgWumpusKilled = stats.tstd(avgWumpusKilled)
    stdvavgDeathByWumpus = stats.tstd(avgDeathByWumpus)
    stdvavgDeathByPit = stats.tstd(avgDeathByPit)
    stdvavgGoldCap = stats.tstd(avgGoldCap)

    avgCost = stats.describe(avgCost)
    avgMoves = stats.describe(avgMoves)
    avgVisitedCells = stats.describe(avgVisitedCells)
    avgWumpusKilled = stats.describe(avgWumpusKilled)
    avgDeathByWumpus = stats.describe(avgDeathByWumpus)
    avgDeathByPit = stats.describe(avgDeathByPit)
    avgGoldCap = stats.describe(avgGoldCap)


    #  print the results
    print("Cost & ",str(avgCost[1]), " & ", str(avgCost[1]), " & ", str(avgCost[2]), " & ", str(round(stdvavgCost,2)), " \\",
    "\nMoves & ",str(avgMoves[1][0]), " & ", str(avgMoves[1][1]), " & ", str(avgMoves[2]), " & ", str(round(stdvavgMoves,2)), " \\",
    "\nVisited Cells & ",str(avgVisitedCells[1][0]), " & ", str(avgVisitedCells[1][1]), " & ", str(avgVisitedCells[2]), " & ", str(round(stdvavgVisitedCells,2)), " \\",
    "\nWumpuses Killed & ",str(avgWumpusKilled[1][0]), " & ", str(avgWumpusKilled[1][1]), " & ", str(avgWumpusKilled[2]), " & ", str(round(stdvavgWumpusKilled,2)), " \\",
    "\nDeath by Wumpus & ",str(avgDeathByWumpus[1][0]), " & ", str(avgDeathByWumpus[1][1]), " & ", str(avgDeathByWumpus[2]), " & ", str(round(stdvavgDeathByWumpus,2)), " \\",
    "\nDeath by Pit & ",str(avgDeathByPit[1][0]), " & ", str(avgDeathByPit[1][1]), " & ", str(avgDeathByPit[2]), " & ", str(round(stdvavgDeathByPit,2)), " \\",
    "\nGold Captured & ",str(avgGoldCap[1][0]), " & ", str(avgGoldCap[1][1]), " & ", str(avgGoldCap[2]), " & ", str(round(stdvavgGoldCap,2)), " \\")
    size += 5
    #  reset the performance tracking variables for the next board size
    avgCost = []
    avgMoves = []
    avgWumpusKilled = []
    avgDeathByWumpus = []
    avgDeathByPit = []
    avgGoldCap = []
    avgVisitedCells = []

print()
print()

size = 5     #  The board size
print("Explorer Results")
for result in e_results:     #  Access the results
    print("\nboard size of", size,"with", numTests,"tests")

    for board in result:     #  Access the results for a specific board size
        #  Sum the performance measures of the simple explorer for a specific board size
        avgCost.append(board['Cost'])
        avgMoves.append(board['Total Moves'])
        avgWumpusKilled.append(board['Wumpuses Killed'])
        avgDeathByWumpus.append(board['Death by Wumpus'])
        avgDeathByPit.append(board['Death by Pit'])
        avgGoldCap.append(board['Gold Captured'])
        avgVisitedCells.append(board['Total Visited Cells'])

    #  divide the summations by the number of tests to find the averages
    avgCost = np.array(avgCost)
    avgMoves = np.array(avgMoves)
    avgVisitedCells = np.array(avgVisitedCells)
    avgWumpusKilled = np.array(avgWumpusKilled)
    avgDeathByWumpus = np.array(avgDeathByWumpus)
    avgDeathByPit = np.array(avgDeathByPit)
    avgGoldCap = np.array(avgGoldCap)

    stdvavgCost = stats.tstd(avgCost)
    stdvavgMoves = stats.tstd(avgMoves)
    stdvavgVisitedCells = stats.tstd(avgVisitedCells)
    stdvavgWumpusKilled = stats.tstd(avgWumpusKilled)
    stdvavgDeathByWumpus = stats.tstd(avgDeathByWumpus)
    stdvavgDeathByPit = stats.tstd(avgDeathByPit)
    stdvavgGoldCap = stats.tstd(avgGoldCap)

    avgCost = stats.describe(avgCost)
    avgMoves = stats.describe(avgMoves)
    avgVisitedCells = stats.describe(avgVisitedCells)
    avgWumpusKilled = stats.describe(avgWumpusKilled)
    avgDeathByWumpus = stats.describe(avgDeathByWumpus)
    avgDeathByPit = stats.describe(avgDeathByPit)
    avgGoldCap = stats.describe(avgGoldCap)

    #  print the results
    print("Cost & ",str(avgCost[1]), " & ", str(avgCost[1]), " & ", str(avgCost[2]), " & ", str(round(stdvavgCost,2)), " \\",
    "\nMoves & ",str(avgMoves[1][0]), " & ", str(avgMoves[1][1]), " & ", str(avgMoves[2]), " & ", str(round(stdvavgMoves,2)), " \\",
    "\nVisited Cells & ",str(avgVisitedCells[1][0]), " & ", str(avgVisitedCells[1][1]), " & ", str(avgVisitedCells[2]), " & ", str(round(stdvavgVisitedCells,2)), " \\",
    "\nWumpuses Killed & ",str(avgWumpusKilled[1][0]), " & ", str(avgWumpusKilled[1][1]), " & ", str(avgWumpusKilled[2]), " & ", str(round(stdvavgWumpusKilled,2)), " \\",
    "\nDeath by Wumpus & ",str(avgDeathByWumpus[1][0]), " & ", str(avgDeathByWumpus[1][1]), " & ", str(avgDeathByWumpus[2]), " & ", str(round(stdvavgDeathByWumpus,2)), " \\",
    "\nDeath by Pit & ",str(avgDeathByPit[1][0]), " & ", str(avgDeathByPit[1][1]), " & ", str(avgDeathByPit[2]), " & ", str(round(stdvavgDeathByPit,2)), " \\",
    "\nGold Captured & ",str(avgGoldCap[1][0]), " & ", str(avgGoldCap[1][1]), " & ", str(avgGoldCap[2]), " & ", str(round(stdvavgGoldCap,2)), " \\")
    size += 5
    #  reset the performance tracking variables for the next board size
    avgCost = []
    avgMoves = []
    avgWumpusKilled = []
    avgDeathByWumpus = []
    avgDeathByPit = []
    avgGoldCap = []
    avgVisitedCells = []

print()
print()