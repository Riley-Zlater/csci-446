#Written by Riley Slater and Cooper Strahan

import puzzleImporter as puz
import backtrackSolve as bt
import arc as arc
from SimAnneal import SimAnneal
from graph import Graph
import forwardCheck as fc
from GeneticAlgorithm import GeneticAlgorithm

# test1 = puz.importPuzzle("..\\testPuzzles\\Hard-P1.csv")

test1 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P5.csv")
puzzle1 = Graph(test1)

selection = input("Select an algorithm to test:\n"+
                  "1. backtrack solve\n"+
                  "2. backtrack solve with forward checking\n"+
                  "3. backtrack solve with arc consistency\n"+
                  "4. local search using simulated annealing with min conflict heuristic\n"+
                  "5. local search using a genetic alg with a penalty function and tournament selection\n"+
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
    
elif (selection == '4'):
    print(test1)
    sa = SimAnneal()
    solution = sa.simulate_annealing(test1)
    print()
    print(solution)
    print(sa.minimum_cost_function(solution))

elif (selection == '5'):
    print(test1)
    print()
    ga = GeneticAlgorithm()
    fitness = ga.genetic_algorithm(test1)
    print(fitness)

