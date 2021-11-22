

from MarkovNode import MarkovNode
from MarkovList import MarkovList


input_file = None

with open("../inputFiles/L-track.txt", "r") as file:
        input_file = file.readlines()
    
def generate_markov_list(file) -> MarkovList:

    f_line = file[0]
    h, w = f_line.split(",")[0], f_line.split(",")[1]
    
    file = file[1:]
    print(h, w)

    markov_list = MarkovList(w, h)
    i = 0
    for line in file:
        print(line)
        j = 0
        line_list = list()
        for cell in line:
            state = get_state(cell)
            line_list.append(MarkovNode(state, i, j))
            j+=1
        i += 1
        markov_list.insert_list(line_list)
    
    return markov_list
        
def get_state(cell: str):
    if cell == "#":
        return "w"
    if cell == ".":
        return "e"
    if cell == "S":
        return "s"
    if cell == "F":
        return "f"


markov_list = generate_markov_list(input_file)

markov_list.display_markov_list()

