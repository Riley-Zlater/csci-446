import random
import math

from LocalSearch import LocalSearch

class SimAnneal(LocalSearch):
    
    def __init__(self) -> None:
        super().__init__()

    def simulate_annealing(self, puzzle):
        puzzle = self.assert_random_values(puzzle)
        T = 1
        print("thinking...")
        while T > 0:    
            c1 = self.minimum_cost_function(puzzle)

            if c1 == 0:
                return puzzle
            
            new_puzzle = self.swap_random(puzzle)
            c2 = self.minimum_cost_function(new_puzzle)

            delta_e = c2 - c1

            if c1 > c2:
                puzzle = new_puzzle
                # print(c2)
            elif random.random() < math.exp(-(delta_e/T)):
                puzzle = new_puzzle
                # print(c2)
            # else:
                # print(c1)
            T -= .0001
        
        return puzzle


    # Determining the minimum cost of a sudoku
    # by checking for duplicate values across 
    # rows and columns
    def minimum_cost_function(self, puzzle):
        
        cost = 0

        for x in range(0,9):
            row_dups = dict()
            for y in range(0,9):
                if puzzle[x][y] in row_dups:
                    cost += 1
                row_dups[puzzle[x][y]] = 1
        
        for x in range(0,9):
            col_dups = dict()
            for y in range(0,9):
                if puzzle[y][x] in col_dups:
                    cost += 1
                col_dups[puzzle[y][x]] = 1

        return cost
