import puzzleImporter as puz
import backtrackSolve as bt
import backtrackSolveWithLookAhead as btfc


test1 = puz.importPuzzle("..\\testPuzzles\\Easy-P2.csv")


bt.recursiveBacktrackSolve(test1)
print()
bt.displayPuzzle(test1)
print()

##btfc.recursiveBacktrackSolve(test1)
##print()
##btfc.displayPuzzle(test1)
##print()

