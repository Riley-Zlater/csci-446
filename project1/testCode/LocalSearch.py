from collections import OrderedDict
import random

csp = OrderedDict()
concrete_entries = dict()
letters = ["A", "B", "C", "D","E","F","G","H","I"]


def simulated_annealing(puzzle):
    construct_csp(puzzle)

    while True:
        node = letters[random.randint(0,9)] + str(random.randint(0,9))
        if concrete_entries[node] == 1:
            continue
        min_conflict = find_min_conflict(node)
        csp[node] = min_conflict

    return

# Construct the CSP graph
# Inserts random values into the graph 
# where the value is equal to 0
# Keeps track of start state values 
# in concrete_entries dictionary
def construct_csp(puzzle):
    for x in range(0, 9):
        for y in range(0, 9):
            csp_item = letters[x] + str(y)
            if puzzle[x][y] != 0:
                csp[csp_item] = puzzle[x][y]
                concrete_entries[csp_item] = 1
            else:
                csp[csp_item] = random.randint(0,9)


def count_conflicts(node, k):
    conflicts = 0

    letter = node[0]
    number = node[1]

    for v in range(0,9):
        temp = letter + str(v)
        if temp == node:
            continue
        if csp[temp] == k:
            conflicts += 1

    for l in letters:
        temp = l + str(number)
        if temp == node:
            continue
        if csp[temp] == k:
            conflicts += 1

    i = letters.index(letter)
    i = 3 * (i // 3)

    j = 3 * (int(number) // 3)

    split_array = letters[i:i+3]
    
    for l in split_array:
        for v in range(j, j+3):
            temp = l + str(v)
            if temp == node:
                continue
            if csp[temp] == k:
                conflicts +=1
    
    return conflicts
    

def find_min_conflict(node):
    conflict_list = {}
    for k in range(9):
        conflict_list[k] = count_conflicts(node, k)

    return min(conflict_list, key=conflict_list.get)

def print_csp():
    for i in csp:
        print(i, csp[i])
        

# Assert random values to zero values
# def random_assign(puzzle):
#     for x in range(0, 9):
#         for y in range(0, 9):
#             if puzzle[x][y] == 0:
#                 puzzle[x][y] = random.randint(0,9)
#     return puzzle

# Determine conflicts using arrays
# def count_conflicts(puzzle, i, j, k):
#     conflicts = 0

#     for v in range(9):
#         if k == puzzle[i][v]:
#             conflicts += 1

#     for v in range(9):
#         if k == puzzle[v][j]:
#             conflicts += 1

#     topX = 3 * (i // 3)
#     topY = 3 * (j // 3)
#     for x in range(topX, topX + 3):
#         for y in range(topY, topY + 3):
#             if puzzle[x][y] == k:
#                 conflicts += 1