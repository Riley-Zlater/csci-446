"""
from ValueIteration2 import value_iteration
from ParseInput import generate_markov_list


O_track = generate_markov_list("../inputFiles/O-track.txt")
L_track = generate_markov_list("../inputFiles/L-track.txt")
R_track = generate_markov_list("../inputFiles/R-track.txt")

iters = 0

policy_list = list()

for num_training in range(10, 101, 10):
    iters += 10
    print(f"training with {iters} iterations\n")
    U, policy = value_iteration(O_track, .0001, .9, num_training, track=False)
    policy_list.append(policy)

iters = 0

for i in policy_list:
    iters += 10
    if i[1] > 200:
        print(f"Number of iters: {iters} - Policy Length: Timed out greater than 200")
    else:
        print(f"Number of iters: {iters} - Policy Length: {i[1]}")
"""

from SARSA import value_iteration
from ParseInput import generate_markov_list

O_track = generate_markov_list("../inputFiles/O-track.txt")
L_track = generate_markov_list("../inputFiles/L-track.txt")
R_track = generate_markov_list("../inputFiles/R-track.txt")

iters = 0

policy_list = list()

for num_training in range(500, 2001, 500):
    iters += 10
    print(f"training with {iters} iterations\n")
    U, policy = value_iteration(L_track, 1, .9, .01, num_training)
    policy_list.append(policy)

iters = 0

for i in policy_list:
    iters += 10
    if i[1] > 200:
        print(f"Number of iters: {iters} - Policy Length: Timed out greater than 200")
    else:
        print(f"Number of iters: {iters} - Policy Length: {i[1]}")