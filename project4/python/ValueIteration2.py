#from os import curdir
from math import sqrt
import numpy as np
from ParseInput import generate_markov_list
from MarkovList import MarkovList
from MarkovNode import MarkovNode
import copy
import random

COURSE_RESET = False

def new_starting_position(mdp: list) -> tuple:
    start_list = list()

    for x, row in enumerate(mdp):
        for y, col in enumerate(row):
            if mdp[row][col].get_condition() == 'S':
                start_list.append((x, y))
    
    start_pos = random.choice(start_list)
    return start_pos

def generate_new_velocity(velocity: list, acceleration: list) -> int and int:

    xv = velocity[0] + acceleration[0]
    yv = velocity[1] + acceleration[1]

    if xv < -5: xv = -5
    if xv > 5: xv = 5
    if yv < -5: xv = -5
    if yv > 5: xv = 5

    return xv, yv

def establish_new_position(position: tuple, velocity: tuple) -> list:
    x, y = position

    xv, yv = velocity

    new_x = x + xv
    new_y = y + yv

    return [new_x, new_y]

def crash_handler(mdp: list, state: MarkovNode, s_prime: MarkovNode, course_reset=False) -> tuple:

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
    c_x, c_y = state.get_position()
    return sqrt(((x_pos - c_x)**2) + (y_pos - c_y)**2)

def take_action(mdp: list, state: MarkovNode, acceleration: tuple) -> MarkovNode:
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



def value_iteration(mdp: list, err: float, discount_factor: float) -> list:
    policy = list()

    U = [[[[0.0 for _ in range(-5, 6)] for _ in range(-5, 6)] for _ in row] for row in mdp]
    U_prime = copy.deepcopy(U)

    training_count = 0
    
    while True and training_count < 100:
        training_count += 1
        U = copy.deepcopy(U_prime)
        print_values(U, len(U), len(U[0]))


        max_rel_change = 0.0

        actions = [(0, 0),   (0, 1),  (0, -1), 
                   (1, 1),   (1, 0),  (-1, 0), 
                   (-1, -1), (-1, 1), (1, -1)]

        for row in range(len(mdp)):
            for col in range(len(mdp[0])):
                for x_velocity in range(-5,6):
                    for y_velocity in range(-5,6):
                        if mdp[row][col].get_wall_condition():
                            U_prime[row][col][x_velocity][y_velocity] = -5.0
                            continue
                        
                        
                        mdp[row][col].set_velocity((x_velocity, y_velocity))
                        new_U_prime, new_acceleration = q_value(mdp, mdp[row][col], actions, U, discount_factor)
                        # print(new_U_prime)
                        U_prime[row][col][x_velocity][y_velocity] = new_U_prime
                        mdp[row][col].set_acceleration(new_acceleration)
        
        
        
        for row in range(len(mdp)):
            for col in range(len(mdp[0])):
                for x_velocity in range(-5,6):
                    for y_velocity in range(-5,6):
                        if mdp[row][col].get_finish_condition() == 'F':
                            U_prime[row][col][x_velocity][y_velocity] = 0.0
                        change = abs(U[row][col][x_velocity][y_velocity] - U_prime[row][col][x_velocity][y_velocity])
                        if change > max_rel_change:
                            max_rel_change = change
        
        if max_rel_change < (err*(1 - discount_factor))/discount_factor:
            U = copy.deepcopy(U_prime)
            break
    
    return U


def q_value(mdp: list, state: MarkovNode, actions: list, U: list, discount_factor: float) -> float and tuple:

    best_utility = -10.0
    best_action = (0,0)
    old_x, old_y = state.get_position()
    old_x_velocity, old_y_velocity = state.get_velocity()

    for a in actions:
        s_prime = take_action(mdp, state, a)
        new_x, new_y = s_prime.get_position()
        new_x_velocity, new_y_velocity = s_prime.get_velocity()
        
        reward = 0 if s_prime.get_finish_condition() else -1

        u_value = reward + (0.8 * discount_factor * U[new_x][new_y][new_x_velocity][new_y_velocity]) 
        + (0.2 * discount_factor * U[old_x][old_y][old_x_velocity][old_y_velocity])

        if u_value > best_utility:
            best_utility = u_value
            best_action = a

    return best_utility, best_action


def print_values(utility_array: list, row: int, col: int) -> None:

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

    print()
    return

race_track = generate_markov_list("../inputFiles/O-track.txt")

value_iteration(race_track, .001, .99)

