from ParseInput import generate_markov_list
from MarkovList import MarkovList

with open("../inputFiles/L-track.txt", "r") as file:
        input_file = file.readlines()

def value_iteration(mdp: MarkovList, e: float):
    print(mdp.get_height())
    U = [[0 for x in range(mdp.get_width())] for y in range(mdp.get_height())]
    U_prime = [[0 for x in range(mdp.get_width())] for y in range(mdp.get_height())]

    for row in U:
        print(row)


mdp = generate_markov_list(input_file)
value_iteration(mdp, 0.0)