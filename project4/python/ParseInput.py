

from MarkovNode import MarkovNode
from MarkovList import MarkovList


input_file = None

# with open("../inputFiles/L-track.txt", "r") as file:
#         input_file = file.readlines()
    
def generate_markov_list(file_name) -> list:

    with open(file_name, "r") as file:
        input_file = file.readlines()
    
    input_file = input_file[1:]
    #print(h, w)

    markov_list = []
    for i, line in enumerate(input_file):
        line = line.strip()
        line_list = list()
        for j, cell in enumerate(line):
            line_list.append(MarkovNode(cell, i, j))

        markov_list.append(line_list)
    
    return markov_list

def display_markov_list(markov_list: list, pos=(0,0)):

    current_x, current_y = pos
    current_condition = markov_list[current_x][current_y].get_condition()

    markov_list[current_x][current_y].set_condition("C")

    for row in markov_list:
        out = ""

        for node in row:
            out += node.get_condition()

        print(out)

    markov_list[current_x][current_y].set_condition(current_condition)
    
    return

def display_markov_accel(markov_list: list, state: MarkovNode):

    current_x, current_y = state.get_position()
    current_condition = markov_list[current_x][current_y].get_condition()

    markov_list[current_x][current_y].set_condition("C")

    for row in markov_list:
        out = ""

        for node in row:
            print(node.acceleration)
            # out += 

        print(out)

    markov_list[current_x][current_y].set_condition(current_condition)
    
    return

# mdp = generate_markov_list("../inputFiles/O-track.txt")
# display_markov_list(mdp)