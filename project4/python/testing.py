#Written by Cooper Strahan and Riley Slater
"""
Testing Value Iteration algorithm

to test value iteration we have it iterate 
from 10 to 100 times stepping by 10

from ValueIteration import value_iteration
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

"""
Testing SARSA Algorithm

to test the sarsa algorithm we have iterate
from 500 to 2000 stepping by 500
"""
from SARSA import sarsa
from ParseInput import generate_markov_list

O_track = generate_markov_list("../inputFiles/O-track.txt")
L_track = generate_markov_list("../inputFiles/L-track.txt")
R_track = generate_markov_list("../inputFiles/R-track.txt")

iters = 0

policy_list = list()


for num_training in range(500, 2001, 500):
    iters += 500
    print(f"training with {iters} iterations\n")
    U, policy = sarsa(O_track, 1, .9, .01, num_training, track=False)
    policy_list.append(policy)

iters = 0

for i in policy_list:
    iters += 500
    if i[1] > 200:
        print(f"Number of iters: {iters} - Policy Length: Timed out greater than 200")
    else:
        print(f"Number of iters: {iters} - Policy Length: {i[1]}")



num_iters = [i for i in range(10, 101, 10)]
L_policies = [16 for _ in range(10)]
R_policies = [200, 200, 56, 34, 45, 34, 34, 32, 46, 32]
R_policies_reset = [200, 200, 46, 34, 56, 56, 46, 32, 46, 56]
O_policies = [200, 34, 37, 34, 33, 33, 33, 34, 34, 33]

import matplotlib.pyplot as plt

plt.plot(num_iters, L_policies, marker="o", label="L-track")
plt.plot(num_iters, R_policies, marker="o", label="R-track Soft Reset")
plt.plot(num_iters, R_policies_reset, marker="o", label="R-track Hard Reset")
plt.plot(num_iters, O_policies, marker="o", label="O-track")
plt.xticks(num_iters)
plt.title("Value Iteration")
plt.xlabel("Number of Training Iterations")
plt.ylabel("Length of Policy")
plt.legend()
plt.show()
