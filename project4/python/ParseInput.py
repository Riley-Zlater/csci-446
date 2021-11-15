

from MarkovNode import MarkovNode


input_file = None

with open("../inputFiles/L-track.txt", "r") as file:
        input_file = file.readlines()
    
f_line = input_file[0]
height, width = f_line.split(",")[0], f_line.split(",")[1]

input_file = input_file[1:]
print(height, width)

markov_list = list()

def get_state(cell: str):
    if cell == "#":
        return "wall"
    if cell == ".":
        return "empty"
    if cell == "S":
        return "start"
    if cell == "F":
        return "finish"

i = 0
for line in input_file:
    j = 0
    for cell in line:
        state = get_state(cell)
        markov_list.append(MarkovNode(state, i, j))
        j+=1
    i += 1
        


