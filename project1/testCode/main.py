#Written by Riley Slater and Cooper Strahan

import puzzleImporter as puz
from graph import Graph
import backtrackSolve as bt
import forwardCheck as fc
import arc as arc
import SimAnneal as sa




test1 = puz.importPuzzle("..\\testPuzzles\\Evil-P3.csv")
puzzle1 = Graph(test1)

#test1 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P5.csv")

selection = input("Select an algorithm to test:\n" +
                  "1. backtrack solve\n" +
                  "2. backtrack solve with forward checking\n" +
                  "3. backtrack solve with arc consistency\n" +
                  "4. local search using simulated annealing with min conflict heuristic\n" +
                  "5. local search using a genetic alg with a penalty function and tournament selection\n" +
                  "6. exit\n")


if selection == '1':
    print("This is the solution from the backtracking algorithm:\n")
    bt.recursiveBacktrackSolve(puzzle1, 0, 0)
    print("\nThis solution took", bt.resets, "backtracks")
    
elif selection == '2':
    print("This is the solution from the backtracking + forward checking algorithm:\n")
    fc.forwardCheck(puzzle1, 0, 0)
    print("\nThis solution took", fc.resets, "backtracks")
    
elif selection == '3':
    print("This is the solution from the backtracking + arc consistency algorithm:\n")
    arc.arc(puzzle1, 0, 0)
    print("\nThis solution took", arc.resets, "backtracks")

elif selection == '4':
    # sa.assert_random_values(test1)
    # sa.display_puzzle(test1)
    print( puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Evil-P1.csv"))
    print()
    solution = sa.simulate_annealing(test1)
    print()
    print(solution)
    print(sa.minimum_cost_function(solution))
    # print( puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P5.csv"))

    # print(test1)
##elif (selection == '5'):

