

from MarkovNode import MarkovNode
from MarkovList import MarkovList


input_file = None

with open("../inputFiles/L-track.txt", "r") as file:
        input_file = file.readlines()
    
def generate_markov_list(file) -> MarkovList:

    f_line = file[0]
    h, w = int(f_line.split(",")[0]), int(f_line.split(",")[1])
    
    file = file[1:]
    #print(h, w)

    markov_list = MarkovList(w, h)
    for i, line in enumerate(file):
        line = line.strip()
        line_list = list()
        for j, cell in enumerate(line):
            condition = transform_state(cell)
            line_list.append(MarkovNode(condition, i, j))

        markov_list.insert_list(line_list)
    
    return markov_list
        
def transform_state(cell: str):
    if cell == "#":
        return "w"
    if cell == ".":
        return "e"
    if cell == "S":
        return "s"
    if cell == "F":
        return "f"


# markov_list = generate_markov_list(input_file)

# markov_list.display_markov_contents()

# markov_list.display_markov_list()