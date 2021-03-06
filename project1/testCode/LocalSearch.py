import random
import copy
from operator import itemgetter

from numpy import empty

class LocalSearch:
    
    def __init__(self) -> None:
        self.fixed_values = []

    def generate_fixed_values(self, puzzle):  
        """
        Iterates through a starting puzzle and creates an array
        based on the sudoku's given values
        This array is used to prevent swaps with original puzzle
        values
        """   
        for i in range(0, 9):
            for j in range(0, 9):
                if puzzle[i][j] != 0:
                    self.fixed_values.append([i,j])
            
        return puzzle

    
    def assert_random_values(self, puzzle):
        """
        This function accepts a sudoku puzzle and asserts random values
        onto the puzzle's empty spaces. 

        The puzzle inserts the values [1-9] into each "sub-square" such that
        we create pseudo random puzzles with the 3x3 constraint already fulfilled
        """

        if not self.fixed_values:
            self.generate_fixed_values(puzzle)

        for r in [0,3,6]:
            for c in [0,3,6]:
                nums = [1,2,3,4,5,6,7,8,9]

                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if puzzle[i][j] != 0:                    
                            nums.remove(puzzle[i][j])
                
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if puzzle[i][j] == 0:
                            val = nums[random.randint(0,len(nums)-1)]
                            puzzle[i][j] = val
                            nums.remove(val)
            
        return puzzle
    

    def generate_randoms(self, r_sector, c_sector):
        """
        Accepts two parameters determining the sector for selection
        Selects two random indices [i,j] within a subsquare
        Prevents the selection of indices matching those in the fixed
        values array.
        Returns the selected indices
        """

        r = random.randint(r_sector, r_sector+2)
        c = random.randint(c_sector, c_sector+2)
        
        while [r,c] in self.fixed_values:
            r = random.randint(r_sector, r_sector+2)
            c = random.randint(c_sector, c_sector+2) 

        return [r,c]

    def swap_random(self, puzzle):
        """
        Accepts a sudoku puzzle as input
        Generates a selection for the subsquare in which
        swapping will occur. 
        Swaps the values of the two cells.
        Returns an updated puzzle
        """
        new_puzzle = copy.deepcopy(puzzle)

        r_sector = 3 * random.randint(0,2)
        c_sector = 3 * random.randint(0,2)

        r1 = self.generate_randoms(r_sector, c_sector)
        r2 = self.generate_randoms(r_sector, c_sector)
        
        while r1 is r2:
            r1 = self.generate_randoms(r_sector, c_sector)
            r2 = self.generate_randoms(r_sector, c_sector)
        
        temp = new_puzzle[r1[0]][r1[1]]
        new_puzzle[r1[0]][r1[1]] = new_puzzle[r2[0]][r2[1]]
        new_puzzle[r2[0]][r2[1]] = temp

        # print("swapped " + str(r1) +" for " + str(r2))

        return new_puzzle
    
    def display_puzzle(puzzle):
        for row in puzzle:
            print(row)