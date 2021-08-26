import puzzleImporter as puz
import backtrackSolve as bt

test1 = puz.importPuzzle("..\\testPuzzles\\Easy-P1.csv")
bt.displayPuzzle(test1)
bt.recursiveBacktrackSolve(test1)
print()
bt.displayPuzzle(test1)
