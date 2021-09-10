import random

fixed_values = []

def assert_random_values(puzzle):

    for r in [0,3,6]:
        for c in [0,3,6]:
            nums = [1,2,3,4,5,6,7,8,9]

            for i in range(r, r+3):
                for j in range(c, c+3):
                    nums.remove(puzzle[i][j])
            
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if puzzle[i][j] != 0:
                        fixed_values.append({i,j})
                    if puzzle[i][j] == 0:
                        val = nums[random.randint(0,len(nums)-1)]
                        puzzle[i][j] = val
                        nums.remove(val)
        
    return puzzle


# Determining the minimum cost of a sudoku
# by checking for duplicate values across 
# rows and columns
def minimum_cost_function(puzzle):
    
    cost = 0

    for x in range(0,9):
        row_dups = dict()
        for y in range(0,9):
            if row_dups.has_key(puzzle[x][y]) != False:
                cost += 1
            row_dups[puzzle[x][y]] = 1
    
    for x in range(0,9):
        col_dups = dict()
        for y in range(0,9):
            if col_dups.has_key(puzzle[y][x]) != False:
                cost += 1
            col_dups[puzzle[y][x]] = 1

    return cost

def display_puzzle(puzzle):
    for row in puzzle:
        print(row)