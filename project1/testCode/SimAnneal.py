import random
import math

from LocalSearch import LocalSearch

class SimAnneal(LocalSearch):
    
    def __init__(self) -> None:
        self.iterations = 0
        super().__init__()

    def simulate_annealing(self, puzzle):
        """
        Accepts a sudoku puzzle in the form of a 2x2 matrix as its input
        Assigns random values to the non given squares in the puzzle
        Determines the minimum cost of the puzzle -- the number of violated constaints
        
        We generate a new puzzle by swapping two values in the puzzle
        If less constraints are violated we accept our new puzzle
        If more constraints are violated we accept with a constructed probability P
        P is higher during our earlier iterations and decreases as our cooling 
        temperature approaches 0
        """
        puzzle = self.assert_random_values(puzzle)
        print(self.fixed_values)
        T = 1
        print("thinking...")
        while T > 0:    
            self.iterations += 1
            c1 = self.minimum_cost_function(puzzle)

            if c1 == 0:
                return puzzle
            
            new_puzzle = self.swap_random(puzzle)
            c2 = self.minimum_cost_function(new_puzzle)

            delta_e = c2 - c1

            if c1 > c2:
                puzzle = new_puzzle
            elif random.random() < math.exp(-(delta_e/T)):
                puzzle = new_puzzle

            T -= .0001
        
        return puzzle


    
    def minimum_cost_function(self, puzzle):
        """
        Determining the minimum cost of a sudoku
        by checking for duplicate values across 
        rows and columns
        """
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
