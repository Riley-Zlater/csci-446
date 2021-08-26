import puzzleImporter as puz
import bruteSearch as brute

test1 = puz.importPuzzle("..\\testPuzzles\\Easy-P1.csv")
brute.displayPuzzle(test1)
brute.bruteSolve(test1)
print()
brute.displayPuzzle(test1)
