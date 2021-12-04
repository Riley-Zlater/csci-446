#from os import curdir
from ParseInput import generate_markov_list
from MarkovList import MarkovList
from MarkovNode import MarkovNode
import copy

with open("../inputFiles/O-track.txt", "r") as file:
        input_file = file.readlines()
        
temp_counter = 0
def value_iteration(mdp: MarkovList, e: float, discount_factor: float):

    # local variables
    global temp_counter
    U = copy.deepcopy(mdp)
    U_prime = copy.deepcopy(U)

    # Begin value iteration
    for utility_line in U.get_markov_list():
            for state in utility_line:
                state.check_and_set_utility()
    
    for utility_line in U_prime.get_markov_list():
            for state in utility_line:
                state.check_and_set_utility()

    while True:
    # while temp_counter <= 1000:
        temp_counter += 1
        max_rel_change = 0.0
        U = copy.deepcopy(U_prime)
        U.display_markov_list()
        print()
        for utility_line in U.get_markov_list():
            for state in utility_line:
                if state.get_condition() in ["w", "f"]:
                    continue
                
                max_value = 0.0
                best_move = None
                best_acceleration = (0, 0)
                best_velocity = state.get_velocity()
                state.prune_poss_actions()

                # pass actions through q value function
                for action in state.get_possible_actions():
                    # best_acceleration = (0, 0)
                    # best_velocity = state.get_velocity()
                    q_val, s_prime = q_value(U_prime, state, action, discount_factor)
                    if q_val > max_value:
                        max_value = q_val
                        best_move = s_prime
                        best_acceleration = action
                        best_velocity = tuple(sum(val) for val in zip(list(state.get_velocity()), list(best_acceleration)))

                # update U prime
                U_prime.get_markov_node(state).set_utility(max_value)
                U_prime.get_markov_node(state).set_best_move(best_move)
                U_prime.get_markov_node(state).set_acceleration(best_acceleration)
                U_prime.get_markov_node(state).set_velocity(best_velocity)

                # check for new max relative change
                u_diff = abs(U_prime.get_markov_node(state).utility - U.get_markov_node(state).utility)
                if u_diff > max_rel_change:
                    max_rel_change = u_diff

        # check for convergence
        if max_rel_change <= (e*(1 - discount_factor))/discount_factor :
            U = copy.deepcopy(U_prime)
            break

    return U

def q_value(mdp: MarkovList, s: MarkovNode, a: tuple, discount_factor: float):
    x_acceleration, y_acceleration = a

    curr_x, curr_y = s.get_position()
    curr_v_x, curr_v_y = s.get_velocity()

    x_prime = curr_x + x_acceleration + curr_v_x
    y_prime = curr_y + y_acceleration + curr_v_y

    s_prime = mdp.get_node(x_prime, y_prime)

    u_value = (0.8 * (1 + discount_factor * s_prime.utility)) + (0.2 * (1 + discount_factor * s.utility)) - 1

    return u_value, s_prime


def define_policy(U: MarkovList):
    steps = 0
    policy = list()
    velocity = list()
    state_space = U.get_markov_list()

    state = find_start(state_space)

    while state.get_condition() != 'f':
        policy.append(state.get_position())
        velocity.append(state.get_velocity())
        state = state.best_move
        steps += 1        

    policy.append(state.get_position())
    velocity.append(state.get_velocity())
    steps += 1

    return policy, velocity, steps

def find_start(state_space: list) -> MarkovNode:
    for state_line in state_space:
        for state in state_line:
            if state.get_condition() == 's':
                return state

mdp = generate_markov_list(input_file)
sol = value_iteration(mdp, 1, 0.99)
sol.display_markov_list_best_move()
print()
sol.display_markov_list_velocity()
print()
sol.display_markov_list_acceleration()
print()

print(define_policy(sol))

# print(temp_counter)