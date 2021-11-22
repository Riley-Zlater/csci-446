

from MarkovNode import MarkovNode
from MarkovList import MarkovList


input_file = None

with open("project4/inputFiles/L-track.txt", "r") as file:
        input_file = file.readlines()
    
def generate_markov_list(file) -> MarkovList:

    f_line = file[0]
    h, w = f_line.split(",")[0], f_line.split(",")[1]

    file = file[1:]
    print(h, w)

    markov_list = MarkovList(w, h)
    #i = 0
    for i, line in enumerate(file):
        line = line.strip()
        #j = 0
        line_list = list()
        for j, cell in enumerate(line):
            state = transform_state(cell)
            line_list.append(MarkovNode(state, i, j))
            #j+=1
        #i += 1
        markov_list.insert_list(line_list)
    
    return markov_list
        
def transform_state(cell: str):
    if cell == "#":
        return "wall"
    if cell == ".":
        return "empty"
    if cell == "S":
        return "start"
    if cell == "F":
        return "finish"


markov_list = generate_markov_list(input_file)

markov_list.display_markov_contents()

