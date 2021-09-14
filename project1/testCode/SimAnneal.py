import random
import copy
import math

fixed_values = []

def simulate_annealing(puzzle):
    puzzle = assert_random_values(puzzle)
    T = 1
    print("thinking...")
    while T > 0:    
        c1 = minimum_cost_function(puzzle)

        if c1 == 0:
            return puzzle
        
        new_puzzle = swap_random(puzzle)
        c2 = minimum_cost_function(new_puzzle)

        delta_e = c2 - c1

        if c1 > c2:
            puzzle = new_puzzle
            # print(c2)
        elif random.random() < math.exp(-(delta_e/T)):
            puzzle = new_puzzle
            # print(c2)
        # else:
            # print(c1)
        T -= .000001
       
    return puzzle

def generate_randoms(r_sector, c_sector):
    r = random.randint(r_sector, r_sector+2)
    c = random.randint(c_sector, c_sector+2)
    
    while [r,c] in fixed_values:
        r = random.randint(r_sector, r_sector+2)
        c = random.randint(c_sector, c_sector+2) 

    return [r,c]

def swap_random(puzzle):
    new_puzzle = copy.deepcopy(puzzle)

    r_sector = 3 * random.randint(0,2)
    c_sector = 3 * random.randint(0,2)

    r1 = generate_randoms(r_sector, c_sector)
    r2 = generate_randoms(r_sector, c_sector)
    
    while r1 is r2:
        r1 = generate_randoms(r_sector, c_sector)
        r2 = generate_randoms(r_sector, c_sector)
    
    temp = new_puzzle[r1[0]][r1[1]]
    new_puzzle[r1[0]][r1[1]] = new_puzzle[r2[0]][r2[1]]
    new_puzzle[r2[0]][r2[1]] = temp

    # print("swapped " + str(r1) +" for " + str(r2))

    return new_puzzle



def assert_random_values(puzzle):

    for r in [0,3,6]:
        for c in [0,3,6]:
            nums = [1,2,3,4,5,6,7,8,9]

            for i in range(r, r+3):
                for j in range(c, c+3):
                    if puzzle[i][j] != 0:                    
                        nums.remove(puzzle[i][j])
            
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if puzzle[i][j] != 0:
                        fixed_values.append([i,j])
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

def display_puzzle(puzzle):
    for row in puzzle:
        print(row)