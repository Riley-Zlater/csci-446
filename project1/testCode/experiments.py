import numpy as np
from scipy import stats
import puzzleImporter as puz
import backtrackSolve as bt
import arc as arc
from SimAnneal import SimAnneal
from graph import Graph
import forwardCheck as fc
from GeneticAlgorithm import GeneticAlgorithm

ez1 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P1.csv")
ez2 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P2.csv")
ez3 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P3.csv")
ez4 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P4.csv")
ez5 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Easy-P5.csv")

m1 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Med-P1.csv")
m2 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Med-P2.csv")
m3 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Med-P3.csv")
m4 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Med-P4.csv")
m5 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Med-P5.csv")

h1 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Hard-P1.csv")
h2 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Hard-P2.csv")
h3 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Hard-P3.csv")
h4 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Hard-P4.csv")
h5 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Hard-P5.csv")

ev1 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Evil-P5.csv")
ev2 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Evil-P5.csv")
ev3 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Evil-P5.csv")
ev4 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Evil-P5.csv")
ev5 = puz.importPuzzle("/Users/cooperstrahan/School/csci-446/project1/testPuzzles/Evil-P5.csv")

easy_puzzles = [ez1, ez2, ez3, ez4, ez5]
med_puzzles = [m1, m2, m3, m4, m5]
hard_puzzles = [h1,h2, h3, h4, h5]
evil_puzzles = [ev1, ev2, ev3, ev4, ev5]

easy_simple_backtrack_results = []
easy_backtrack_forwardtrack_results = []
easy_backtrack_arc_consistency_results = []

easy_simulated_annealing_results = []
easy_genetic_algorithm_results = []

med_simple_backtrack_results = []
med_backtrack_forwardtrack_results = []
med_backtrack_arc_consistency_results = []

med_simulated_annealing_results = []
med_genetic_algorithm_results = []

hard_backtrack_forwardtrack_results = []
hard_backtrack_arc_consistency_results = []

hard_simulated_annealing_results = []
hard_genetic_algorithm_results = []

# evil_simple_backtrack_results = []
evil_backtrack_forwardtrack_results = []
evil_backtrack_arc_consistency_results = []

evil_simulated_annealing_results = []
evil_genetic_algorithm_results = []


for _ in range(0,10):

    for easy_sudoku in easy_puzzles:
        graph = Graph(easy_sudoku)
        bt.recursiveBacktrackSolve(graph, 0, 0)
        easy_simple_backtrack_results.append(bt.resets)
        fc.forwardCheck(graph, 0, 0)
        easy_backtrack_forwardtrack_results.append(fc.resets)
        arc.arc(graph, 0, 0)
        easy_backtrack_arc_consistency_results.append(arc.resets)
        sa = SimAnneal()
        solution = sa.simulate_annealing(easy_sudoku)
        easy_simulated_annealing_results.append(sa.minimum_cost_function(solution))

    for med_sudoku in med_puzzles:
        graph = Graph(med_sudoku)
        bt.recursiveBacktrackSolve(graph, 0, 0)
        med_simple_backtrack_results.append(bt.resets)
        fc.forwardCheck(graph, 0, 0)
        med_backtrack_forwardtrack_results.append(fc.resets)
        arc.arc(graph, 0, 0)
        med_backtrack_arc_consistency_results.append(arc.resets)
        sa = SimAnneal()
        solution = sa.simulate_annealing(med_sudoku)
        med_simulated_annealing_results.append(sa.minimum_cost_function(solution))

    for hard_sudoku in hard_puzzles:
        graph = Graph(hard_sudoku)
        fc.forwardCheck(graph, 0, 0)
        hard_backtrack_forwardtrack_results.append(fc.resets)
        arc.arc(graph, 0, 0)
        hard_backtrack_arc_consistency_results.append(arc.resets)
        sa = SimAnneal()
        solution = sa.simulate_annealing(hard_sudoku)
        hard_simulated_annealing_results.append(sa.minimum_cost_function(solution))

    for evil_sudoku in evil_puzzles:
        graph = Graph(evil_sudoku)
        fc.forwardCheck(graph, 0, 0)
        evil_backtrack_forwardtrack_results.append(fc.resets)
        arc.arc(graph, 0, 0)
        evil_backtrack_arc_consistency_results.append(arc.resets)
        sa = SimAnneal()
        solution = sa.simulate_annealing(evil_sudoku)
        evil_simulated_annealing_results.append(sa.minimum_cost_function(solution))

easy_simple_backtrack_results = np.array(easy_simple_backtrack_results)
easy_backtrack_forwardtrack_results = np.array(easy_backtrack_forwardtrack_results)
easy_backtrack_arc_consistency_results = np.array(easy_backtrack_arc_consistency_results)
easy_simulated_annealing_results = np.array(easy_simulated_annealing_results)

med_simple_backtrack_results = np.array(med_simple_backtrack_results)
med_backtrack_forwardtrack_results = np.array(med_backtrack_forwardtrack_results)
med_backtrack_arc_consistency_results = np.array(med_backtrack_arc_consistency_results)
med_simulated_annealing_results = np.array(med_simulated_annealing_results)

hard_backtrack_forwardtrack_results = np.array(hard_backtrack_forwardtrack_results)
hard_backtrack_arc_consistency_results = np.array(hard_backtrack_arc_consistency_results)
hard_simulated_annealing_results = np.array(hard_simulated_annealing_results)

evil_backtrack_forwardtrack_results = np.array(evil_backtrack_forwardtrack_results)
evil_backtrack_arc_consistency_results = np.array(evil_backtrack_arc_consistency_results)
evil_simulated_annealing_results = np.array(evil_simulated_annealing_results)

print("Easy Results")
print(stats.describe(easy_simple_backtrack_results))
print(stats.describe(easy_backtrack_forwardtrack_results))
print(stats.describe(easy_backtrack_arc_consistency_results))
print(stats.describe(easy_simulated_annealing_results))

print("Medium Results")
print(stats.describe(med_simple_backtrack_results))
print(stats.describe(med_backtrack_forwardtrack_results))
print(stats.describe(med_backtrack_arc_consistency_results))
print(stats.describe(med_simulated_annealing_results))

print("Hard Results")
print(stats.describe(hard_backtrack_forwardtrack_results))
print(stats.describe(hard_backtrack_arc_consistency_results))
print(stats.describe(hard_simulated_annealing_results))

print("Evil Results")
print(stats.describe(evil_backtrack_forwardtrack_results))
print(stats.describe(evil_backtrack_arc_consistency_results))
print(stats.describe(evil_simulated_annealing_results))
