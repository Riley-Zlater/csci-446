#Written by Riley Slater and Cooper Strahan

import puzzleImporter as puz
import backtrackSolve as bt
import SimAnneal as sa
from graph import Graph
import forwardCheck as fc


test1 = puz.importPuzzle("..\\testPuzzles\\Hard-P1.csv")

#test1 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P5.csv")

selection = input("Select an algorithm to test:\n"+
                  "1. backtrack solve\n"+
                  "2. backtrack solve with forward checking\n"+
                  "3. backtrack solve with arc consistency\n"+
                  "4. local search using simulated annealing with min conflict heuristic\n"+
                  "5. local search using a genetic alg with a penalty function and tournament selection\n"+
                  "6. exit\n")


if (selection == '1'):
    bt.recursiveBacktrackSolve(test1)
    print()
    bt.displayPuzzle(test1)
    print()
    
elif (selection == '2'):
    puzzle = Graph(test1)
    fc.rBackSolve(puzzle, 0, 0)
    print()
    #bt.displayPuzzle(test1)
    print()
    
##elif (selection == '3'):
##
elif (selection == '4'):
    # sa.assert_random_values(test1)
    # sa.display_puzzle(test1)
    print(sa.simulate_annealing(test1))
    print()
    print( puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P5.csv"))

    # print(test1)
##elif (selection == '5'):

