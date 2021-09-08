import puzzleImporter as puz
import backtrackSolve as bt
import backtrackSolveWithLookAhead as btfc


test1 = puz.importPuzzle("..\\testPuzzles\\Easy-P2.csv")

selection = input("Select an algorithm to test:\n"+
                  "1. backtrack solve\n"+
                  "2. backtrack solve with forward checking\n"+
                  "3. backtrack solve with arc consistency\n"+
                  "4. local search using simulated annealing with min conflict heuristic\n"+
                  "5. local search using a genetic alg with a penalty function and tournament selection\n")


if (selection == '1'):
    bt.recursiveBacktrackSolve(test1)
    print()
    bt.displayPuzzle(test1)
    print()
    
elif (selection == '2'):
    btfc.recursiveBacktrackSolve(test1)
    print()
    btfc.displayPuzzle(test1)
    print()
    
##elif (selection == '3'):
##
##elif (selection == '4'):
##
##elif (selection == '5'):

