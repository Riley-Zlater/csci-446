from os import curdir
from ParseInput import generate_markov_list
from MarkovList import MarkovList
from MarkovNode import MarkovNode
import copy

with open("../inputFiles/L-track.txt", "r") as file:
        input_file = file.readlines()

def value_iteration(mdp: MarkovList, e: float, discount_factor: float):

    # local variables
    max_rel_change = int()
    U = mdp
    U_prime = copy.deepcopy(U)


    # for line in U:
    #     print(line)

    # Begin value iteration
    while True:
        max_rel_change = 0.0
        U = U_prime
        U.display_markov_list()
        for utility_line in U.get_markov_list():
            for state in utility_line:
                possible_actions =     [(0, 0),   (0, 1),  (0, -1), 
                                        (1, 1),   (1, 0),  (-1, 0), 
                                        (-1, -1), (-1, 1), (1, -1)]
                max = 0.0
                best_move = None
                best_acceleration = (0, 0)
                best_velocity = (0,0)

                # prune poss actions
                for action in possible_actions:
                    x_a, y_a = action
                    curr_v_x, curr_v_y = state.get_velocity()
                    if -5 > x_a + curr_v_x > 5 or -5 > y_a + curr_v_y > 5:
                        possible_actions.remove(action)

                # pass actions through q value function
                for action in possible_actions:
                    q_val, s_prime = q_value(U_prime, state, action, discount_factor)
                    if q_val > max:
                        max = q_val
                        best_move = s_prime
                        best_acceleration = action
                        best_velocity = tuple(map(sum, state.get_velocity(), best_acceleration))

                # update U prime
                U_prime.get_markov_node(state).set_utility(max)
                U_prime.get_markov_node(state).set_best_move(best_move)
                U_prime.get_markov_node(state).set_acceleration(best_acceleration)
                U_prime.get_markov_node(state).set_velocity(best_velocity)

                # check for new max relative change
                u_diff = abs(U_prime.get_markov_node(state).utility - U.get_markov_node(state).utility)
                if u_diff > max_rel_change:
                    max_rel_change = u_diff
        
        # check for convergence
        if max_rel_change <= (e(1 - discount_factor))/discount_factor:
            break

    return U

def q_value(mdp: MarkovList, s: MarkovNode, a: tuple, discount_factor: float):
    x_acceleration, y_acceleration = a

    curr_x, curr_y = s.get_position()
    curr_v_x, curr_v_y = s.get_velocity()

    x_prime = curr_x + x_acceleration + curr_v_x
    y_prime = curr_y + y_acceleration + curr_v_y

    s_prime = mdp.get_node(x_prime, y_prime)

    u_value = (0.8 * (-1 + discount_factor * s_prime.utility)) + (0.2 * (-1 + discount_factor * s.utility))

    return u_value, s_prime
    

mdp = generate_markov_list(input_file)
value_iteration(mdp, 0.05, 0.1)