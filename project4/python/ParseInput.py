

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
<<<<<<< HEAD
    #i = 0
    for i, line in enumerate(file):
        line = line.strip()
        #j = 0
=======
    i = 0
    for line in file:
        print(line)
        j = 0
>>>>>>> 87424b95b6d4d9ba1f9bd92f1b4cc9c996ae173c
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
        return "w"
    if cell == ".":
        return "e"
    if cell == "S":
        return "s"
    if cell == "F":
        return "f"


markov_list = generate_markov_list(input_file)

<<<<<<< HEAD
markov_list.display_markov_contents()
=======
markov_list.display_markov_list()
>>>>>>> 87424b95b6d4d9ba1f9bd92f1b4cc9c996ae173c

