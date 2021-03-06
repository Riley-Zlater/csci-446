# Written by Riley Slater and Cooper Strahan

import puzzleImporter as puz
import backtrackSolve as bt
import arc as arc
from SimAnneal import SimAnneal
from graph import Graph
import forwardCheck as fc
from GeneticAlgorithm import GeneticAlgorithm

test1 = puz.importPuzzle("..\\testPuzzles\\Med-P1.csv")
puzzle1 = Graph(test1)
test2 = puz.importPuzzle("..\\testPuzzles\\Evil-P1.csv")
puzzle2 = Graph(test2)
#test1 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P5.csv")
#puzzle1 = Graph(test1)

selection = input("Select an algorithm to test:\n" +
                  "1. backtrack solve\n" +
                  "2. backtrack solve with forward checking\n" +
                  "3. backtrack solve with arc consistency\n" +
                  "4. local search using simulated annealing with min conflict heuristic\n" +
                  "5. local search using a genetic alg with a penalty function and tournament selection\n" +
                  "6. exit\n")

while selection != '6':

    if selection == '1':  # testing brute-force/backtracking
        print("This is the solution from the backtracking algorithm:\n")
        bt.recursiveBacktrackSolve(puzzle1, 0, 0)
        print("\nThis solution took", bt.resets, "backtracks\n")

    elif selection == '2':  # testing backtracking + forward checking
        print("This is the solution from the backtracking + forward checking algorithm:\n")
        fc.forwardCheck(puzzle2, 0, 0)
        print("\nThis solution took", fc.resets, "backtracks\n")

    elif selection == '3':  # testing backtracking + arc consistency
        print("This is the solution from the backtracking + arc consistency algorithm:\n")
        arc.arc(puzzle2, 0, 0)
        print("\nThis solution took", arc.resets, "backtracks\n")

    elif selection == '4':
        print(test1)
        sa = SimAnneal()
        solution = sa.simulate_annealing(test1)
        print()
        print(solution)
        print(sa.minimum_cost_function(solution))

    elif selection == '5':
        print(test1)
        print()
        ga = GeneticAlgorithm()
        solution = ga.genetic_algorithm(test1)
        print(solution)

        g = Graph(solution)
        print(g.validator())

    selection = input("Select an algorithm to test:\n" +
                      "1. backtrack solve\n" +
                      "2. backtrack solve with forward checking\n" +
                      "3. backtrack solve with arc consistency\n" +
                      "4. local search using simulated annealing with min conflict heuristic\n" +
                      "5. local search using a genetic alg with a penalty function and tournament selection\n" +
                      "6. exit\n")
