# Written by Cooper Strahan and Riley Slater
from math import sqrt
import numpy as np
from ParseInput import generate_markov_list, display_markov_list
from MarkovNode import MarkovNode
import copy
import random
import time


def new_starting_position(mdp: list) -> tuple:
    """
    Randomly choose a new start state
    """
    start_list = list()

    for x, row in enumerate(mdp):
        for y, _ in enumerate(row):
            if mdp[x][y].get_condition() == 'S':
                start_list.append((x, y))
    
    start_pos = random.choice(start_list)
    return start_pos


def crash_handler(mdp: list, state: MarkovNode, s_prime: MarkovNode, course_reset=False) -> MarkovNode:
    """
    This function resets the car to the finish line if course_reset is true 
    otherwise uses the euclidian distance to find the nearest safe state.
    Resets car velocity to (0, 0)
    """

    width = len(mdp) - 1
    height = len(mdp[0]) - 1

    if s_prime.get_wall_condition() and not course_reset:
        s_prime_x, s_prime_y = s_prime.get_position()
        s_prime_x_velocity, s_prime_y_velocity = s_prime.get_velocity()


        x_range = s_prime_x - s_prime_x_velocity
        y_range = s_prime_y - s_prime_y_velocity
    

        min_distance = max(width, height) 
        min_position = state.get_position()

        for x in range(x_range, s_prime_x):
            for y in range(y_range, s_prime_y):
                if x < 0: x = 0 
                if x > width: x = width
                if y < 0: y = 0
                if y > height: y = height

                if mdp[x][y].get_condition() == '.':
                    distance = euclidean_distance(x, y, state)
                    if distance < min_distance:
                        min_distance = distance
                        min_position = mdp[x][y]
    elif course_reset:
        min_position = new_starting_position(mdp)

    return min_position

def euclidean_distance(x_pos: int, y_pos: int, state: MarkovNode) -> float:
    """
    Calculate euclidian distance
    """
    c_x, c_y = state.get_position()
    return sqrt(((x_pos - c_x)**2) + (y_pos - c_y)**2)

def take_action(mdp: list, state: MarkovNode, acceleration: tuple) -> MarkovNode:
    """
    this function will apply an acceleration to the velocity determining
    where the car will be after current velocity + acceleration
    """
    width = len(mdp) - 1
    height = len(mdp[0]) - 1

    x_acceleration, y_acceleration = acceleration

    x_position, y_position = state.get_position()
    x_velocity, y_velocity = state.get_velocity()

    x_velocity = x_velocity + x_acceleration 
    y_velocity = y_velocity + y_acceleration

    state.set_velocity((x_velocity, y_velocity))

    x_new_velocity, y_new_velocity = state.get_velocity()
    
    new_x_position = x_position + x_new_velocity
    new_y_position = y_position + y_new_velocity

    if new_x_position < 0: new_x_position = 0
    if new_x_position > width: new_x_position = width
    if new_y_position < 0: new_y_position = 0
    if new_y_position > height: new_y_position = height

    s_prime = mdp[new_x_position][new_y_position]

    if s_prime.get_wall_condition():
        new_x, new_y = crash_handler(mdp, state, s_prime)
        s_prime = mdp[new_x][new_y]
        x_new_velocity = 0
        y_new_velocity = 0


    s_prime.set_velocity((x_new_velocity, y_new_velocity))

    return s_prime

def determine_illegal_move(mdp: list, state: MarkovNode, s_prime: MarkovNode) -> bool:
    """
    This function checks to see if the next state given the 
    current velocity and acceleration is a wall or not
    """

    position_list = [state, s_prime]

    state_x_pos, state_y_pos = state.get_position()
    s_prime_x_pos, s_prime_y_pos = s_prime.get_position()

    x_distance = s_prime_x_pos - state_x_pos 
    y_distance = s_prime_y_pos - state_y_pos

    x_factor = 1 if x_distance > 0 else -1 if x_distance < 0 else 0
    y_factor = 1 if y_distance > 0 else -1 if y_distance < 0 else 0


    current_x, current_y = state_x_pos, state_y_pos

    x_iter = 1 * x_factor
    y_iter = 1 * y_factor

    while current_x != s_prime_x_pos or current_y != s_prime_y_pos:

        if current_x == s_prime_x_pos:
            x_iter = 0
        
        if current_y == s_prime_y_pos:
            y_iter = 0


        current_x += x_iter
        current_y += y_iter

        position_list.append(mdp[current_x][current_y])

    for node in position_list:
        if node.get_wall_condition():
            return True

    return False

def determine_overshoot_finish(mdp: list, state: MarkovNode, s_prime: MarkovNode) -> bool:
    """
    This function checks to see if the car over shoots the finish
    """

    position_list = [state, s_prime]

    state_x_pos, state_y_pos = state.get_position()
    s_prime_x_pos, s_prime_y_pos = s_prime.get_position()

    x_distance = s_prime_x_pos - state_x_pos 
    y_distance = s_prime_y_pos - state_y_pos

    x_factor = 1 if x_distance > 0 else -1 if x_distance < 0 else 0
    y_factor = 1 if y_distance > 0 else -1 if y_distance < 0 else 0


    current_x, current_y = state_x_pos, state_y_pos

    x_iter = 1 * x_factor
    y_iter = 1 * y_factor

    while current_x != s_prime_x_pos or current_y != s_prime_y_pos:

        if current_x == s_prime_x_pos:
            x_iter = 0
        
        if current_y == s_prime_y_pos:
            y_iter = 0


        current_x += x_iter
        current_y += y_iter

        position_list.append(mdp[current_x][current_y])

    for node in position_list:
        if node.get_finish_condition():
            return True

        if node.get_wall_condition():
            return False

    return False

def value_iteration(mdp: list, err: float, discount_factor: float, counter: int, track=True) -> list and list:
    """
    This function performs value iteration on the race track to 
    deterimine the optimal policy for the car
    """
    policy = list()

    U = [[[[0.0 for _ in range(-5, 6)] for _ in range(-5, 6)] for _ in row] for row in mdp]
    U_prime = copy.deepcopy(U)

    training_count = 0
    
    while True and training_count < counter:
        training_count += 1
        U = copy.deepcopy(U_prime)
        print_values(U, len(U), len(U[0]), training_count)


        max_rel_change = 0.0

        actions = [(0, 0),   (0, 1),  (0, -1), 
                   (1, 1),   (1, 0),  (-1, 0), 
                   (-1, -1), (-1, 1), (1, -1)]
        

        for row in range(len(mdp)):
            for col in range(len(mdp[0])):
                for x_velocity in range(-5,6):
                    for y_velocity in range(-5,6):
                        if mdp[row][col].get_wall_condition():
                            U_prime[row][col][x_velocity][y_velocity] = -10.0
                            continue
                        if mdp[row][col].get_finish_condition():
                            U_prime[row][col][x_velocity][y_velocity] = 0.0
                            continue 
                        
        for row in range(len(mdp)):
            for col in range(len(mdp[0])):
                for x_velocity in range(-5,6):
                    for y_velocity in range(-5,6):
                        if mdp[row][col].get_wall_condition() == False and mdp[row][col].get_finish_condition() == False:
                            mdp[row][col].set_velocity((x_velocity, y_velocity))
                            new_U_prime, new_acceleration = q_value(mdp, mdp[row][col], actions, U, discount_factor, track)
                            U_prime[row][col][x_velocity][y_velocity] = new_U_prime
                            mdp[row][col].set_acceleration(new_acceleration)
                            mdp[row][col].add_acceleration((x_velocity, y_velocity), new_acceleration)
        
        
        
        for row in range(len(mdp)):
            for col in range(len(mdp[0])):
                for x_velocity in range(-5,6):
                    for y_velocity in range(-5,6):
                        if mdp[row][col].get_finish_condition():
                            U_prime[row][col][x_velocity][y_velocity] = 0.0
                        change = abs(U[row][col][x_velocity][y_velocity] - U_prime[row][col][x_velocity][y_velocity])
                        if change > max_rel_change:
                            max_rel_change = change
        
        if max_rel_change < (err*(1 - discount_factor))/discount_factor:
            break
    
    U = copy.deepcopy(U_prime)
    mdp = update_mdp(mdp, U, len(U), len(U[0]))
    policy = simulate(mdp)
    print(policy)

    return U, policy


def q_value(mdp: list, state: MarkovNode, actions: list, U: list, discount_factor: float, track=True) -> float and tuple:
    """
    This function determines the utility value of a state action pair
    """

    best_utility = -10.0
    best_action = (0,0)
    old_x, old_y = state.get_position()
    old_x_velocity, old_y_velocity = state.get_velocity()

    actions = prune_actions(mdp, state, actions)

    for a in actions:
        s_prime = take_action(mdp, state, a)
        new_x, new_y = s_prime.get_position()
        new_x_velocity, new_y_velocity = s_prime.get_velocity()
        
        reward = 0 if s_prime.get_finish_condition() else -1

        # POSSIBLE U VALUE FIX FOR O TRACK
        if determine_illegal_move(mdp, state, s_prime):
            u_value = -10.0            
        else:
            u_value = reward + (0.8 * discount_factor * U[new_x][new_y][new_x_velocity][new_y_velocity])  \
                + (0.2 * discount_factor  * U[old_x][old_y][old_x_velocity][old_y_velocity])

        if track:
            if u_value > best_utility:
                best_utility = u_value
                best_action = a
        else:
            if u_value >= best_utility:
                best_utility = u_value
                best_action = a
            

    return best_utility, best_action


def prune_actions(mdp: list, state: MarkovNode, actions: list) -> list:
    """
    This function removes poor utility actions from a state
    """
    width = len(mdp) - 1
    height = len(mdp[0]) - 1
    pruned_actions = copy.deepcopy(actions)

    for action in actions:
        x_v, y_v = state.get_velocity()
        x_p, y_p = state.get_position()
        x_a, y_a = action
        new_x = x_p + x_v + x_a
        new_y = y_p + y_v + y_a

        if new_x < 0: new_x = 0
        if new_x > width: new_x = width
        if new_y < 0: new_y = 0
        if new_y > height: new_y = height

        if mdp[new_x][new_y].get_condition() == '#':
            pruned_actions.remove(action)

    return pruned_actions

def print_values(utility_array: list, row: int, col: int, i: int) -> None:
    """
    This function prints the utility values of the states
    """

    utility_two_dim = np.zeros([row, col])
    
    for row in range(len(utility_array)):
        for col in range(len(utility_array[0])):
            max = -10
            for x_velocity in range(-5,6):
                for y_velocity in range(-5,6):
                    if utility_array[row][col][x_velocity][y_velocity] > max:
                        max = utility_array[row][col][x_velocity][y_velocity]
            utility_two_dim[row][col] = max

    for x in utility_two_dim:
        line = ""
        for y in x:
            line += str(round(y,2))
        print(line)

    print(i)
    print()
    return

def update_mdp(mdp: list, utility_array: list, row: int, col: int) -> None:
    """
    This function provides a state a velocity and chooses the largest utility
    """
    for row in range(len(utility_array)):
        for col in range(len(utility_array[0])):
            max = -10
            best_x_velocity = 0
            best_y_velocity = 0
            for x_velocity in range(-5,6):
                for y_velocity in range(-5,6):
                    if utility_array[row][col][x_velocity][y_velocity] > max:
                        max = utility_array[row][col][x_velocity][y_velocity]
                        best_x_velocity = x_velocity
                        best_y_velocity = y_velocity
            mdp[row][col].set_velocity((best_x_velocity, best_y_velocity))

    return mdp

def simulate(mdp: list) -> list:
    """
    This function simulates the car driving the track
    according to the policy chosen by the value iteration function
    """
    policy = list()
    
    position = new_starting_position(mdp)
    x_position, y_position = position
    state = mdp[x_position][y_position]
    velocity = (0,0)
    state.set_velocity(velocity)

    iter = 0

    while state.get_condition() != 'F' and len(policy) < 200:
        iter += 1
        time.sleep(1)
        display_markov_list(mdp, position)
        
        policy.append(position)

        if iter == 1:
            velocity = (0,0)
            state.set_velocity(velocity)
        else:
            velocity = state.get_velocity()
        
        acceleration = state.get_best_acceleration(velocity)
        print("velocity: " + str(velocity))
        print("acceleration: " + str(acceleration))
        print()
        
        s_prime = take_action(mdp, state, acceleration)

        if determine_overshoot_finish(mdp, state, s_prime):
            state = s_prime
            position = state.get_position()
            break
        
        state = s_prime
        position = state.get_position()

    display_markov_list(mdp, position)

    policy.append(position)
    return [policy, len(policy)]

L_track = generate_markov_list("../inputFiles/L-track.txt")
value_iteration(L_track, .0001, .9, 200)

